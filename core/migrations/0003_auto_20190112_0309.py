# Generated by Django 2.1.5 on 2019-01-12 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190110_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='date_sheet',
            new_name='data_sheet',
        ),
        migrations.AlterField(
            model_name='document',
            name='dtype',
            field=models.CharField(choices=[('ID', 'Identity card'), ('OT', 'others'), ('PP', 'Passport')], max_length=2),
        ),
    ]
