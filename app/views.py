from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from app.models import Photo
from app.serializers import PhotoSerializer

# Create your views here.


class PhotoListCreateView(ListCreateAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()


class PhotoUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()
    lookup_field = "id"
