# Generated by Django 3.1.4 on 2020-12-16 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ai_evm', '0002_auto_20201216_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='isNominee',
        ),
    ]
