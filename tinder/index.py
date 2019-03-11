from sense_hat import SenseHat
import json
import requests
import time
import sys

sense = SenseHat()

# get data from json
def dataFromJson():
    with open('data.json') as json_data:
        data = json.load(json_data)
        return data


# display name
def getUsers():
    request = requests.get('https://randomuser.me/api').json()

    global data = request['results'][0]
    global name = data['name']['first']
    global gender = data['gender']
    global location = data['location']['city']

    sense.show_message(name)
    sense.show_message(gender)
    sense.show_message(location)

    return name
    return gender
    return location

# save data to json
def dataToJson(user, joystick, dataset):
    data = dataset
    if(joystick == 'liked'):
        data['liked'].append(user)
        sense.set_pixel(0,0, [0,255,0])
    else:
        data['disliked'].append(user)
        sense.set_pixel(0,0, [255,0,0])
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

# swipe
def swipe():
    try: 
        data = dataFromJson()
        user = getUsers()
        events = sense.stick.get_events()
        if(len(events) != 0):
            choiceEvent = events[0]
        else:
            choiceEvent = sense.stick.wait_for_event()
        if(choiceEvent.direction == 'right'):
            choice = 'disliked'
        else:
            choice = 'liked'
        dataToJson(user, joystick, data)
        time.sleep(1)
 
except KeyboardInterrupt:
    sense.clear()
    quit()
    sys.exit(0)
