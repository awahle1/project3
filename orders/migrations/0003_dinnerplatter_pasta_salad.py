# Generated by Django 2.1.5 on 2020-04-20 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_sub'),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerPlatter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salad', models.CharField(choices=[('Garden Salad', 'Garden Salad'), ('Greek Salad', 'Greek Salad'), ('Antipasto', 'Antipasto'), ('Baked Ziti', 'Baked Ziti'), ('Meatball Parm', 'Meatball Parm'), ('Chicken Parm', 'Chicken Parm')], default='Baked Ziti', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salad', models.CharField(choices=[('Baked Ziti w/Mozzarella', 'Baked Ziti w/Mozzarella'), ('Baked Ziti w/Meatballs', 'Baked Ziti w/Meatballs'), ('Baked Ziti w/Chicken', 'Baked Ziti w/Chicken')], default='Baked Ziti w/Mozzarella', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salad', models.CharField(choices=[('Garden Salad', 'Garden Salad'), ('Greek Salad', 'Greek Salad'), ('Antipasto', 'Antipasto'), ('Salad w/Tuna', 'Salad w/Tuna')], default='Garden Salad', max_length=15)),
            ],
        ),
    ]
