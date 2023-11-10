from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests

from classifier.service.src.FingerSpellingService import FingerSpellingService

fingerSpellingService = FingerSpellingService()


class Post_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        data = json.loads(request.body)
        # message = fingerSpellingService.getPhrase(jsonFile=data)
        # payload = {'message': message}
        # r = requests.get('http://myserver/emoncms2/api/post', data=payload)
        print(data)

    def post(self, request, format=None):
        tmp = request.data.get('width')
        print(tmp)
        
        # return Response(serializer.data)