from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from publication.models import BlogPost, PostTour
from publication.serializers import BlogPostSerializer, PublicationPostSerializer, PostTourSerializer

class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostDetailView(RetrieveAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostFeaturedView(ListAPIView):
    queryset = BlogPost.objects.all().filter(featured=True)
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class BlogPostCategoryView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = BlogPost.objects.order_by('-date_created').filter(category__iexact=category)

        serializer = BlogPostSerializer(queryset, many=True)

        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def post_image(request: Request):
    serializer = PublicationPostSerializer(data=request.data)
    if serializer.is_valid():
        account = serializer.save()
        account.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=400)


class PostTourListView(ListAPIView):
    queryset = PostTour.objects.order_by('-date_created')
    serializer_class = PostTourSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class PostTourDetailView(RetrieveAPIView):
    queryset = PostTour.objects.order_by('-date_created')
    serializer_class = PostTourSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class PostTourFeaturedView(ListAPIView):
    queryset = PostTour.objects.all().filter(featured=True)
    serializer_class = PostTourSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny, )

class PostTourCategoryView(APIView):
    serializer_class = PostTourSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = PostTour.objects.order_by('-date_created').filter(category__iexact=category)

        serializer = PostTourSerializer(queryset, many=True)

        return Response(serializer.data)
