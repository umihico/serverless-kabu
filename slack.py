from pprint import pformat
import requests
from ssm import get_ssm_value


def send_text(text, channel_id=None):
    slack_token = get_ssm_value('SLACK_TOKEN')
    channel_id = channel_id or get_ssm_value('SLACK_DEFAULT_CHANNEL')
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': channel_id,
        'text': text,
        'username': 'kabubot',
    })


def test_send_text():
    response = send_text("THIS IS TEST.")
    response.raise_for_status()
    json = response.json()
    assert json['ok']
    response = send_text(pformat({'asset': '10,000円'}))
    response.raise_for_status()
    json = response.json()
    assert json['ok']
    return json


if __name__ == '__main__':
    test_send_text()
