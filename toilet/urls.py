from django.urls import path, include
from django.contrib import admin
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'toilet'

router = DefaultRouter()
router.register(r'list', views.ToiletViewSet)

urlpatterns = [
    path('',views.home,name='home'),
    path('add/',views.add, name='add'),
    path('about/',views.about, name='about'),
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
]
