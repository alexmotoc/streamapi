from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'overlays', views.TemplateViewSet)
router.register(r'user', views.UserViewSet)
router.register(r'effect', views.EffectViewSet)
# router.register(r'start-stream', views.start_stream)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('start-stream', views.start_stream),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]