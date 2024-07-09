from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import News
from .data_crawler import NBANewsCrawler
from .serializer import NewsSerializer


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all().order_by('-news_time')
    serializer_class = NewsSerializer

    @action(detail=False, methods=['GET'])
    def crawler(self, request):
        try:
            NBANewsCrawler().catch_different_news(number=request.query_params.get('number', 0))
        except Exception as e:
            print(e)
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
        return Response('Successful crawler', status=status.HTTP_200_OK)
