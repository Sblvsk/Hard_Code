# Generated by Django 4.1.7 on 2023-02-15 12:22

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_remove_product_deleted_alter_product_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=models.ImageField(upload_to=mainapp.models.products_avatars_path),
        ),
    ]
