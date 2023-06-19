# Generated by Django 4.1.7 on 2023-06-17 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('a', 'a'), ('b', 'b')], default='a', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dispositivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ip', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('fecha_nacimiento', models.DateTimeField(blank=True, null=True, verbose_name='fecha...')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='acceso',
            name='nombreAula',
        ),
        migrations.RemoveField(
            model_name='acceso',
            name='nombreProfesor',
        ),
        migrations.RemoveField(
            model_name='acceso',
            name='password',
        ),
        migrations.RemoveField(
            model_name='acceso',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='acceso',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True, verbose_name='fecha...'),
        ),
        migrations.AddField(
            model_name='acceso',
            name='tipo_acceso',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='DetalleAccesos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateTimeField(auto_now=True, verbose_name='fecha..DA.')),
                ('timestamps', models.DateTimeField(blank=True, null=True, verbose_name='fecha...')),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.aula')),
                ('dispositivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dispositivo')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True, verbose_name='fechaInicio')),
                ('fecha_fin', models.DateTimeField(blank=True, null=True, verbose_name='fechaFin')),
                ('dias_laborales', models.IntegerField()),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.rol')),
            ],
        ),
        migrations.AddField(
            model_name='aula',
            name='tipo_aula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tipoaula'),
        ),
        migrations.AddField(
            model_name='aula',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.zona'),
        ),
        migrations.AddField(
            model_name='acceso',
            name='persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.persona'),
        ),
    ]
