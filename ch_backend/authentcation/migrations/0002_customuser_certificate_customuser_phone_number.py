# Generated by Django 4.2.5 on 2023-09-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentcation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='certificate',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
