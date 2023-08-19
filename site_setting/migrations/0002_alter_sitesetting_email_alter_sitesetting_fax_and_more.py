# Generated by Django 4.2.2 on 2023-07-27 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='fax',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='فکس'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='phone',
            field=models.IntegerField(blank=True, max_length=200, null=True, verbose_name='شماره تماس'),
        ),
    ]
