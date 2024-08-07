# Generated by Django 5.0 on 2024-02-18 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptitudes', '0006_vocabulary_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='vocab_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='vocabulary',
            name='answer',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vocabulary',
            name='question',
            field=models.TextField(null=True),
        ),
    ]
