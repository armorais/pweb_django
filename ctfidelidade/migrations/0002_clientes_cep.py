# Generated by Django 2.0.13 on 2019-04-02 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctfidelidade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='cep',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
