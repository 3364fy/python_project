# Generated by Django 4.0.1 on 2022-04-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_userinfo_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='names',
            field=models.CharField(max_length=32),
        ),
    ]
