from playwright.sync_api import sync_playwright

def scrape_website(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto(url)
        # Replace 'your_selector' with the actual CSS selector for the element you want to scrape
        elements = page.query_selector_all('your_selector')

        # Extracting information from the elements
        for element in elements:
            text = element.text_content()
            print(text) # Change this to process or save the scraped data

        browser.close()

if __name__ == "__main__":
    # Replace 'https://example.com' with the URL you want to scrape
    scrape_website('https://example.com')