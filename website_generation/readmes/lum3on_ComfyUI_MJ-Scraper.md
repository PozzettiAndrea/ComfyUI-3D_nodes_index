# ComfyUI Midjourney Scraper Node

This custom node for ComfyUI allows you to scrape and download images and videos from the Midjourney showcase pages. It uses `undetected_chromedriver` to bypass anti-scraping measures, but requires session cookies from a logged-in browser session to function correctly.

## Features

- Scrapes both images and videos from Midjourney showcase URLs.
- Transforms `.webp` image thumbnails to full `.png` images.
- Transforms `.webp` video thumbnails to `.mp4` videos.
- Implements a retry mechanism with a file size check to ensure downloads are complete and not corrupted.
- Allows customization of the number of items to scrape, output directory, and other browser settings.

## Installation

1.  **Clone the Repository**:
    Navigate to your `ComfyUI/custom_nodes/` directory and clone this repository.
    ```bash
    cd /path/to/ComfyUI/custom_nodes/
    git clone <repository_url> ComfyUI_MJ-Scraper
    ```

2.  **Install Dependencies**:
    Navigate into the cloned directory and install the required Python packages using the `requirements.txt` file.
    ```bash
    cd ComfyUI_MJ-Scraper
    pip install -r requirements.txt
    ```

3.  **Update Google Chrome**:
    Ensure you have an up-to-date version of Google Chrome installed. The `undetected_chromedriver` library works best with the latest browser version.

4.  **Restart ComfyUI**:
    Completely restart your ComfyUI application to ensure the new custom node is loaded.

## Usage

After installation, you will find the **Midjourney Scraper** node under the **Image Scrapers** category in ComfyUI.

### Getting Your Midjourney Cookies

This is the most critical step to make the scraper work. Midjourney uses strong anti-bot protection, and you need to provide session cookies from a logged-in browser to bypass it.

1.  Open your regular web browser (e.g., Chrome) and log in to your Midjourney account.
2.  Navigate to the Midjourney showcase page you want to scrape (e.g., `https://www.midjourney.com/showcase/top/`).
3.  Open your browser's **Developer Tools** (you can press `F12` or right-click on the page and select "Inspect").
4.  Go to the **Network** tab in the Developer Tools.
5.  Refresh the page. You will see a list of network requests.
6.  Click on the first request in the list (it should be the main page URL).
7.  In the "Headers" tab for that request, scroll down to the **Request Headers** section.
8.  Find the `cookie` header. **Right-click and copy the entire value** of this header. It will be a long string of text.
9.  Paste this entire string into the `cookies` input field on the Midjourney Scraper node in ComfyUI.

### Node Inputs

-   `search_url`: The URL of the Midjourney showcase page to scrape (e.g., `https://midjourney.com/showcase/top/`).
-   `output_directory`: The directory where the downloaded images and videos will be saved.
-   `num_images_to_scrape`: The maximum number of items to download.
-   `timeout`: The time in seconds to wait for the page to load.
-   `headless`: If `True`, the Chrome browser will run in the background without a visible UI.
-   `cookies`: The session cookies copied from your logged-in browser session. **This is required for the node to work.**

### Node Outputs

-   `image_paths`: A comma-separated string containing the file paths of all successfully downloaded images and videos.