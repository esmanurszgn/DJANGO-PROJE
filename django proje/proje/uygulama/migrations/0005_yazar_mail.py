# Generated by Django 4.0.4 on 2022-05-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uygulama', '0004_rename_soyadı_yazar_unvan_alter_yazar_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='yazar',
            name='mail',
            field=models.CharField(default='', max_length=80),
        ),
    ]