# Generated by Django 4.2.1 on 2023-05-07 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvgen', '0002_qualifcation_profile_address_profile_email_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Qualifcation',
            new_name='Qualification',
        ),
    ]