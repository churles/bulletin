# Generated by Django 3.2.9 on 2022-05-18 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
