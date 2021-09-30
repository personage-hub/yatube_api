from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

URL_VERSION_1 = 'v1/'
URL_POSTS = r'posts'
URL_GROUP = r'groups'
URL_COMMENTS = r'posts/(?P<post_id>\d+)/comments'
URL_FOLLOW = r'follow'

router_v1 = DefaultRouter()
router_v1.register(
    URL_VERSION_1 + URL_COMMENTS,
    CommentViewSet,
    basename='comments'
)
router_v1.register(
    URL_VERSION_1 + URL_POSTS,
    PostViewSet,
    basename='posts'
)
router_v1.register(
    URL_VERSION_1 + URL_GROUP,
    GroupViewSet,
    basename='groups'
)
router_v1.register(
    URL_VERSION_1 + URL_FOLLOW,
    FollowViewSet,
    basename='follow'
)


urlpatterns = [
    path(URL_VERSION_1, include('djoser.urls.jwt')),
    path('', include(router_v1.urls))
]
