
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [

    # admin-page
    url('admin/', admin.site.urls),

    # for sign-up
    url(r'', include('accounts.urls', namespace = 'accounts')),

    # for blogs
    url(r'blogs/', include('blog.urls', namespace = 'blog')),

]
