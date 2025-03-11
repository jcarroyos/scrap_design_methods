# Scrap Design Methods

This project scrapes data from the following websites:

- [Dave Birss Free Resources](https://davebirss.com/free-resources/)
- [Hyper Island Toolbox](https://hyperisland.com/en/toolbox)

## Usage

To scrape data from these websites, run the following JavaScript functions in the browser console.

### Dave Birss Free Resources

```javascript
function scrapeElementorCards() {
    try {
        // Select all Elementor card containers
        const cards = document.querySelectorAll('.elementor-element-5d35dc6a');
        let csvData = "Title;Description;Link;Image Path\n"; // Updated order

        cards.forEach(card => {
            const title = card.querySelector('.elementor-icon-box-title a')?.innerText.trim() || '';
            const description = card.querySelector('.elementor-widget-text-editor p')?.innerText.trim() || '';
            const link = card.querySelector('.elementor-button-link')?.href || '';

            // Extract background image from CSS
            let imagePath = '';
            const bgElement = card.querySelector('.elementor-element-2df273c4'); // Adjust selector as needed
            if (bgElement) {
                const bgStyle = window.getComputedStyle(bgElement).backgroundImage;
                if (bgStyle && bgStyle.startsWith('url')) {
                    imagePath = bgStyle.replace(/url\(["']?(.*?)["']?\)/, '$1'); // Extract URL from CSS
                }
            }

            csvData += `"${title}";"${description}";"${link}";"${imagePath}"\n`;
        });

        console.log(csvData); // Logs CSV formatted data with semicolon separator
    } catch (error) {
        console.error("Error scraping Elementor cards:", error);
    }
}

// Run the function in the browser console
scrapeElementorCards();
```

### Hyper Island Toolbox

```javascript
function scrapeWebsite(htmlBlockClass) {
    try {
        // Find the specified HTML blocks by class
        const blocks = document.querySelectorAll(`.${htmlBlockClass}`);
        let csvData = "Title;Description;Link;Image Path\n"; // Title is now first

        blocks.forEach(block => {
            const h4Text = block.querySelector('h4')?.innerText.trim() || '';
            const textDescription = block.querySelector('.text-description')?.innerText.trim() || '';
            const anchor = block.querySelector('a')?.href || '';

            // Try to get the image from an <img> tag
            let imagePath = block.querySelector('img')?.src || '';

            // If no <img> found, check for a background image in CSS
            if (!imagePath) {
                const bgElement = block.querySelector('.background-image'); // Adjust selector if needed
                if (bgElement) {
                    const bgStyle = window.getComputedStyle(bgElement).backgroundImage;
                    if (bgStyle && bgStyle.startsWith('url')) {
                        imagePath = bgStyle.replace(/url\(["']?(.*?)["']?\)/, '$1'); // Extract the URL from CSS
                    }
                }
            }

            csvData += `"${h4Text}";"${textDescription}";"${anchor}";"${imagePath}"\n`;
        });

        console.log(csvData); // Logs CSV formatted data with semicolon separator
    } catch (error) {
        console.error("Error scraping the webpage:", error);
    }
}

// Example usage in the browser console
scrapeWebsite('lMnBhZ3gjfo2MMbjeZ19');
```