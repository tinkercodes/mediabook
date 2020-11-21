from django.shortcuts import render
from django.urls import reverse 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as Login,logout as Logout
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from home.models import media
from django.utils import timezone
# Create your views here.

def login(request):
	context={
	"error_username":"",
	"error_password":""
	}
	if(request.method=="POST"):
	    username = request.POST['username']
	    password = request.POST['password']
	    user = authenticate(request, username=username, password=password)
	    if user is not None:
	        Login(request,user)
	        # Redirect to a success page.
	        # HttpResponseRedirect(url('home:index'))
	        return HttpResponseRedirect('/home/')
	    else:
	        # Return an 'invalid login' error message.
	        return HttpResponseRedirect('/login/')
	else:
		return render(request, 'home/login.html',context)

	

def signup(request):
	context={
	"error_username":"",
	"error_pass1":"",
	"error_pass1":""
	}
	if(request.method=="POST"):
		username=request.POST['username']
		password=request.POST['password']
		email=request.POST['email']
		user = User.objects.create_user(username, email, password)
		user.save()
		return HttpResponseRedirect('/home/')

	return render(request, 'home/signup.html',context)

class MediaList(ListView):
    model = media
    # by default -> template_name=media_list.html
    # for filter queryset -> queryset = Book.objects.filter(publisher__name='ACME Publishing')
    queryset = media.objects.order_by('-date_uploaded')
    extra_context={
    "title":"prabhat_home",
    "name":"prabhat"
    }

def MediaCreate(request):
    ctx={

    }
    audio=[]
    video=["mp4","mp3"]
    img=["jpeg","png","jpg"]

    if(request.method=="POST"):
    	title=request.POST['title']
    	description=request.POST['description']
    	data=request.FILES['data']
    	media_type=data.content_type.split('/')[0]
    	
    	date_uploaded=timezone.now()
    	Media=media.objects.create(title=title,description=description,date_uploaded=date_uploaded,data=data,author=request.user,media_type=media_type)
    	Media.save()
    	return HttpResponseRedirect('/home/')
    return render(request,'home/media_form.html',ctx)

def logout(request):
 	Logout(request)
 	return HttpResponseRedirect('/home/')

class your_media(ListView):
    model = media
    template_name='home/your_media.html'
    # by default -> template_name=media_list.html
    # for filter queryset -> queryset = Book.objects.filter(publisher__name='ACME Publishing')
    context_object_name="my_view_list"
    
    
    def get_queryset(self):
        return media.objects.filter(author=self.request.user).order_by('-date_uploaded')
    
    

