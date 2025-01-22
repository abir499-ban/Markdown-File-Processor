from django.shortcuts import render
from rest_framework import status, generics
from rest_framework import response
from myapp.serializers import FileSerailizers
from myapp.models import MarkdownFile


# Create your views here.
class FilesView(generics.GenericAPIView):
    serializer_class = FileSerailizers
    queryset = MarkdownFile.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(
                {
                    "message": "Markdown file content saveds uccesfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        
    def get(self, request):
        try:
            serializer = self.serializer_class(self.queryset, many=True)
            return response.Response({"message" : "Fetched all Md files ", "data" : serializer.data},
                                     status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response({"message" : "Failed to fetch Md files", "error" : str(e)})


