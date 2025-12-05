from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import get_all_models
from uploads.models import UploadedFile as Upload
from django.conf import settings
from django.core.management import call_command
from django.contrib import messages







@api_view(['POST','GET'])
def data_entry_view(request):
    if request.method == 'POST':
        model_name = request.data.get('model')
        file = request.FILES.get('file')

        if not model_name or not file:
            return Response({"error": "Model name and file are required."}, status=400)

        x = Upload(model_name=model_name, file=file)
        # x.save()  # MUST SAVE BEFORE ACCESSING .path
        relative_path = str(x.file.url)
        base_url = str(settings.BASE_DIR)

        full_path = base_url+relative_path
       


        # full_path = x.file.path  # This is already correct filesystem path

        try:
            call_command('dataentry', full_path, model_name)
            messages.success(request, "File processed successfully.")
        except Exception as e:
            messages.error(request, f"Error processing file: {str(e)}")

        return Response({"message": "File processed successfully."})

    data = get_all_models()
    return Response({'message': "Hello, world!", 'data': data})

