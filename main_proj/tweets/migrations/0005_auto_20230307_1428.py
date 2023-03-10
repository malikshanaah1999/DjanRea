# Generated by Django 3.2.18 on 2023-03-07 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_tweet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='image',
            field=models.FileField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
