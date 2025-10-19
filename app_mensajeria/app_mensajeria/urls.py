"""
URL configuration for app_mensajeria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from messenger.urls import messenger_patterns
from notices.urls import notices_patterns
from profiles.urls import profiles_patterns
from registration.urls import registration_patterns
from userCalendar.urls import userCalendar_patterns

urlpatterns = [
    path('', include('core.urls')),
    path('messenger/', include(messenger_patterns)),
    path('notices/', include(notices_patterns)),
    path('admin/', admin.site.urls),
    # profiles paths
    path('profiles/', include(profiles_patterns)),
    # path authentication - registration app
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include(registration_patterns)),
    path('calendar/', include(userCalendar_patterns)),
]

if settings.DEBUG == True:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
