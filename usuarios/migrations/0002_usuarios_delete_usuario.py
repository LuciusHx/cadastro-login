# Generated by Django 5.0.6 on 2024-05-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
