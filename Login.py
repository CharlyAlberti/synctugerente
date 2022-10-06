import pytest 
from playwright.sync_api import Playwright, sync_playwright, expect

@pytest.mark.skip_browser("chromium")
def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://erp.implementaconbubo.com/
    page.goto("https://erp.implementaconbubo.com/")
    # Go to https://erp.implementaconbubo.com/principal
    page.goto("https://erp.implementaconbubo.com/principal")
    # Go to https://auth.implementaconbubo.com/login?url_redirect=https://lobby.implementaconbubo.com/api/companies?url_redirect=https://erp.implementaconbubo.com/principal&url_name=tugerente
    page.goto("https://auth.implementaconbubo.com/login?url_redirect=https://lobby.implementaconbubo.com/api/companies?url_redirect=https://erp.implementaconbubo.com/principal&url_name=tugerente")
    assert page.is_visible("text=Registro")
    expect(page.locator("text=Registro")).to_be_visible()
    # ---------------------
with sync_playwright() as playwright:
    test_run(playwright)
