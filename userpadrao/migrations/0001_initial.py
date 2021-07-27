import os
from decouple import config
from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    def generate_superuser(apps, schema_editor):
        from django.contrib.auth.models import User

        DJANGO_NAME = config('NOMEUSER')
        DJANGO_EMAIL = config('EMAILUSER')
        DJANGO_PASSWORD = config('PWDUSER')
        
        superuser = User.objects.create_superuser(
            username=DJANGO_NAME,
            email=DJANGO_EMAIL,
            password=DJANGO_PASSWORD)
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]