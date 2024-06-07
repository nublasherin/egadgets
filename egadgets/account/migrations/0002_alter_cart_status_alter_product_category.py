# Generated by Django 5.0.6 on 2024-05-31 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(default='added', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('smart Phone', 'smart phone'), ('laptop', 'laptop'), ('tablates', 'tablates'), ('smartwatch', 'smartwatch')], max_length=200),
        ),
    ]