# Generated by Django 4.1.7 on 2023-04-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(max_length=10)),
                ('image', models.ImageField(upload_to='media/')),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
