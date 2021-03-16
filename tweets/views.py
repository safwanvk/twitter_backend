from django.shortcuts import render
from rest_framework.response import Response
from .serializer import TweetSerializer
from rest_framework.decorators import api_view
from .models import Tweet

# Create your views here.
@api_view(['POST']) # http method the client == POST
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data, status=200)

