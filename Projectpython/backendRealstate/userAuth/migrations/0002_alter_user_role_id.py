# Generated by Django 4.1.13 on 2024-03-04 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAuth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='userAuth.role'),
        ),
    ]
