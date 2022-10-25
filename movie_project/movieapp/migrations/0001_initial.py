# Generated by Django 3.2.15 on 2022-09-29 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dscr', models.TextField()),
                ('year', models.IntegerField()),
            ],
        ),
    ]
