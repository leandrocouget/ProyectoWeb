# Generated by Django 4.0.4 on 2022-04-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProyectoWebApp', '0002_rename_formulario_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.CharField(max_length=30)),
                ('cantidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('comentario', models.TextField()),
            ],
        ),
    ]
