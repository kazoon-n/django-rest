# Generated by Django 2.1.5 on 2019-02-17 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190217_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='data_sheet',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.DataSheet'),
        ),
        migrations.AlterField(
            model_name='document',
            name='dtype',
            field=models.CharField(choices=[('ID', 'Identity card'), ('OT', 'others'), ('PP', 'Passport')], max_length=2),
        ),
    ]