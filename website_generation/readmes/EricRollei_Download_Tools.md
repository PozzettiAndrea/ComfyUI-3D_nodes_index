# Download Tools for ComfyUI

ComfyUI custom nodes for downloading media from 1000+ websites including Instagram, Reddit, Twitter, YouTube, TikTok, and more.

## 🎉 Features

- **Gallery-dl Node** - Download images and videos from 100+ websites
  - Instagram, Reddit, Twitter/X, DeviantArt, Pixiv, and more
  - **Resolution filtering** - Skip small images (default: 768px minimum)
  - Supports authentication via config file or browser cookies
  - Automatic file organization
  - Download archive to avoid duplicates
  - **Persistent config paths** - Paths are remembered between sessions
  - **Configurable timeout** - Up to 1 hour for large downloads

- **Web Image Scraper Node** - Extract images from any website via Playwright
  - 25+ site-specific handlers for optimised extraction
  - Automatic full-resolution image detection (skips thumbnails)
  - Multi-page pagination and infinite-scroll support
  - Spoiler / hidden-content auto-reveal (IPS forums)
  - Video link collection (YouTube / Vimeo) for use with yt-dlp
  - Duplicate detection via perceptual hashing
  - Configurable minimum dimensions, parallel downloads

- **Yt-dlp Node** - Download videos and audio from 1800+ platforms
  - YouTube, TikTok, Vimeo, Twitch, and more
  - Multiple quality options
  - Audio extraction support
  - Playlist support
  - Authentication via cookies or credentials

## 📺 Yt-dlp Supported Sites (Major Platforms)

The yt-dlp node supports **1800+ websites**. Here are the most popular ones:

### Video Platforms
| Platform | Features | Auth Required |
|----------|----------|---------------|
| **YouTube** | Videos, playlists, channels, shorts, live streams, music | Optional (for age-restricted/private) |
| **Vimeo** | Videos, albums, channels, on-demand, showcases | Optional (for private content) |
| **Twitch** | VODs, clips, live streams | Optional |
| **TikTok** | Videos, user profiles, collections | No |
| **Dailymotion** | Videos, playlists, user content | Optional |
| **Facebook** | Videos, reels, ads | No |
| **Instagram** | Videos, reels, stories | No (use gallery-dl for images) |
| **Twitter/X** | Videos, spaces, broadcasts | No |
| **Reddit** | Video posts | No |
| **Rumble** | Videos, channels | No |
| **Kick** | VODs, clips, live streams | No |
| **Odysee/LBRY** | Videos, channels, playlists | No |

### Streaming Services (May Require Subscription)
| Platform | Notes |
|----------|-------|
| **Crunchyroll** | Anime streaming |
| **Nebula** | Creator platform |
| **CuriosityStream** | Documentaries |
| **Dropout** | Comedy streaming |
| **Patreon** | Creator videos |
| **Floatplane** | Tech creator content |

### Music & Audio
| Platform | Features |
|----------|----------|
| **SoundCloud** | Tracks, playlists, user content |
| **Bandcamp** | Albums, tracks |
| **Mixcloud** | Mixes, playlists |
| **Audiomack** | Tracks, albums |
| **Spotify** | Podcasts only (not music) |
| **Apple Podcasts** | Podcast episodes |

### News & Media
| Platform | Notes |
|----------|-------|
| **BBC iPlayer** | UK content |
| **PBS** | US public broadcasting |
| **CBS News** | News clips |
| **NBC** | News and shows |
| **CNN** | News clips |
| **ESPN** | Sports clips |
| **Arte** | European culture |

### Educational
| Platform | Notes |
|----------|-------|
| **Khan Academy** | Free courses |
| **TED** | Talks and playlists |
| **Udemy** | Requires login |
| **LinkedIn Learning** | Requires subscription |
| **Coursera** | Some content |

### Other Popular Sites
| Platform | Type |
|----------|------|
| **Bilibili** | Chinese video platform |
| **NicoNico** | Japanese video platform |
| **VK** | Russian social network |
| **Weibo** | Chinese social media |
| **Archive.org** | Internet Archive |
| **Dropbox** | Shared videos |
| **Google Drive** | Shared videos |
| **Steam** | Game trailers |
| **Imgur** | Video content |

