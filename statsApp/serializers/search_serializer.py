from rest_framework import serializers
from statsApp.models.search import Search


class SearchSerializer(serializers.ModelSerializer):
    """Serializer for Search model
    """
    class Meta:
        model = Search

        fields = ["id",
                  "word",
                  "count",
                  "start_date",
                  "last_date",
                  "last_results",
                  ]
