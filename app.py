import os
import requests
from sys import argv
from wit import Wit
from bottle import Bottle, request, debug

import sys
from wit import Wit

if len(sys.argv) != 2:
    print('usage: python ' + sys.argv[0] + 'SIRWNSUEZS2YM2PIQG27N2N4MVV35YVT')
    exit(1)
access_token = 'SIRWNSUEZS2YM2PIQG27N2N4MVV35YVT'
def send(request, response):
    print(response['text'])

actions = {
    'send': send,
}

client = Wit(access_token=access_token, actions=actions)
client.interactive()


"""
# Wit.ai parameters
WIT_TOKEN = os.environ.get('SIRWNSUEZS2YM2PIQG27N2N4MVV35YVT')
# Messenger API parameters
FB_PAGE_TOKEN = os.environ.get('EAAaG4dbOagQBAPvZAuM0kAKgZCpis2rseD2TrM0Fmkci2a0zZAFfzGUbwhMSDurMrCoFKQUVQCr1TQ9Ph3HpDoqnbHrr5vP02oTBYUcmmPG6B5ePk46Qx23n1YX8EYG0qaGvZAdW6aaNH5MTJ6TK57LVVi4t2uVxw7XgtEE67QZDZD')
# A user secret to verify webhook get request.
FB_VERIFY_TOKEN = os.environ.get('test_token')

# Setup Bottle Server
debug(True)
app = Bottle()


# Facebook Messenger GET Webhook
@app.get('/webhook')
def messenger_webhook():
    """
    A webhook to return a challenge
    """
    verify_token = request.query.get('hub.verify_token')
    # check whether the verify tokens match
    if verify_token == FB_VERIFY_TOKEN:
        # respond with the challenge to confirm
        challenge = request.query.get('hub.challenge')
        return challenge
    else:
        return 'Invalid Request or Verification Token'


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
"""
