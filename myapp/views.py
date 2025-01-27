from django.shortcuts import render
from rest_framework import status, generics
from rest_framework import response
from myapp.serializers import FileSerializers
from myapp.models import MarkdownFile
import markdown
from datetime import datetime
from myapp.dbConfig import create_connection


# Create your views here.
class FilesView(generics.GenericAPIView):
    serializer_class = FileSerializers
    queryset = MarkdownFile.objects.all()

    def post(self, request):
        original_name = request.data.get('name')
        modified_name = original_name + "".join(str(datetime.now()).split(' '))
        file_creation_DTO = {
            "name" : modified_name,
            "content" : request.data.get("content")
        }
        
        try:

            serializer = self.serializer_class(data=file_creation_DTO)
            if serializer.is_valid():
                serializer.save()
                return response.Response(
                    {
                        "message": "Markdown file content saved succesfully",
                        "data": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )
        except Exception as e:
            print(e)
        
    def get(self, request):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            
           
            cursor.execute("SELECT id, name, content FROM files")
            rows = cursor.fetchall()  

            

            conn.close()  

            return response.Response(
                {"message": "Fetched all files using raw SQL and sqlite3", "data": rows},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return response.Response(
                {"message": "Failed to fetch files", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

##todo:add the routes for HTML rendering and Grammar checking


class MarkdownParser(generics.GenericAPIView):
    serializer_class = FileSerializers

    def post(self, request):
        try:
            html_content = markdown.markdown(request.data.get("content", ""))
            if not html_content:
                return response.Response({"message" : "No content found"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return response.Response({"message" : "Markdown file", "data" : html_content}, status=status.HTTP_200_OK)
        except Exception as e:
            return response.Response({"message":f"Error {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

