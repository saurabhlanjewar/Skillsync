# Generated by Django 5.1.4 on 2024-12-10 16:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Group', '0001_initial'),
        ('Task', '0002_alter_task_assigned_user_alter_task_group_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_user',
            field=models.ManyToManyField(blank=True, null=True, related_name='todo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='group_name',
            field=models.ManyToManyField(blank=True, null=True, related_name='tasks_list', to='Group.group'),
        ),
    ]