from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (get_token, sign_up,
                    UsersViewSet, CategoryViewSet,
                    GenreViewSet, TitleViewSet,
                    CommentViewSet, ReviewViewSet)

app_name = 'api'

router = SimpleRouter()
router.register(r'users', UsersViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', sign_up, name='signup'),
]
