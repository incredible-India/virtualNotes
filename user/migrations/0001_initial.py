# Generated by Django 4.0 on 2022-04-10 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='./static/Faculty/img')),
            ],
        ),
    ]
