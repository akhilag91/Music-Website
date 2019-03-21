"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from music import views
from accounts import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home',views.home,name='home'),
    url(r'^album_detail/(\d+)/',views.album_detail,name='album_detail'),
    url(r'^signup',account_views.signup,name='signup'),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    url(r'^profile',views.profile,name='profile'),
    url(r'^uploads',views.song_upload_form,name='song_upload_form'),
    url(r'^playlist',views.crud_playlist,name='crud_playlist'),
    url(r'^saveplaylist',views.save_playlist,name='save_playlist'),
    url(r'^viewplaylist/(\d+)',views.view_playlist,name='view_playlist'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
