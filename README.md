# Yeager's Kodi Repository

Custom Kodi add-on repository.

## Installation

1. Download [repository.yeager-1.0.0.zip](https://yeager.github.io/kodi-repo/repository.yeager/repository.yeager-1.0.0.zip)
2. In Kodi, go to **Add-ons** → **Install from zip file**
3. Select the downloaded zip file
4. Go to **Add-ons** → **Install from repository** → **Yeager Repository**
5. Browse and install add-ons!

## Available Add-ons

### Subtitle Translator (v0.9.5)
Automatically translate embedded subtitles to your preferred language.

- **10 translation services** — Lingva, MyMemory, DeepL (Pro & Free), Google Translate, Microsoft, OpenAI, Anthropic, LibreTranslate, and more
- **FFmpeg subtitle extraction** — MKV, MP4, AVI and other containers
- **Smart caching** — translations cached for faster repeat playback
- **Auto-selection** — newly translated subtitles selected automatically
- **Auto-fallback** — falls back to Lingva if API keys are missing
- **FFmpeg helper** — guided installation dialog when FFmpeg not found
- **25 languages** — UI translated via Transifex

**Latest changes (v0.9.5):**
- GitHub Actions CI (Transifex sync + automated builds)
- DeepL Free API key bugfix
- FFmpeg not found dialog with platform-specific instructions
- Auto-fallback to Lingva when API keys missing

[Source code](https://github.com/yeager/kodi-subtitle-translator) · [Releases](https://github.com/yeager/kodi-subtitle-translator/releases)

## For Developers

Repository URL: `https://yeager.github.io/kodi-repo/`

Files:
- `addons.xml` — Add-on metadata
- `addons.xml.md5` — Checksum
- `repository.yeager/` — Repository installer
- `service.subtitletranslator/` — Subtitle Translator add-on
