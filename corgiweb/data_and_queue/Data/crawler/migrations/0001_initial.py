# Generated by Django 4.1.3 on 2022-11-19 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='websites_default',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('partition', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]
