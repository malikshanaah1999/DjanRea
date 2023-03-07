from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm
from django.utils.http import is_safe_url
from django.conf import settings
from .serializers import TweetSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

##########################################################################
@api_view(['POST'])
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
##########################################################################
'''
@api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs)
    return Response(serializer.data)


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
##########################################################################