from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
        url(r'^$',include('polls.urls',namespace='polls')),
        url(r'^polls/',include('polls.urls', namespace='polls')),
        url(r'^FH/',include('FH.urls',namespace='fh')),
        url(r'^favicon.ico$',RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'),
            permanent=False),name='favicon'),
        url(r'^admin/',include(admin.site.urls)),
        ]
