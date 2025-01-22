from django.db import models
import uuid

# Create your models here.
class MarkdownFile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100, unique=True, null=False)
    content = models.TextField()

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'files'
        ordering = ['-createdAt']

    def __str__(self) -> str:
        return self.name
