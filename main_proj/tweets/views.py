from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
# Create your views here.

##########################################################################
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id":x.id, "content":x.content} for x in qs] # Comprehensive List
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

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