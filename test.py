
from chrome import test_chrome
from ssm import test_get_ssm_value
from nomura import NomuraChrome
from slack import test_send_text


def lambda_test(event=None, context=None):
    return {
        'message': 'lambda passed tests',
        'details': {
            'test_chrome': test_chrome(),
            'test_chromes': {
                'NomuraChrome': NomuraChrome().test()
            },
            'test_slack': test_send_text(),
            'test_get_ssm_value': test_get_ssm_value(),
        }
    }
