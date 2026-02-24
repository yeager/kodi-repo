# Yeager's Kodi Repository

Custom Kodi add-on repository with automatic updates.

## Installation

1. Download [repository.yeager-1.0.1.zip](https://yeager.github.io/kodi-repo/repository.yeager-1.0.1.zip)
2. In Kodi: **Add-ons → Install from zip file** → select the downloaded zip
3. Go to **Add-ons → Install from repository → Yeager Repository**
4. Browse and install add-ons!

## Compatibility

- Kodi 19 (Matrix), 20 (Nexus), 21 (Omega), 22 (Piers)

## Available Add-ons

### Subtitle Translator (v0.9.17)

Automatically translate embedded and external subtitles to your preferred language.

- **Built-in MKV parser** — extracts subtitles directly from MKV files without FFmpeg, streams over SMB/NFS
- **10 translation services** — Lingva (default, free), DeepL, Google, Microsoft, OpenAI, Anthropic, LibreTranslate, Argos (offline), MyMemory, Yandex
- **FFmpeg optional** — only needed as fallback for non-MKV containers (MP4, AVI)
- **Android/Shield** — works out of the box, no FFmpeg or Termux needed for MKV files
- **Smart caching** — translations cached for faster repeat playback
- **Auto-fallback** — falls back to Lingva if API keys are missing
- **25 UI languages** — fully translated via Transifex

**Latest changes (v0.9.17):**
- Pure Python MKV subtitle extractor — no FFmpeg needed, streams over SMB/NFS
- Fixed OOM crash on Android (streaming parser, never loads full file)
- Fixed Lingva rate limiting (1.2s delay between requests)
- Fixed NameError crash in progress dialog
- Fixed language matching (sv/sv_se/swe all match correctly)
- Better error logging for translation troubleshooting

[Source code](https://github.com/yeager/kodi-subtitle-translator) · [Releases](https://github.com/yeager/kodi-subtitle-translator/releases)

## For Developers

Repository metadata URL: `https://raw.githubusercontent.com/yeager/kodi-repo/main/addons.xml`

Files:
- `addons.xml` — Add-on metadata
- `addons.xml.md5` — MD5 checksum
- `repository.yeager/` — Repository installer addon
- `service.subtitletranslator/` — Subtitle Translator addon zip

## Author

Daniel Nylander — [danielnylander.se](https://danielnylander.se)
