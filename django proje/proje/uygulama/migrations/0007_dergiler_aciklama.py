# Generated by Django 4.0.4 on 2022-05-29 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uygulama', '0006_alter_kullanıcımesaj_dosya'),
    ]

    operations = [
        migrations.AddField(
            model_name='dergiler',
            name='aciklama',
            field=models.ImageField(default='', null='false', upload_to='icerik'),
            preserve_default='false',
        ),
    ]
