# Generated by Django 2.0.7 on 2019-10-31 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(default='gen', max_length=100),
        ),
    ]
