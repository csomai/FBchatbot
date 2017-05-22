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
