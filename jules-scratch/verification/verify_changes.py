import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Navigate to the local index.html file via the HTTP server
        await page.goto("http://localhost:8000/index.html")

        # 1. Take a screenshot of the main CEO dashboard
        await expect(page.locator("#page-dashboard")).to_be_visible()
        await page.screenshot(path="jules-scratch/verification/ceo_dashboard.png")
        print("Took screenshot of CEO Dashboard")

        # 2. Navigate to the "Settings" page and take a screenshot
        await page.locator("#nav-settings").click()
        await expect(page.locator("#page-settings")).to_be_visible()
        await page.screenshot(path="jules-scratch/verification/settings_page.png")
        print("Took screenshot of Settings Page")

        # 3. Switch to the "VC" view and take a screenshot
        await page.locator("#view-toggle").check()
        await expect(page.locator("#page-vc-dashboard")).to_be_visible()
        await page.screenshot(path="jules-scratch/verification/vc_dashboard.png")
        print("Took screenshot of VC Dashboard")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())