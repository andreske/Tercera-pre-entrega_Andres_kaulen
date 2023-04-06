# Generated by Django 4.1.7 on 2023-04-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0002_direccion_delete_direcciones_remove_home_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('lugar', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=1000)),
                ('imagen', models.ImageField(upload_to='Lugares/imagenes/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Direccion',
        ),
        migrations.DeleteModel(
            name='Solicitud',
        ),
    ]
