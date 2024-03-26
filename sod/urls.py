"""
URL configuration for sod project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home' ),
    path('events', views.events, name = 'events' ),
    path('about', views.about, name = 'about' ),
    path('contact', views.contact, name = 'contact'),
    path('animation', views.animation, name = 'animation'),
    path('greenscreen', views.greenscreen, name = 'greenscreen'),    
    path('animation_masterclass', views.animation_masterclass, name = 'animation_masterclass'),
    path('communication', views.communication, name = 'communication'),
    path('poster', views.poster, name = 'poster'),
    path('calligraphy', views.calligraphy, name = 'calligraphy'),
    path('fashiondesign', views.fashion, name = 'fashiondesign'),
    path('repurpose', views.repurpose, name = 'repurpose'),
    path('sunkissed', views.sunkissed, name = 'sunkissed'),
    path('interior', views.interior, name = 'interior'),
    path('innofur', views.innofur, name = 'innofur'),
    path('masterclass_iiid', views.masterclass_iiid, name = 'masterclass_iiid'),
    path('multisensory', views.multisensory, name = 'multisensory'),
    path('illuminating', views.illuminating, name = 'illuminating'),
    path('studentexhibition', views.studentexhibition, name = 'studentexhibition'),
    path('productdesign', views.product, name = 'productdesign'),
      path('parking', views.parking_shed, name = 'parking'),
      path('laser', views.laser_cutting, name = 'laser'),
    path('conceptual_packaging', views.conceptual_packagaing, name = 'conceptual_packaging'),
    path('gift_wrapping', views.gift_wrapping, name = 'gift_wrapping'),
    path('bamboo', views.bamboo, name = 'bamboo'),
    path('handicraft', views.handicraft, name = 'handicraft'),
    path('claycreation', views.claycreation, name = 'claycreation'),
    path('birdnest', views.birdnest, name = 'birdnest'),
    path('coaster', views.coaster, name = 'coaster'),    
    path('tieanddye', views.tieanddye, name = 'tieanddye'),
        path('designworkshop', views.designworkshop, name = 'designworkshop'),
    
    
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
