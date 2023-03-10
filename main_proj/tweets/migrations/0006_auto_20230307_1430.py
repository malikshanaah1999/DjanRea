# Generated by Django 3.2.18 on 2023-03-07 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20230307_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
