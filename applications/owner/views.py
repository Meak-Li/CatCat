from django.shortcuts import render
from rest_framework.views import APIView

from applications.owner.serializers import OwnerSerializer


# Create your views here.
class OwnerView(APIView):

    def get(self, request, *args, **kwargs):
        data = request.DATA
        owner_ser = OwnerSerializer(data)
        owner_ser.is_valid()
        print(owner_ser.data)
