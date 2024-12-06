from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('articles/<slug:slug>/', ArticleDetailsView.as_view(), name="article-details")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
