# Generated by Django 3.0.7 on 2021-01-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyApi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
            ],
        ),
    ]
