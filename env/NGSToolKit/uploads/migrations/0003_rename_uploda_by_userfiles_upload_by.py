# Generated by Django 4.0.3 on 2022-03-25 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_userfiles_delete_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfiles',
            old_name='uploda_by',
            new_name='upload_by',
        ),
    ]