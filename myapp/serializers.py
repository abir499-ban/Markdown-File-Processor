from rest_framework import serializers
from myapp.models import MarkdownFile


class FileSerailizers(serializers.ModelSerializer):
    class Meta:
        model = MarkdownFile
        feilds = '__all__'