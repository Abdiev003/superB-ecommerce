# Generated by Django 3.2.6 on 2021-08-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=50, verbose_name='First Name')),
                ('email', models.EmailField(db_index=True, max_length=254, verbose_name='Email Address')),
                ('company', models.CharField(blank=True, max_length=80, null=True, verbose_name='Company')),
                ('telephone', models.CharField(max_length=13, verbose_name='Telephone')),
                ('address', models.CharField(max_length=254, verbose_name='Address')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ('-created_at',),
            },
        ),
    ]
