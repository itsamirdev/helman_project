# Generated by Django 4.2.2 on 2023-08-02 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0002_articlecomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecomment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article_module.article', verbose_name='مقاله'),
        ),
    ]
