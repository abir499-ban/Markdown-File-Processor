from django.urls import path, re_path
from myapp.views import FilesView, MarkdownParser,FileswithParams

urlpatterns = [
    path('', FilesView.as_view() , name="general-file-operation"),
    path('<str:id>/', FileswithParams.as_view()),
    path('render/', MarkdownParser.as_view() , name="render_file")
]