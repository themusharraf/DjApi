from rest_framework import viewsets
from rest_framework.response import Response
from api.models import Product
from api.serializers import PostSerializer


class PostListView(viewsets.ViewSet):

    def list(self, request):
        queryset = Product.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)


user_list = PostListView.as_view({'get': 'list'})
