# Generated by Django 2.2.22 on 2021-05-22 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0009_auto_20210522_1106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendas',
            options={'permissions': (('setar_nfe', 'Usuario pode alterar parametro NFe'), ('remover_nfe', 'Usuario pode alterar para Nfe nao emitida'), ('ver dashboard', 'Pode vizualizar dashboard'))},
        ),
    ]