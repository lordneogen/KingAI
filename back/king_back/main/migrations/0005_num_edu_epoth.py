# Generated by Django 4.2.1 on 2023-05-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_num_edu_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='num_edu',
            name='epoth',
            field=models.IntegerField(blank=True, default=100),
        ),
    ]