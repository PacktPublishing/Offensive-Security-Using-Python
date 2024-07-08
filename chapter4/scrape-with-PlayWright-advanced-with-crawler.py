from playwright.sync_api import sync_playwright

def scrape_data():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()

        # Open a new page
        page = context.new_page()

        # Navigate to the website
        page.goto('https://example.com')

        # Example: Log in (replace these with your actual login logic)
        page.fill('input[name="username"]', 'your_username')
        page.fill('input[name="password"]', 'your_password')
        page.click('button[type="submit"]')

        # Wait for navigation to dashboard or relevant page after login
        page.wait_for_load_state('load')

        # Start crawling and scraping
        scraped_data = []

        while True:
            # Scraping data on the current page
            data_elements = page.query_selector_all('.data-element-selector')
            scraped_data.extend([element.text_content() for element in data_elements])

            # Look for the 'next page' button or link
            next_page_button = page.query_selector('.next-page-button-selector')

            if not next_page_button:
                # If no next page is found, stop crawling
                break

             # Click on the 'next page' button
            next_page_button.click()
            # Wait for the new page to load
            page.wait_for_load_state('load')

        # Print or process scraped data from all pages
        for data in scraped_data:
            print(data)

        # Close the browser
        context.close()

if __name__ == "__main__":
    scrape_data()