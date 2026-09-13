#!/usr/bin/env python3
"""Publish a release ZIP locally and validate Kodi index/package checksums."""
from pathlib import Path
import argparse
import hashlib
import re
import shutil
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def package_metadata(path):
    with zipfile.ZipFile(path) as archive:
        manifests = [n for n in archive.namelist() if len(Path(n).parts) == 2 and n.endswith('/addon.xml')]
        if len(manifests) != 1 or archive.testzip():
            raise ValueError('Invalid Kodi package: ' + str(path))
        data = archive.read(manifests[0])
        addon = ET.fromstring(data)
        addon_id, version = addon.get('id', ''), addon.get('version', '')
        if not re.fullmatch(r'[a-z0-9._-]+', addon_id) or not re.fullmatch(r'[0-9A-Za-z._-]+', version):
            raise ValueError('Invalid addon identity')
        for asset in addon.findall('./extension/assets/*'):
            if not asset.text:
                continue
            relative = Path(asset.text)
            if relative.is_absolute() or '..' in relative.parts or addon_id + '/' + relative.as_posix() not in archive.namelist():
                raise ValueError('Missing or invalid packaged artwork: ' + asset.text)
        if manifests[0] != addon_id + '/addon.xml':
            raise ValueError('Package root does not match addon ID')
        return addon_id, version, data


def checksum(path):
    return hashlib.md5(path.read_bytes()).hexdigest()


def update(package=None):
    if package:
        addon_id, version, data = package_metadata(package)
        directory = ROOT / addon_id
        directory.mkdir(exist_ok=True)
        destination = directory / (addon_id + '-' + version + '.zip')
        if destination.exists() and destination.read_bytes() != Path(package).read_bytes():
            raise ValueError('Do not replace an existing version with different package contents')
        if Path(package).resolve() != destination.resolve():
            shutil.copyfile(package, destination)
        (directory / 'addon.xml').write_bytes(data)
    index = ET.Element('addons')
    for manifest in sorted(ROOT.glob('*/addon.xml')):
        index.append(ET.parse(manifest).getroot())
    data = ET.tostring(index, encoding='UTF-8', xml_declaration=True)
    (ROOT / 'addons.xml').write_bytes(b'\n'.join(line.rstrip() for line in data.splitlines()) + b'\n')
    for path in [ROOT / 'addons.xml'] + sorted(ROOT.rglob('*.zip')):
        path.with_name(path.name + '.md5').write_text(checksum(path) + '\n')


def check():
    index = ROOT / 'addons.xml'
    if index.with_name('addons.xml.md5').read_text().strip() != checksum(index):
        raise ValueError('Index checksum mismatch')
    for addon in ET.parse(index).getroot():
        addon_id, version = addon.get('id'), addon.get('version')
        path = ROOT / addon_id / (addon_id + '-' + version + '.zip')
        package_id, package_version, data = package_metadata(path)
        if (package_id, package_version) != (addon_id, version):
            raise ValueError('Index/package version mismatch')
        addon.tail = None
        normalize = lambda node: b'\n'.join(line.rstrip() for line in ET.tostring(node).splitlines())
        if normalize(ET.fromstring(data)) != normalize(addon):
            raise ValueError('Index/package metadata mismatch')
        if path.with_name(path.name + '.md5').read_text().strip() != checksum(path):
            raise ValueError('Package checksum mismatch: ' + str(path))
        print('OK:', path.relative_to(ROOT))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package', type=Path)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    if args.check and args.package:
        parser.error('--check cannot publish a package')
    if not args.check:
        update(args.package)
    check()
