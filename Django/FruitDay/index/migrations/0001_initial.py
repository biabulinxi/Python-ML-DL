# Generated by Django 2.1.4 on 2019-02-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uphone', models.CharField(max_length=11)),
                ('upwd', models.CharField(max_length=50)),
                ('uemail', models.EmailField(max_length=254)),
                ('uname', models.CharField(max_length=30)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
    ]
