# Generated by Django 3.0.4 on 2020-04-04 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_auto_20200404_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='department_hod_title',
            field=models.CharField(default='Mr', max_length=20),
            preserve_default=False,
        ),
    ]
