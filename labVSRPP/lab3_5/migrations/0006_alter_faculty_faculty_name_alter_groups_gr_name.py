# Generated by Django 4.0.4 on 2022-05-21 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab3_5', '0005_alter_groups_group_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='faculty_name',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='groups',
            name='gr_name',
            field=models.CharField(blank=True, max_length=45, null=True, unique=True),
        ),
    ]
