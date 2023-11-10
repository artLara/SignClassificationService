import json
from .Hand import Hand
def parseJSONtoHands(jsonFile):
    data = json.load(jsonFile)
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