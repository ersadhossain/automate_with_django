from rest_framework.decorators import api_view
from rest_framework.response import Response
from uploads.models import UploadedFile as Upload
from django.contrib import messages
from .tasks import dataentry_task
from .utils import get_all_models,check_csv_error

@api_view(['POST', 'GET'])
def data_entry_view(request):

    # === POST: handle upload ===
    if request.method == 'POST':
        model_name = request.data.get('model')
        file = request.FILES.get('file')

        if not model_name or not file:
            return Response({"error": "Model name and file are required."}, status=400)

        # Save uploaded file
        x = Upload(model_name=model_name, file=file)
        x.save()  # FIXED — MUST SAVE TO USE .path

        # Use correct full filesystem path
        
        full_path = x.file.path  
        try:
            check_csv_error(full_path, model_name)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

        # Trigger celery task
        dataentry_task.delay(full_path, model_name)

        # Correct message usage
        messages.success(request, 'Your data is being imported; you will be notified once done.')

        return Response({"message": "Your data is being imported; you will be notified once done."})

    # === GET: send list of models ===
    data = get_all_models()
    return Response({'message': "Success", 'data': data})
