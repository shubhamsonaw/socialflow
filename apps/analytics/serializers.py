from rest_framework import serializers
from .models import ContentAnalytics


class ContentAnalyticsSerializer(serializers.ModelSerializer):

    engagement_rate = serializers.ReadOnlyField()

    class Meta:
        model = ContentAnalytics
        fields = "__all__"