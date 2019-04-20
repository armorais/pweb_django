# Generated by Django 2.0.13 on 2019-04-03 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=15)),
                ('nome', models.CharField(max_length=200)),
                ('cep', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'clientes',
            },
        ),
    ]