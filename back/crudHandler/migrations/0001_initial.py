# Generated by Django 5.1.3 on 2024-11-26 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('api_token', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('documents_ID', models.AutoField(primary_key=True, serialize=False)),
                ('openID', models.IntegerField()),
                ('token', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=255)),
                ('externalID', models.CharField(max_length=255, null=True)),
                ('companyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudHandler.company')),
            ],
        ),
        migrations.CreateModel(
            name='Signers',
            fields=[
                ('signers_ID', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('externalID', models.CharField(max_length=255, null=True)),
                ('documentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crudHandler.documents')),
            ],
        ),
    ]
