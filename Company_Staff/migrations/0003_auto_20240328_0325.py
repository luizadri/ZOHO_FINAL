# Generated by Django 3.2.23 on 2024-03-28 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0002_auto_20240328_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='price_list',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Company_Staff.pricelist'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='price_list_applied',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
