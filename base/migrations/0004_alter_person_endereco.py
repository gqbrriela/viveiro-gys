# Generated by Django 4.0.5 on 2022-11-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_endereço_person_endereco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='endereco',
            field=models.CharField(blank=True, max_length=35),
        ),
    ]
