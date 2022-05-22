import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')

import django

django.setup()
from django.contrib.auth.models import Group

GROUPS = ['guest', 'manager', 'admin']
MODELS = ['ISotL']

for group in GROUPS:
    new_group, created = Group.objects.get_or_create(name=group)
