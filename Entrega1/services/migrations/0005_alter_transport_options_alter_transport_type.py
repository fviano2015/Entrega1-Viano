# Generated by Django 4.1.5 on 2023-01-20 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_alter_transport_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transport',
            options={'verbose_name': 'Transporte', 'verbose_name_plural': 'Transportes'},
        ),
        migrations.AlterField(
            model_name='transport',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]