# Generated by Django 4.0.4 on 2022-05-29 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uygulama', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yazar',
            name='soyadı',
            field=models.CharField(default='', max_length=50),
        ),
    ]
