# Generated by Django 4.0.3 on 2022-03-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_delete_userdata_0'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='adminupload',
            field=models.FileField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='userdata',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
