# Generated by Django 2.0.4 on 2018-05-22 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('belt_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='wish_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('item_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_items', to='belt_users.LogUsers')),
                ('wisher', models.ManyToManyField(related_name='wish_adder', to='belt_users.LogUsers')),
            ],
        ),
    ]
