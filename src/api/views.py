import os
from builtins import type

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_auth.registration.views import SocialLoginView
import openai
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from src.api.serializer import OpenAISerializer


class FaceBookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class OpenAIChatAPi(APIView):

    def post(self, request):
        text = request.data.get('text')
        print(text)
        openai.api_key = os.environ.get('OPEN_AI_API_KEY')
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )
        result = response['choices'][0]['text']
        
        return Response({'result': result},status=status.HTTP_200_OK)


