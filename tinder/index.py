from sense_hat import SenseHat
import json
import requests
from time import sleep
import sys

sense = SenseHat()

# tinder app
def tinder():
    request = requests.get('https://randomuser.me/api').json()
    with open('data.json', 'a') as json_data:
        json.dump(request, json_data)

    data = request['results'][0]
    name = data['name']['first']
    sense.show_message(name)
tinder()

while 1:
    for event in sense.stick.get_events():
        if event.action =="pressed":
            if event.direction == 'left':
                sense.clear(255,0,0)
                sense.show_message('disliked')
            elif event.direction == "right":
                sense.clear(0,255,0)
                sense.show_message('liked')
    tinder()
    sleep(1)
    sense.clear()
