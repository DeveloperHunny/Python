# Generated by Django 3.2.6 on 2021-09-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('createDate', models.DateField(auto_now_add=True)),
                ('modifyDate', models.DateField(auto_now=True)),
            ],
        ),
    ]