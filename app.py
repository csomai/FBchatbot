import os
import requests
from sys import argv
from wit import Wit
from bottle import Bottle, request, debug

import sys
from wit import Wit

# Wit.ai parameters
WIT_TOKEN = os.environ.get('SIRWNSUEZS2YM2PIQG27N2N4MVV35YVT')
# Messenger API parameters
FB_PAGE_TOKEN = os.environ.get('EAAaG4dbOagQBAPTwYpY6U1wTo31cZBSK1ZBuDn53MQlGZAJVwE8mRd0jx9RlszkQpZA300gcYk2d8JQNerofvlZAD79TtKOMNyjx0c5SQjcHryUDlKyls5goqXsGVSeXyh0tZCnEudubTjuo5JiR3FUxMZBuaZC73nZClDi1E9cZAFtgZDZD')


# Setup Bottle Server
debug(True)
app = Bottle()

# Facebook Messenger POST Webhook
@app.post('/webhook')
def messenger_post():
    """
    Handler for webhook (currently for postback and messages)
    """
    data = request.json
    if data['object'] == 'page':
        for entry in data['entry']:
            # get all the messages
            messages = entry['messaging']
            if messages[0]:
                # Get the first message
                message = messages[0]
                # Yay! We got a new message!
                # We retrieve the Facebook user ID of the sender
                fb_id = message['sender']['id']
                # We retrieve the message content
                text = message['message']['text']
                # Let's forward the message to the Wit.ai Bot Engine
                # We handle the response in the function send()
                client.run_actions(session_id=fb_id, message=text)
    else:
        # Returned another event
        return 'Received Different Event'
return None
