# Generated by Django 3.2.6 on 2021-09-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profiles/default_profile.png', null=True, upload_to='profiles/'),
        ),
    ]
