# Generated by Django 4.2.2 on 2023-07-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0002_alter_sitesetting_email_alter_sitesetting_fax_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='site_logo',
            field=models.ImageField(upload_to='uploads/setting', verbose_name='لوگو سایت'),
        ),
    ]
