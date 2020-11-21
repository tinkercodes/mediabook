from django.urls import path

from . import views
app_name='home'
urlpatterns = [
	path('', views.MediaList.as_view()),
    path('home/', views.MediaList.as_view()),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'), 
    # path('handle_signup/', views.handle_signup, name='handlSignup'),   
    # path('handle_login/', views.handle_login, name='handleLogin'),
    path('logout/',views.logout),
    path('createPost/', views.MediaCreate,name='MediaCreate'),
    # path('submit/', views.handle_mediacreate,name='handle_mediacreate'),
    path('your_media/', views.your_media.as_view(),name='your_media'),
]
