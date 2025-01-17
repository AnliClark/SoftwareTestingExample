import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(channel="chrome", headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://github.com/")
    page.get_by_label("Search or jump to…").click()
    page.get_by_role("combobox", name="Search").fill("testing")
    page.get_by_role("combobox", name="Search").press("Enter")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)