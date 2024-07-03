from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')

v1_patterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
]

urlpatterns = [
    path('v1/', include(v1_patterns)),
]
