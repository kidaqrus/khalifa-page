# Generated by Django 3.0 on 2019-12-13 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Animation', models.ImageField(upload_to='images/')),
                ('Tile', models.CharField(max_length=10)),
                ('Summary', models.CharField(max_length=30)),
            ],
        ),
    ]