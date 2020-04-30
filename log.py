
from nomura import NomuraChrome
from slack import send_text
from pprint import pformat


def log(event=None, context=None):
    result = NomuraChrome().get_current_asset()
    send_text(pformat(result))
    return result


if __name__ == '__main__':
    log()
