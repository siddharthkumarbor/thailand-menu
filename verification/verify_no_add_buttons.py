from playwright.sync_api import sync_playwright, expect

def verify_no_add_buttons():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto("http://localhost:3000")

            # Wait for content to load
            page.wait_for_selector('.container')

            # Check for Add buttons. There should be none.
            # We look for button with class 'add-btn' which matches the original code
            # But they should be gone.
            add_btns = page.locator('.add-btn')
            count = add_btns.count()
            print(f"Found {count} add buttons (should be 0)")

            # Check visibly
            expect(add_btns).to_have_count(0)

            # Take screenshot of the menu
            page.screenshot(path="verification/menu_screenshot.png", full_page=True)
            print("Screenshot saved to verification/menu_screenshot.png")

        except Exception as e:
            print(f"Error: {e}")
            # Take error screenshot
            page.screenshot(path="verification/error_screenshot.png")
            raise e
        finally:
            browser.close()

if __name__ == "__main__":
    verify_no_add_buttons()
