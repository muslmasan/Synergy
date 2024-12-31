from rest_framework.routers import DefaultRouter
from .views import PostView, CommentView, CommunityView
from django.urls import path, include


router = DefaultRouter()
router.register(r'', CommunityView)
router.register(r'comment', CommentView)
router.register(r'post', PostView)
app_name = 'community'


urlpatterns = [
    path('',include(router.urls)),
]
