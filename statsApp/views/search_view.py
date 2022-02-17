from rest_framework import fields, status, views, generics
from rest_framework.response import Response
from django.utils import timezone

from statsApp.models.search import Search
from statsApp.serializers.search_serializer import SearchSerializer


class SearchPostView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        
        search = Search.objects.filter(word=request.data['word']).first()
        
        # Update stats if word exists
        if search:
            search.update_current(request.data['last_results'])
            serializer = SearchSerializer(search, data=request.data, 
                                          partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"search": serializer.data}, 
            status=status.HTTP_200_OK)

        # Add new word to stats    
        serializer = SearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"search": serializer.data}, 
            status=status.HTTP_201_CREATED)