# Generated by Django 2.2.4 on 2019-10-19 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20191019_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='search.Categories'),
        ),
    ]
