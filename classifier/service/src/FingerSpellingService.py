import sys
sys.path.append('../')
sys.path.append('../../')

from .SignClassification import SignClassification
from .Utils import parseJSONtoHands

class FingerSpellingService():
    def __init__(self, confidence = 0.5):
        self.__signClassification = SignClassification()
        self.__confidence = confidence

    def getPhrase(self, jsonFilePath='', jsonFile=None):
        if jsonFilePath != '':
            jsonFile = open(jsonFilePath)
        
        if jsonFile == None:
            print('None file')
            return ''
        
        signWords = parseJSONtoHands(jsonFile)
        message = ''
        for signWord in signWords:
            word = ''
            for hand in signWord:
                letter, sm_value = self.__signClassification.classify(hand.getLandmarksNormalized())
                if sm_value >= self.__confidence:
                    word += letter
            message += word + ' '

        return message