from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests
import sys
sys.path.append('../')
sys.path.append('../../')
from classifier.service.src.FingerSpellingService import FingerSpellingService

fingerSpellingService = FingerSpellingService()


class Post_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        data = request.body
        data = json.loads(data)

        # print('------>Data:', data)
        # print('------>Data:', type(data))
        message = fingerSpellingService.getPhrase(jsonData=data)
        print(message)
        response = {
           "message": "OK",
           "error": False,
           "code": 200,
        }
        return Response(response, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        # data = request.POST['data']
        data = request.body
        # dataFile = open(data)
        print(data)
        # data = json.loads(dataFile)
        # message = fingerSpellingService.getPhrase(jsonFile=data)
        # payload = {'message': message}
        # r = requests.get('http://myserver/emoncms2/api/post', data=payload)
        print('------>Data:', type(data))
        
        # return Response(serializer.data)