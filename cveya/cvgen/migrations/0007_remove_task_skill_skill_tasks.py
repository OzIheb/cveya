# Generated by Django 4.2.1 on 2023-05-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvgen', '0006_alter_educationhistory_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='skill',
        ),
        migrations.AddField(
            model_name='skill',
            name='tasks',
            field=models.ManyToManyField(to='cvgen.task'),
        ),
    ]
