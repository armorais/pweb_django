# Generated by Django 2.0.13 on 2019-04-04 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctfidelidade', '0004_empresaservico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresaservico',
            name='empresa',
        ),
        migrations.RemoveField(
            model_name='empresaservico',
            name='servico',
        ),
        migrations.DeleteModel(
            name='EmpresaServico',
        ),
    ]
