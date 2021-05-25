# Generated by Django 2.2.22 on 2021-05-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0005_auto_20210521_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdopedido',
            name='desconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='desconto',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='impostos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='vendas',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
