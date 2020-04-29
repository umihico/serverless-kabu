from boto3 import client


"""
How to register credential
aws ssm put-parameter --name NOMURA_ACCOUNT_NUMBER_DUMMY --type "String" --overwrite --value 111222333
"""


def get_ssm_value(key):
    return client('ssm').get_parameter(Name=key)['Parameter']['Value']


def test_get_ssm_value():
    account_number = get_ssm_value("NOMURA_ACCOUNT_NUMBER_DUMMY")
    assert account_number == "111222333"
    print(account_number)
    return account_number
