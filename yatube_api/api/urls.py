from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

app_name = 'api'
API_VERSION_1 = 'v1/'

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comment')
router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path(API_VERSION_1, include('djoser.urls')),
    path(API_VERSION_1, include('djoser.urls.jwt')),
    path(API_VERSION_1, include(router.urls)),
]
