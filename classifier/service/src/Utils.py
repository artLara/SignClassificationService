import json
from .Hand import Hand
def parseJSONtoHands(jsonFile='', data = None):
    
    if data != None: #http request
        data = data['json_payload']

    elif jsonFile != '':#json file for testing
        data = json.load(jsonFile)

    else:
        print('Error: jsonFile or data parameters have to be valid')
        return []
    
        
    word = [] #This list has only signs of a specific word
    signWords = [] #This list has all the lists of words
    for handData in data['hands']:
        if handData != None:
            hand = Hand()
            hand.setAttributes(handData)
            word.append(hand)
        else:
            if len(word) > 0: #Avoid empty list
                signWords.append(word)
                word = []

    return signWords