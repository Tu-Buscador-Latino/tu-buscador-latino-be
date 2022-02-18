from rest_framework import status, views, generics
from rest_framework.response import Response

from statsApp.models.search import Search
from statsApp.serializers.search_serializer import SearchSerializer


class SearchPostView(views.APIView):
    """Represents the API to receive the searched words from
    the frontend 
    """
    
    def post(self, request, *args, **kwargs):
        word = request.data['word'].lower()
        search = Search.objects.filter(word=word).first()
        
        # Update stats if word exists
        if search:
            search.update_current(request.data['last_results'])
            serializer = SearchSerializer(search, data={},partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"search": serializer.data}, 
            status=status.HTTP_200_OK)

        # Add new word to stats
        data = {
            "word": word,
            "last_results": request.data['last_results']
        }    
        serializer = SearchSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"search": serializer.data}, 
            status=status.HTTP_201_CREATED)


class SearchStats(generics.ListAPIView):
    """Represents the API to consult the statistics about the most
    searched words
    """
    serializer_class = SearchSerializer
    
    def get(self, request, *args, **kwargs):
        max_results = int(request.query_params['max'])
        searchs = Search.objects.all().order_by('-count')[:max_results]
        serializer_tickets = SearchSerializer(searchs, many=True)
        return Response(serializer_tickets.data, 
            status=status.HTTP_200_OK)