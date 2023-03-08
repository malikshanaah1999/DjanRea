from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm
from django.utils.http import is_safe_url
from django.conf import settings
from .serializers import TweetSerializer, TweetActionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
# Create your views here.

# Using DRF requires the following: 
# 1- converting forms to serializers
# 2- converting Django views to DRF Views...
##########################################################################
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)
''' 
def tweet_create_view(request, *args, **kwargs):
    user = request.user

    if not request.user.is_authenticated:
        user = None
        return redirect(settings.LOGIN_URL)

    form = TweetForm(request.POST or None) 
    next_url = request.POST.get("next") or None
    # request.is_ajax() = T / F.
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user # For Anonymous User
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, allowed_hosts='127.0.0.1'):
            return redirect(next_url)
        form = TweetForm()
    return render (request, 'components/form.html', context={"form":form})
    '''
##########################################################################



@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data, status=200)

'''
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)
'''
##########################################################################
def home_view(request, *args, **kwargs):

    return render(request, "pages/home.html", context={})
##########################################################################
@api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id = tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status=200)

'''
def tweet_detail_view(request, tweet_id, *args, **kwargs): # It's kind of Error Handling
    # *args, **kwargs : Are used for Dynamic URL, ex., <int:tweet_id>
    status = 200
    data = {
        "id": tweet_id,
        #"content": obj.content
        #"image": obj.image.url
    }
    try:
        obj = Tweet.objects.get(id = tweet_id)
        data['content'] = obj.content
  
    except:
        data['message'] = "Not Found"
        status= 404
  
    return JsonResponse(data, status = status)
'''

@api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id = tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user = request.user)
    if not qs.exists():
        return Response({"msg: You cannot delete this tweet"}, status=401)
    obj = qs.first()
    if obj:
        obj.delete()
    return Response({"msg": "Tweet Removed."})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def tweet_action_view(request, tweet_id, *args, **kwargs):
    '''
        id is required
        action includes: like, dislike, retweet
    '''
    serializer = TweetActionSerializer(request.POST)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.__getattribute__("id")
        action = data.__getattribute__("action")
        qs = Tweet.objects.filter(id = tweet_id)
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()
        if obj:
            if request.user in obj.likes.all():
                obj.likes.remove(request.user)
            else:
                obj.likes.add(request.user)
    return Response({"msg": "Tweet Removed."}, status=200)







