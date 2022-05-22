import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'labVSRPP.settings')

import django

django.setup()
from django.contrib.auth.models import Group
GROUPS = ['admin', 'student']
MODELS = ['lab3_5']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)
