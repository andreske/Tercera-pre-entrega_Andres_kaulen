# Generated by Django 4.1.7 on 2023-04-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLugares', '0003_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='post_id',
            field=models.IntegerField(default=444),
            preserve_default=False,
        ),
    ]