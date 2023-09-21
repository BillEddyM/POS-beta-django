# Generated by Django 4.2.5 on 2023-09-21 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('categoria_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('laboratorio_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Laboratorios',
            },
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('medicamento_id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('stock', models.IntegerField()),
                ('fecha_expiracion', models.DateField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicamento.categoria')),
                ('laboratorio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicamento.laboratorio')),
            ],
            options={
                'verbose_name_plural': 'Medicamentos',
            },
        ),
    ]
