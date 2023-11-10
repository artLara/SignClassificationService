from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests
class Post_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        data = json.loads(request.body)
        print(data)

    def post(self, request, format=None):
        tmp = request.data.get('width')
        print(tmp)
        
        # return Response(serializer.data)