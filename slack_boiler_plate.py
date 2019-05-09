import os
import time
import re
from slackclient import SlackClient

slack_client = SlackClient('xoxb-446465326693-619141708722-KddJvAgGKYrVzfK95UUbTRKj')
starterbot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM
MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events):
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == starterbot_id:
                return message, event["channel"]
    return None, None

def parse_direct_mention(message_text):
    matches = re.search(MENTION_REGEX, message_text)
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)

def handle_command(command, channel):
    # Required Variables
    # command
    # response
    response = ""
    if "running-config" in command:
        response = "May I clarify which device it is?"
    else:
        response = "Sorry Master I do not know what you mean"

    device_config = {
            "LPCDH-01" : "switchport mode access",
            "LPCDH-02" : "switchport mode trunk"
    }  

    if "LPCDH-01" in command:
        response = device_config["LPCDH-01"]
    elif "LPCDH-02" in command:
        response = device_config["LPCDH-02"]
    else:
        response = "Master there is no device like that"
    
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=response
    )

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Starter Bot connected and running!")
        # Read bot's user ID by calling Web API method `auth.test`
        starterbot_id = slack_client.api_call("auth.test")["user_id"]
        while True:
            command, channel = parse_bot_commands(slack_client.rtm_read())
            if command:
                handle_command(command, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")
