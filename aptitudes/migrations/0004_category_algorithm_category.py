# Generated by Django 5.0 on 2024-02-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aptitudes', '0003_algorithm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='algorithm',
            name='category',
            field=models.TextField(null=True),
        ),
    ]
