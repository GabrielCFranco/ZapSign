# Generated by Django 5.1.3 on 2024-11-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudHandler', '0002_documents_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documents',
            old_name='openID',
            new_name='open_id',
        ),
        migrations.AlterField(
            model_name='documents',
            name='externalID',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
