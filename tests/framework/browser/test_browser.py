from framework.web.application.ports import IBrowser


def test_browser3_get(browser: IBrowser):
    browser.get('google.com')
