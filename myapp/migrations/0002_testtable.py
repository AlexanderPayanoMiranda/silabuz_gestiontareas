# Generated by Django 4.1.3 on 2022-11-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aula', models.CharField(max_length=2)),
                ('hora_entrada', models.TimeField()),
            ],
        ),
    ]
