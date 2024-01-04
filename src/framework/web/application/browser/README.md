# How to use browser?

```
from framework.web.application.ports import IBrowser
from framework.web.infrastructure.factories import NoSecureBrowserFactory


def main(browser: IBrowser) -> None:
    print('Run Client')

    response = browser.get("0.0.0.0", port=3000)

    print(f'Client accepted {response}')

    response2 = browser.post("0.0.0.0", data={'hello': 'world'}, port=3000)

    print(f'Client accepted {response2}')


if __name__ == '__main__':
    # main(BrowserFactory.get_browser()) for https
    main(NoSecureBrowserFactory.get_browser()) for http
```