# Generated by Django 3.1.2 on 2024-01-26 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_customuser_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', max_length=100, verbose_name='username'),
        ),
    ]
