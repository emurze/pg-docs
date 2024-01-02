from src.framework.server.ports import IBrowser


def test_browser_get(browser: IBrowser):
    pr = browser.get("https://python.org")

    print(pr)
