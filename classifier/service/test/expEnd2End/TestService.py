"""
This file is a test for the service with previous data loaded.
"""
import os
import sys
import pandas as pd
sys.path.append('../')
sys.path.append('../../')
sys.path.append('../../../')

from src.FingerSpellingService import FingerSpellingService
class TestService():
    def __init__(self):
        self.__fingerSpellingService = FingerSpellingService()
    
    def runTest(self):
        df = pd.read_csv('/home/lara/Desktop/dactilologiaLSM_microservices/SignClassificationService/classifier/service/test/expEnd2End/end2end.csv')
        confidenses=[0.0,0.5,0.6,0.7,0.8]
        messagesDict = {}
        for confidence in confidenses:
            messagesDict[confidence] = []

        for ind in df.index:
            jsonfile = df['jsonfile'][ind]
            print('Procesando:',jsonfile)
            

            noiseMessages = self.__fingerSpellingService.getPhrassTest(jsonFilePath='json_messages/'+jsonfile, confidenses=confidenses)
            for confidence in confidenses:
                # print('Confidence ', confidence)
                # print(noiseMessages[confidence])
                messagesDict[confidence].append(noiseMessages[confidence])

            #break

        for confidence in confidenses:
            df_aux = pd.DataFrame(messagesDict[confidence])
            # df.insert(2, "noiseMessage", messagesDict[confidence]).to_csv('confidence{}'.format(confidence),index=False)
            pd.concat([df,df_aux], ignore_index=True, axis=1).rename(columns={0: "target", 1: "jsonfile", 2:"noiseMessage"}).to_csv('confidence{}.csv'.format(confidence),index=False)
            # print(noiseWord)
        # print(jsonFiles)

t = TestService()
t.runTest()