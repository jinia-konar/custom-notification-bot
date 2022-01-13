import requests
import random
import json
import sys
import random

def selectFriend():
    fellowTeamMates = ["Aman", "Siddhant", "Ankit", "Vinit", "Gunjan", "Palak"]

    return(fellowTeamMates[random.randint(0, len(fellowTeamMates)-1)])

if __name__ == '__main__':
    url = "https://hooks.slack.com/services/T0000000000/B0000000000/XXXXXXXXXXXXXXXXXXXXXXXX"
    friend = selectFriend()
    message = (friend)
    title = (f"Have a chit chat with :zap:")
    slack_data = {
        "username": "NotificationBot",
        "icon_emoji": ":satellite:",
        "channel" : "#dosto",
        "text": "Want to talk to " + message + "?",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": message,
                        "short": "false",
                    }
                ]
            }
        ]
    }
    byte_length = str(sys.getsizeof(slack_data))
    headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
    response = requests.post(url, data=json.dumps(slack_data), headers=headers)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)