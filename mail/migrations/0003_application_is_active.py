# Generated by Django 3.0.4 on 2020-04-04 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_application_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
