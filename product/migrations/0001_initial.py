# Generated by Django 3.2.6 on 2021-09-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=80, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=100, verbose_name='Category Slug')),
                ('is_main', models.BooleanField(default=True, verbose_name='Main Category')),
                ('is_second', models.BooleanField(default=False, verbose_name='Second Category')),
                ('is_third', models.BooleanField(default=False, verbose_name='Third Category')),
                ('is_published', models.BooleanField(default=True, verbose_name='Published')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, related_name='_product_category_category_+', to='product.Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('-created_at',),
            },
        ),
    ]