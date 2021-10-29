from rest_framework import generics

from .models import Article, Type
from .serializers import ArticleSerializer, TypeSerializer, ArticleCreateSerializer


class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleListByTypeView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        try:
            type_of = Type.objects.get(pk=self.kwargs['pk'])
            return Article.objects.filter(type=type_of)
        except:
            return None


class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer


class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TypeListView(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
