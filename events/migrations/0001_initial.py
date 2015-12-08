# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_store_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('store', models.ForeignKey(related_name='events', to='stores.Store')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('notes', models.TextField(default='', blank=True)),
                ('event', models.ForeignKey(related_name='orders', to='events.Event')),
                ('item', models.ForeignKey(related_name='orders', to='stores.MenuItem')),
                ('user', models.ForeignKey(related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='order',
            unique_together=set([('event', 'user')]),
        ),
    ]
