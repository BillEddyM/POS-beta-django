# Generated by Django 4.2.5 on 2023-10-19 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0003_remove_proveedor_tipo_producto_proveedor_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='proveedor_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]