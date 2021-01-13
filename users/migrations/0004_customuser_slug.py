# Generated by Django 3.1.4 on 2020-12-20 12:10

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201220_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=1, editable=False, populate_from='username'),
            preserve_default=False,
        ),
    ]