from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('post<int:id>', views.post, name="post"),
    path('new', views.new, name="new"),
    path('newsletter', views.newsletter, name="newsletter"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)