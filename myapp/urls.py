from django.urls import path
from myapp.views import FilesView, MarkdownParser

urlpatterns = [
    path('', FilesView.as_view()),
    path('render/', MarkdownParser.as_view())
]