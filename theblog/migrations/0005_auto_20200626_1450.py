# Generated by Django 3.0.7 on 2020-06-26 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_auto_20200626_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