### Full List
For the complete list of 1800+ supported sites, see the [official yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

### Site-Specific Authentication

Some sites work better with authentication:

```bash
# Using .netrc file (recommended for security)
--netrc

# Using username/password directly
--username YOUR_EMAIL --password YOUR_PASSWORD

# Using browser cookies
--cookies-from-browser firefox
```

**Tip:** For sites like Vimeo, YouTube (age-restricted), or any subscription service, authentication unlocks more content.

## 🌐 Web Image Scraper – Site Handlers

The Web Image Scraper node ships with **25+ site-specific handlers** that understand each site's DOM structure and extract full-resolution images automatically. A generic handler covers everything else.

| Handler | Sites | Key Features |
|---------|-------|--------------|
| **BellazonHandler** | bellazon.com (IPS / Invision Community forums) | Full-res from `<a>` hrefs (not thumbnails); auto-paginate all topic pages; opens spoiler / hidden-content blocks; collects YouTube & Vimeo video links |
| **InstagramHandler** | instagram.com | Posts, reels, stories; cookie auth |
| **RedditHandler** | reddit.com | Gallery posts, age-gate bypass |
| **BskyHandler** | bsky.app | Bluesky AT Protocol API |
| **PinterestHandler** | pinterest.com | Pin boards, infinite scroll |
| **FlickrHandler** | flickr.com | Original-size downloads |
| **DeviantArtHandler** | deviantart.com | Full-resolution deviations |
| **ArtStationHandler** | artstation.com | Project galleries |
| **BehanceHandler** | behance.net | Project modules |
| **500pxHandler** | 500px.com | Photo pages |
| **UnsplashHandler** | unsplash.com | Full-res downloads |
| **TumblrHandler** | tumblr.com | Blog posts |
| **KavyarHandler** | kavyar.com | Model portfolios |
| **CosmosHandler** | cosmos.so | Boards & collections |
| **GoogleArtsHandler** | artsandculture.google.com | High-res artwork tiles |
| **ArtsyHandler** | artsy.net | Artwork pages |
| **ModelMayhemHandler** | modelmayhem.com | Portfolio images |
| **WixHandler** | Wix-powered sites | Wix media URLs |
| **WordPressHandler** | WordPress sites | Featured images, galleries |
| **YouTubeHandler** | youtube.com | Thumbnails, channel art |
| **PortfolioHandler** | Generic portfolio sites | Common portfolio layouts |
| **GenericHandler** | Any website | Fallback: extracts all images meeting size thresholds |

### IPS / Invision Community Forums (Bellazon)

The **BellazonHandler** is purpose-built for Invision Community (IPS) forums:

- **Full-resolution only** — IPS thumbnails use a different hash than the full-res image, so the handler reads the authoritative `<a href>` and `data-full-image` attributes instead of trying to rewrite thumbnail URLs.
- **Spoiler handling** — Automatically opens `<details>` spoiler blocks ("Spoiler", "Spoiler Nudity", "Reveal hidden contents", etc.) before extraction so hidden images are included.
- **Multi-page pagination** — Detects "PAGE X OF Y" controls and walks through every page of a topic automatically.
- **Video link collection** — YouTube and Vimeo URLs embedded in posts are collected and returned as video items for optional download with the yt-dlp node.
- **Zero thumbnail downloads** — Any URL containing `.thumb.` is hard-rejected at three levels (JS extraction, Python filter, post-processing).

To add support for another IPS-powered forum, just add its domain to the `IPS_DOMAINS` list in `site_handlers/bellazon_handler.py`.

## 📦 Installation

### Using ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "Download Tools"
3. Click Install

### Manual Installation

1. Clone or download this repository to your ComfyUI custom_nodes folder:
   ```powershell
   cd ComfyUI/custom_nodes
   git clone https://github.com/EricRollei/download-tools.git
   ```

2. Install dependencies:
   ```powershell
   # Windows (using ComfyUI's Python)
   .\ComfyUI\python_embeded\python.exe -m pip install -r download-tools\requirements.txt
   
   # Or using system Python
   pip install -r download-tools/requirements.txt
   ```

3. (Optional) Install FFmpeg for audio extraction:
   - Windows: `choco install ffmpeg` or download from https://ffmpeg.org/
   - macOS: `brew install ffmpeg`
   - Linux: `apt-get install ffmpeg`

4. Restart ComfyUI

## 🚀 Quick Start

### Gallery-dl Downloader

1. Add "Gallery-dl Downloader" node to your workflow
2. Enter a URL (e.g., Instagram profile, Reddit post)
3. Configure options:
   - Set `config_path` to `./configs/gallery-dl.conf` (auto-saved for next time)
   - Enable `filter_by_resolution` to skip small images (768px default)
   - Enable `organize_files` to sort by type
   - Enable `use_download_archive` to avoid duplicates
   - Increase `download_timeout` for large galleries (default: 600s)
4. Execute!

**Supported Sites:** Instagram, Reddit, Twitter, DeviantArt, Pixiv, Tumblr, Pinterest, Flickr, and 90+ more. See [gallery-dl supported sites](https://github.com/mikf/gallery-dl/blob/master/docs/supportedsites.md).

### Yt-dlp Downloader

1. Add "Yt-dlp Downloader" node to your workflow
2. Enter a URL (e.g., YouTube video, Vimeo, Twitch VOD, TikTok)
3. Choose format:
   - `best` - Best quality video
   - `best[height<=1080]` - Best quality up to 1080p
   - `audio-only` - Extract audio (requires FFmpeg)
   - Custom format string
4. For private content, enable browser cookies or use config file with credentials
5. Execute!

**Supported Sites:** YouTube, Vimeo, TikTok, Twitch, Facebook, Instagram, Twitter, Dailymotion, SoundCloud, and 1800+ more. See [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) or the table above.

## � Instagram Downloads

**For Instagram, use Gallery-dl as it is better.** Gallery-dl has native Instagram API support, handles pagination, rate limits, and can download posts, stories, reels, and highlights.

### Recommended Settings

| Setting | Value | Notes |
|---------|-------|-------|
| `config_path` | `./configs/gallery-dl.conf` | Contains all site credentials (auto-saved) |
| `cookie_file` | *(leave empty)* | Cookies are in config file |
| `use_browser_cookies` | ❌ False | Config file is more reliable |
| `filter_by_resolution` | ✅ True | Skip thumbnails and small images |
| `min_image_width/height` | 768 | Minimum resolution in pixels |

### One Config For All Sites

The `gallery-dl.conf` file contains credentials for **all supported sites** (Instagram, Reddit, 500px, DeviantArt, Pinterest, Flickr, Bluesky). Gallery-dl automatically uses the right credentials based on the URL you're downloading from.

### Why Not Browser Cookies?

- **Chrome/Edge:** Require admin privileges AND browser must be closed
- **Firefox:** Works without admin, but less reliable than config file
- **Config file:** Most reliable method - always works

### Setting Up Instagram Authentication

1. **Export your Instagram cookies** from Chrome/Firefox using "Get cookies.txt LOCALLY" extension
2. **Copy the key cookies** to `configs/gallery-dl.conf` in the `instagram` section:
   ```json
   "instagram": {
       "cookies": {
           "sessionid": "YOUR_SESSION_ID",
           "ds_user_id": "YOUR_USER_ID", 
           "csrftoken": "YOUR_CSRF_TOKEN",
           "mid": "YOUR_MID_VALUE"
       }
   }
   ```
3. **Use in node:**
   - Set `config_path` to `./configs/gallery-dl.conf`
   - Leave `cookie_file` empty
   - Set `use_browser_cookies` to False

### Cookie Expiration

Instagram session cookies expire after ~1 year. If downloads start failing with 401 errors, export fresh cookies from your browser.

## �🔐 Authentication

Many sites require authentication for private content:

### Method 1: Browser Cookies (Automatic)

1. Log into the website in your browser
2. Enable `use_browser_cookies` in the node
3. Select your browser (Chrome, Firefox, Edge, etc.)
4. The node will automatically use your login session

### Method 2: Export Cookies

1. Install browser extension: "Get cookies.txt LOCALLY"
2. Log into the website
3. Export cookies
4. Save to `configs/instagram_cookies.json` (or site-specific file)
5. Set `cookie_file` parameter in the node

## 📁 Configuration

Config files are stored in `download-tools/configs/`:

- `gallery-dl.conf` - **Main config** with credentials for all sites (Instagram, Reddit, 500px, DeviantArt, Pinterest, Flickr, Bluesky)
- `gallery-dl.conf.example` - Template for creating your own config
- `yt-dlp.conf.example` - Yt-dlp template (copy to `yt-dlp.conf` and add your credentials)
- `yt-dlp-audio.conf` - Audio extraction preset
- `yt-dlp-hq.conf` - High quality preset

### Persistent Paths

Config file paths are **automatically saved** between ComfyUI sessions. Once you set `config_path` or `cookie_file`, they'll be remembered for next time.

## 📚 Documentation

Detailed guides available in `Docs/`:

- `gallery_dl_node_complete_guide.md` - Complete gallery-dl usage
- `yt_dlp_node_complete_guide.md` - Complete yt-dlp usage
- `gallery_dl_authentication_guide.md` - Authentication setup
- `gallery_dl_advanced_options_guide.md` - Advanced features

## 🐛 Troubleshooting

### "gallery-dl not found"
Already installed! It's a Python package. The node will find it automatically.

### "Chrome cookies not accessible"
Chrome locks its cookie database while running. Solutions:
- Close Chrome completely before running
- Run ComfyUI as administrator
- Use Firefox instead (doesn't require admin)
- **Best:** Use config file with cookies (see Instagram section above)

### "Instagram/Reddit downloads fail"
Authentication required:
- Use `config_path: ./configs/gallery-dl.conf` with cookies
- Or enable `use_browser_cookies` with Firefox
- 401 Unauthorized = expired cookies, export fresh ones

### "Downloads timing out"
For large galleries:
- Increase `download_timeout` (default: 1800s / 30 min, max: 10 hours)
- Large Instagram profiles may need several hours
- If a download times out, just run again — gallery-dl automatically resumes using the download archive

### "Too many small images"
Enable resolution filtering:
- Set `filter_by_resolution` to True
- Adjust `min_image_width` and `min_image_height` (default: 768px)
- Videos are never filtered, only images

### "CUDA out of memory" / "FFmpeg not found"
For audio extraction:
- Install FFmpeg separately
- Or use video formats

## ⚙️ Requirements

- Python 3.10+
- ComfyUI
- gallery-dl (auto-installed)
- yt-dlp (auto-installed)
- FFmpeg (optional, for audio extraction)

## 📄 License

Copyright (c) 2025 Eric Hiss. All rights reserved.

**Dual License:**
- **Non-Commercial Use:** Licensed under [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](http://creativecommons.org/licenses/by-nc/4.0/)
- **Commercial Use:** Requires a separate commercial license. Contact: eric@historic.camera or eric@rollei.us

See [LICENSE.md](LICENSE.md) for full terms.

### Third-Party Tools

- **gallery-dl** (GNU GPL v2) by Mike Fährmann: https://github.com/mikf/gallery-dl
- **yt-dlp** (Unlicense/Public Domain): https://github.com/yt-dlp/yt-dlp

See [CREDITS.md](CREDITS.md) for complete dependency list.

## 👥 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📧 Contact

- **Author:** Eric Hiss
- **GitHub:** [EricRollei](https://github.com/EricRollei)
- **Email:** eric@historic.camera, eric@rollei.us

## 🙏 Acknowledgments

- **ComfyUI** community for the platform
- **Mike Fährmann** for gallery-dl
- **yt-dlp** contributors for the excellent video downloader

---

**Ready to download!** 🚀 Add the nodes to your workflow and start downloading media from across the web.
