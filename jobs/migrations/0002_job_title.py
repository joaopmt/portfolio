# Generated by Django 2.1.7 on 2019-02-14 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='title',
            field=models.CharField(default='default title', max_length=200),
        ),
    ]