# Generated by Django 3.2 on 2023-01-15 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20230114_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('id',)},
        ),
    ]