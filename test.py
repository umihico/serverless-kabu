
from chrome import test_chrome
from ssm import test_get_ssm_value


def lambda_test(event=None, context=None):
    return {
        'message': 'lambda passed tests',
        'details': {
            'test_chrome': test_chrome(),
            'test_get_ssm_value': test_get_ssm_value(),
        }
    }
