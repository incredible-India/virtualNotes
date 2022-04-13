# Generated by Django 4.0 on 2022-04-13 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_image'),
        ('myNotes', '0002_rename_date_stickynotes_dateof_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('dateOf', models.DateField()),
                ('cimg', models.ImageField(upload_to='categories/')),
                ('clink', models.CharField(max_length=100)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]