

from pprint import pprint
from datetime import datetime
import time

print(time.time())

messages = [
  {
    'name': 'Jack',
    'text': 'Привет всем, я Jack',
    'time': 1614887902.9050515,
  },
  {
    'name': 'Mary',
    'text': 'Привет всем, я Mary',
    'time': 1614887904.9050515,
  }
]
pprint(messages)
print()
# print(messages[0]['text'], messages[0]['name'], sep='|')


def send_message(name, text):
    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    messages.append(message)

def get_messages(after):
    response = []
    for message in messages:
        if message['time'] > after:
            response.append(message)
    return response[:50]

send_message('Jack', 'Привет, Mary')

response = get_messages(0)
pprint(response)
print()

after = response[-1]['time']

response = get_messages(after)
pprint(response)
print()

response = get_messages(after)
pprint(response)
print()

send_message('Jack', '1')
send_message('Jack', '2')

response = get_messages(after)
pprint(response)
print()

after = response[-1]['time']
