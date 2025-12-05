from django.apps import apps

def get_all_models():
    all_models = []
    default = ['LogEntry', 'Permission', 'Group', 'User', 'ContentType', 'Session','UploadedFile']

    # models = apps.get_models()
    # print(models.__name__)

    for model in apps.get_models():
        if model.__name__ not in default:
            all_models.append(model.__name__)
    return all_models
