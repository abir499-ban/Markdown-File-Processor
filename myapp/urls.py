from django.urls import path, re_path
from myapp.views import FilesView, MarkdownParser

urlpatterns = [
    path('', FilesView.as_view() , name="general-file-operation"),
    re_path(r'^(?P<id>[0-9a-f-]+)/$', FilesView.as_view(), name="get_a_file"),
    path('render/', MarkdownParser.as_view() , name="render_file")
]