# Generated by Django 4.2.2 on 2023-07-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us', '0002_alter_contactus_is_read_by_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='response',
            field=models.TextField(blank=True, null=True, verbose_name='متن پاسخ تماس با ما'),
        ),
    ]
