from django.db import models
import uuid

# Create your models here.
class MarkdownFile(models.Model):
    id : models.UUIDField(primary_key==True, editable=False, default=uuid.uuid4)
    name : models.CharField(max_length=100, unique=True)
    content : models.TextField()

    createdAt : models.TimeField(auto_now_add=True)
    updatedAt : models.TimeField(auto_now_add=True)