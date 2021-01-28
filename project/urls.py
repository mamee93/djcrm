from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from leads.views import LandingPage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(),name="landing-page"),
    path('leads/', include('leads.urls', namespace='leads')),
]
urlpatterns  += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

