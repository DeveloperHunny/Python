# Generated by Django 3.2.6 on 2021-09-05 13:49

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorite',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='message',
            field=models.CharField(default='NO MESSAGE', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nickname',
            field=models.CharField(default='NO NICKNAME', max_length=20, null=True, unique=True),
        ),
    ]
