# Generated by Django 4.1.13 on 2024-02-28 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Property.category'),
        ),
    ]