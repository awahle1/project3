# Generated by Django 3.0.5 on 2020-04-23 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200423_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pizza',
            field=models.ManyToManyField(related_name='orders', to='orders.Pizza'),
        ),
    ]
