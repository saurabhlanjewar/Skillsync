# Generated by Django 5.1.4 on 2024-12-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=30)),
                ('task_description', models.CharField(max_length=225)),
                ('skill_used', models.JSONField(blank=True, default=list)),
                ('deadline', models.IntegerField(default=1)),
                ('available_all', models.BooleanField(default=False)),
                ('assigned_user', models.ManyToManyField(blank=True, null=True, related_name='todo', to='Group.group')),
                ('group_name', models.ManyToManyField(blank=True, null=True, related_name='tasks_list', to='Group.group')),
            ],
        ),
    ]
