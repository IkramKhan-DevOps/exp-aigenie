import os
import openai
from rest_framework import status, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, \
    RetrieveAPIView, ListAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from src.api.serializer import PurchaseSerializer, PackageSerializer, PurchaseCreateSerializer
from src.administration.admins.models import Package, Purchase


class OpenAIChatAPi(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        text = request.data.get('text')
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

        return Response({'result': result}, status=status.HTTP_200_OK)


class PurchaseListAPIView(ListAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Purchase.objects.filter(user=self.request.user)


class PurchaseCreateAPIView(CreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        package = serializer.validated_data['package']
        serializer.save(
            user=self.request.user, amount_total=package.price,
            amount_paid=package.price, tokens=package.tokens
        )


class PurchaseRetrieveAPIView(RetrieveAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Purchase.objects.filter(user=self.request.user), pk=self.kwargs['pk'])


class PackageListAPIView(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [permissions.IsAuthenticated]

