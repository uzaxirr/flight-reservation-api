# Generated by Django 3.2.7 on 2021-10-11 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flight_api', '0002_rename_passener_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_api.flight'),
        ),
    ]
