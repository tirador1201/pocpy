import re
from playwright.sync_api import Page, expect

from api.models.transaction_models import CashOutTransactionStatusRequest
from api.requests.transaction_requests import TransactionRequests
from pages.main import MainPage


def test_has_title(page: Page):

    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    wsdl_url = 'http://example.com'
    cash_out_transaction_status_request = {'merchantId': 123, 'merchantKeyword': 123, 'referenceNr': 123}
    soap_results = TransactionRequests(wsdl_url).get_cash_out_transaction_status(**cash_out_transaction_status_request)

    # Click the get started link.
    main_page = MainPage(page)
    main_page.click_link()
    # page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()