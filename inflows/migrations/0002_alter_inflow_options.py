# Generated by Django 5.0.6 on 2024-07-05 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inflows', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inflow',
            options={'ordering': ['-created_at']},
        ),
    ]
