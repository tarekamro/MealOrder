# Generated by Django 2.1.5 on 2019-05-25 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190526_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meals.Meal'),
        ),
    ]
