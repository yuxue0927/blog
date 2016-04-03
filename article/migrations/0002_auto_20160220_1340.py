# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=64, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(null=True, verbose_name=b'\xe6\xad\xa3\xe6\x96\x87', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'\xe4\xb8\xbb\xe9\xa2\x98'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='article.Tag', blank=True),
        ),
    ]
