from rest_framework import serializers
from myapp.models import MarkdownFile


class FileSerializers(serializers.ModelSerializer):  # Ensure class name is corrected
    class Meta:
        model = MarkdownFile
        fields = '__all__'  # Fixed typo here
