# Generated by Django 2.2.22 on 2021-05-21 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20210521_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendas',
            name='pessoa',
        ),
        migrations.DeleteModel(
            name='ItemDoPedido',
        ),
        migrations.DeleteModel(
            name='Vendas',
        ),
    ]
