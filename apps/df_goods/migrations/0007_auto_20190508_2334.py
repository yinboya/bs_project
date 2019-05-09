# Generated by Django 2.0.12 on 2019-05-08 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0006_auto_20190508_2330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typeinfo',
            name='add_time',
        ),
        migrations.AlterField(
            model_name='typeinfo',
            name='category_type',
            field=models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], default=1, help_text='类目级别', verbose_name='类目级别'),
        ),
    ]
