# Generated by Django 2.1.7 on 2019-03-02 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20190301_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(default='default-image.png', upload_to='categories_photos'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='photo',
            field=models.ImageField(default='default-image.png', upload_to='collections_photos'),
        ),
    ]
