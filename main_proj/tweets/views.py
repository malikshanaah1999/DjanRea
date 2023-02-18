from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet
from .forms import TweetForm
from django.utils.http import is_safe_url
# Create your views here.

##########################################################################
def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None) # the TweetForm class can be initialized with data or not.
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url, allowed_hosts='127.0.0.1'):
            return redirect(next_url)
        form = TweetForm()
    return render (request, 'components/form.html', context={"form":form})
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