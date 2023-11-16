import tensorflow as tf
# from tensorflow.keras import models
import sys
sys.path.append('../')
class SignClassification():
    def __init__(self):
        # self.__model = tf.keras.models.load_model('classifier/service/bin/saved_model/alf_gray')
        self.__model = tf.keras.models.load_model('/home/lara/Desktop/dactilologiaLSM_microservices/SignClassificationService/classifier/service/bin/saved_model/lsm')
        self.__dictOneHot = {0: 'a',
                            1: 'b',
                            2: 'c',
                            3: 'd',
                            4: 'e',
                            5: 'f',
                            6: 'g',
                            7: 'h',
                            8: 'i',
                            9: 'j',
                            10: 'l',
                            11: 'm',
                            12: 'n',
                            13: 'o',
                            14: 'p',
                            15: 'q',
                            16: 'r',
                            17: 's',
                            18: 't',
                            19: 'u',
                            20: 'v',
                            21: 'w',
                            22: 'x',
                            23: 'y',
                            24: 'z',
                            25: 'ñ'}

    def classify(self, pattern):
        res = self.__model.predict(pattern, verbose=0)
        # print(res)
        y_p, index_dict, sm_value = self.getClass(res, self.__dictOneHot)
        return y_p, sm_value

    def getClass(self, x, dictOneHot):
        index, sm_value = self.getClassIndex(x)
        # print(ord(dictOneHot[index]) - ord('A'))
        return dictOneHot[index], index, sm_value

    def getClassIndex(self, x):
        for vector in x:
            maxValue = max(vector)
            output = []
            for index, val in enumerate(vector):
                if maxValue == val:
                    return index, maxValue
