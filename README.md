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

### Subtitle Translator (v0.9.6)

Automatically translate embedded and external subtitles to your preferred language.

- **10 translation services** — Lingva (default, free), DeepL, Google Translate, Microsoft, OpenAI, Anthropic, LibreTranslate, Argos (offline), MyMemory, Yandex
- **Embedded & external subtitles** — FFmpeg extraction for MKV/MP4/AVI + .srt/.ass/.ssa/.sub/.vtt
- **Android/Shield support** — automatic FFmpeg download, no manual steps needed
- **Smart caching** — translations cached for faster repeat playback
- **Auto-fallback** — falls back to Lingva if API keys are missing
- **Translation profiles** — Anime, Kids, Documentary, etc.
- **25 UI languages** — fully translated via Transifex

**Latest changes (v0.9.6):**
- Android/Termux FFmpeg detection improved (nightly paths, PATH scanning)
- Auto-download FFmpeg on Android (one-click in dialog)
- All user-visible strings now translatable via Transifex
- Detailed installation instructions for Android/Shield

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
