from django.shortcuts import render
from rest_framework import status, generics
from rest_framework import response
from myapp.serializers import FileSerializers
from myapp.models import MarkdownFile
import markdown
from datetime import datetime
from myapp.dbConfig import create_connection
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings 


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
                cursor.execute("SELECT id, name, content,createdAt FROM files")
                rows = cursor.fetchall()            
                conn.close() 

                FileUploadObj = FileUpload()
                fileUploaded = FileUploadObj.get()["data"]
                rows.extend(fileUploaded)
               

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

class FileswithParams(generics.GenericAPIView):
    serializer_class = FileSerializers
    def get(self, request, id=None):
        try:
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM files WHERE id=?" , (id,))
            rows = cursor.fetchall()
            conn.close()

            return response.Response(
                {'data' : rows}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return response.Response(
                    {"message": "Failed to fetch files", "error": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )



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


class FileUpload(generics.GenericAPIView):
    directory = os.path.join(settings.BASE_DIR , 'uploads')
    os.makedirs(directory, exist_ok=True)

    def post(self, request):
        if 'file' not in request.FILES:
            return response.Response({"message" : "no file provided"},status=status.HTTP_400_BAD_REQUEST)
        
        uploaded_file = request.FILES['file']
        file_name  = uploaded_file.name
        pos = "".join(reversed(file_name)).find('.')
        file_name  = file_name[:len(file_name) - pos - 1]
        uniques_filname = file_name + "_" + datetime.now().strftime("%Y%m%d_%H%M%S")  + ".md"

        file_path = os.path.join(self.directory, uniques_filname)
        default_storage.save(file_path, ContentFile(uploaded_file.read()))

        return response.Response({"message" : "File Upload Successfully!", "filename" : uniques_filname})

    def get(self, request=None, fileName=None):
        if fileName == None:
            try:
                files = os.listdir(self.directory)
                file_info = []
                for file in files:
                    file_info.append([file, 'localfile'])
                return {"data" : file_info}
            except Exception as e:
                return response.Response({"error" : e})
        else:
            filePath = os.path.join(self.directory , fileName)
            try:
                content = 'Not Found'
                if os.path.exists(filePath):
                    with open(filePath, 'r') as file:
                        content = file.read()
                    return response.Response({"message" : "File from local device fetched successfully", "data" : content}, status=status.HTTP_200_OK)
            
            except Exception as e:
                return response.Response({"error" : e})

