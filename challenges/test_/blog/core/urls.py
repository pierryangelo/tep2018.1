from django.conf.urls import url, include

from rest_framework_nested import routers

from .views import UserViewSet, PostViewSet, CommentViewSet, AddressViewSet

router = routers.SimpleRouter()

router.register(r'users', UserViewSet, base_name='users')
router.register(r'quick', UserViewSet, base_name='quick')

users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'posts', PostViewSet, base_name='posts')

addresses_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
addresses_router.register(r'addresses', AddressViewSet, base_name='addresses')

posts_router = routers.NestedSimpleRouter(users_router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, base_name='comments')

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'', include(users_router.urls)),
    url(r'', include(posts_router.urls)),
    url(r'', include(addresses_router.urls)),
]