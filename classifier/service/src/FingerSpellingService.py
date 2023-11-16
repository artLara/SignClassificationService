import sys
sys.path.append('../')
sys.path.append('../../')

from .SignClassification import SignClassification
from .Utils import parseJSONtoHands

class FingerSpellingService():
    def __init__(self, confidence = 0.0):
        self.__signClassification = SignClassification()
        self.__confidence = confidence

    def getPhrase(self, jsonFilePath='', jsonData=None):
        
        if jsonData != None:
            signWords = parseJSONtoHands(data=jsonData)

        elif jsonFilePath != '':
            jsonFile = open(jsonFilePath)
            signWords = parseJSONtoHands(jsonFile)
        else:
            print('Error: jsonFilePath or jsonData parameters have to be valid') 
            return None       
            
        message = ''
        for signWord in signWords:
            word = ''
            for hand in signWord:
                letter, sm_value = self.__signClassification.classify(hand.getLandmarksNormalized())
                if sm_value >= self.__confidence:
                    word += letter
            message += word + ' '

        return message
    
    def getPhrassTest(self, jsonFilePath='', jsonData=None, confidenses=[0.0,0.5,0.6,0.7,0.8]):
        noiseMessages = {}
        for confidence in confidenses:
            noiseMessages[confidence] = ''

        if jsonData != None:
            signWords = parseJSONtoHands(data=jsonData)

        elif jsonFilePath != '':
            jsonFile = open(jsonFilePath)
            signWords = parseJSONtoHands(jsonFile)
        else:
            print('Error: jsonFilePath or jsonData parameters have to be valid') 
            return None       
            
        message = ''
        for signWord in signWords:
            word = ''
            for hand in signWord:
                letter, sm_value = self.__signClassification.classify(hand.getLandmarksNormalized())
                for confidence in confidenses:
                    if sm_value >= confidence:
                        noiseMessages[confidence] += letter

            for confidence in confidenses:
                noiseMessages[confidence] += ' '

        return noiseMessages