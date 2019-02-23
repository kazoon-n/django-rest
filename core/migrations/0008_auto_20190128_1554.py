# Generated by Django 2.1.5 on 2019-01-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190115_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='doc',
            field=models.CharField(default='testdoc', max_length=12, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='dtype',
            field=models.CharField(choices=[('ID', 'Identity card'), ('PP', 'Passport'), ('OT', 'others')], max_length=2),
        ),
    ]
