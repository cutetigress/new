# Generated by Django 4.2.4 on 2023-08-15 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_client_joined_date_client_phone_member_joined_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matters',
            name='clientnumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='matters',
            name='createtime',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='modifiedtime',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='createtime',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='requestid',
            field=models.IntegerField(null=True),
        ),
    ]
