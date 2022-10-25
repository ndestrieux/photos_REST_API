from rest_framework import serializers

from app.models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "id",
            "title",
            "album_id",
            "width",
            "height",
            "dominant_color",
            "local_url",
        ]
        read_only_fields = [
            "width",
            "height",
            "dominant_color",
        ]
