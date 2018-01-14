"""pingpong URL Configuration

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
# django imports
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.db.models.signals import post_save
from django.dispatch import receiver

#rest_framework imports
from rest_framework.authtoken.models import Token
from rest_framework.authtoken import views as rest_views
from rest_framework import routers

# views imports
from referee import views


# routers
router = routers.DefaultRouter()
router.register('game', views.GameViewSet)
router.register('player', views.PlayerViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'get/auth/token/', rest_views.obtain_auth_token, name="get_auth_token"),
    url(r'^', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





# signals

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user = instance)
