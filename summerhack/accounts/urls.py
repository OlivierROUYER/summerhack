from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'summerhack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', views.home, name='home'),
    #url(r'^merkle-tree/', include(admin.site.merkleTree)),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]
