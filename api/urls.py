from api.views import PostListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'product', PostListView, basename='product')

urlpatterns = router.urls
