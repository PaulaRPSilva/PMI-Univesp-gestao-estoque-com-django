# Generated by Django 3.2.8 on 2021-10-29 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_estoque', '0003_auto_20211029_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='situacao_material',
            name='localizacao',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
