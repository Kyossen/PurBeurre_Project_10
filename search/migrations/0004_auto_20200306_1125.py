# Generated by Django 2.2.4 on 2020-03-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20200306_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='nutrition_grade',
            field=models.TextField(default=''),
        ),
    ]
