# Generated by Django 4.2.2 on 2023-06-20 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_resident_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('start',)},
        ),
    ]
