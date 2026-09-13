import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile
from scripts import update_repository as repo


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.package = self.root / 'fixture.zip'
        with zipfile.ZipFile(self.package, 'w') as archive:
            archive.writestr('service.fixture/addon.xml', '<addon id="service.fixture" version="1.0.0"/>')
        self.patch = patch.object(repo, 'ROOT', self.root)
        self.patch.start()
        self.addCleanup(self.patch.stop)
        repo.update(self.package)

    def test_valid_index_and_packages(self):
        repo.check()

    def test_missing_package_hash_rejected(self):
        (self.root / 'service.fixture/service.fixture-1.0.0.zip.md5').unlink()
        with self.assertRaises(FileNotFoundError):
            repo.check()

    def test_wrong_index_hash_rejected(self):
        (self.root / 'addons.xml.md5').write_text('wrong')
        with self.assertRaises(ValueError):
            repo.check()

    def test_missing_package_rejected(self):
        (self.root / 'service.fixture/service.fixture-1.0.0.zip').unlink()
        with self.assertRaises(FileNotFoundError):
            repo.check()

    def test_published_version_cannot_be_replaced(self):
        with zipfile.ZipFile(self.package, 'a') as archive:
            archive.writestr('service.fixture/extra.py', 'different contents')
        with self.assertRaises(ValueError):
            repo.update(self.package)

    def test_zip_checksum_mismatch_rejected(self):
        path = self.root / 'service.fixture/service.fixture-1.0.0.zip.md5'
        path.write_text(hashlib.md5(b'other contents').hexdigest())
        with self.assertRaises(ValueError):
            repo.check()
