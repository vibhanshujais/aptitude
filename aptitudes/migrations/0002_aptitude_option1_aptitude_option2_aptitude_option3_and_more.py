# Generated by Django 5.0 on 2024-02-08 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptitudes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aptitude',
            name='option1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aptitude',
            name='option2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aptitude',
            name='option3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aptitude',
            name='option4',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='aptitude',
            name='option5',
            field=models.TextField(null=True),
        ),
    ]
