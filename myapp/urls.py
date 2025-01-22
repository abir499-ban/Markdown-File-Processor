from django.urls import path
from myapp.views import FilesView

urlpatterns = [
    path('', FilesView.as_view())
]