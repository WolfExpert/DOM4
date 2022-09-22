# Generated by Django 4.1.1 on 2022-09-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_alter_house_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ['name'], 'verbose_name': 'дом', 'verbose_name_plural': 'дома'},
        ),
        migrations.AddField(
            model_name='house',
            name='photo',
            field=models.ImageField(blank=True, default='', upload_to='houses/photos', verbose_name='фотография'),
        ),
    ]
