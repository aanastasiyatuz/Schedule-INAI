# Generated by Django 3.2.8 on 2021-12-25 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_alter_order_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dateOfIssue',
            field=models.DateField(),
        ),
    ]
