# Generated by Django 4.1.7 on 2023-07-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_detalleaccesos_detalleacceso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mqtt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('valor', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(auto_now=True, null=True, verbose_name='fecha...')),
            ],
        ),
    ]
