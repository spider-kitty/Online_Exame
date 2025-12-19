import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<ONLINE_EXAME-MAIN>.settings")  # مثلا config.settings یا Online_Exame.settings
django.setup()

from django.apps import apps
for app in apps.get_app_configs():
    print(app.label)
    for m in app.get_models():
        print("  -", m.__name__)
