# Generated by Django 4.0.4 on 2022-05-21 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_5', '0006_alter_faculty_faculty_name_alter_groups_gr_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
