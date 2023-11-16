"""
This file is a test for the service with previous data loaded.
"""
import os
import sys
sys.path.append('../')
sys.path.append('../../')
sys.path.append('../../../')

from src.FingerSpellingService import FingerSpellingService
class TestService():
    def __init__(self):
        self.__fingerSpellingService = FingerSpellingService()
    
    def runTest(self):
        dir_path = 'phrasesJSON/'
        jsonFiles = []
        # Iterate directory
        for file_path in os.listdir(dir_path):
            # check if current file_path is a file
            if os.path.isfile(os.path.join(dir_path, file_path)):
                # add filename to list
                jsonFiles.append(file_path)
                noiseWord = self.__fingerSpellingService.getPhrase(dir_path+file_path)
                print(noiseWord)
        # print(jsonFiles)

t = TestService()
t.runTest()