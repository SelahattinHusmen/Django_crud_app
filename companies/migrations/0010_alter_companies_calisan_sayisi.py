# Generated by Django 4.2.1 on 2023-06-04 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0009_alter_companies_calisan_sayisi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='Calisan_sayisi',
            field=models.IntegerField(null=True),
        ),
    ]
