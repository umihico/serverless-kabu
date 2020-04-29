
from chrome import ServerlessChrome
from ssm import test_get_ssm_value


def lambda_test(event=None, context=None):
    return {
        'message': 'lambda passed tests',
        'details': {
            'test_chrome': test_chrome(),
            'test_get_ssm_value': test_get_ssm_value(),
        }
    }


def test_chrome():
    chrome = ServerlessChrome()
    try:
        chrome.get("https://www.google.com/")
        assert len(chrome.xpaths("//input")) > 0
        title = chrome.title
        assert title == "Google"
        chrome.wait_element("//img")
        return title
    except Exception:
        raise
    finally:
        chrome.quit()
