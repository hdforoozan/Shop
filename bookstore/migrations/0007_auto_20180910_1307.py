# Generated by Django 2.1 on 2018-09-10 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_remove_author_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pubdate',
            field=models.DateField(blank=True),
        ),
    ]