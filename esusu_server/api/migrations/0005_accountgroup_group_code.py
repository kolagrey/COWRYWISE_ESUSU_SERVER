# Generated by Django 2.2.3 on 2019-08-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_account_group_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountgroup',
            name='group_code',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]