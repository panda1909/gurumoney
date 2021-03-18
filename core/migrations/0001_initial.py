# Generated by Django 3.1 on 2021-03-18 12:05

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=128)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Message', models.TextField(max_length=5000)),
            ],
            options={
                'verbose_name': '1 - Customer Query',
                'verbose_name_plural': '1 - Customer Queries',
            },
        ),
    ]
