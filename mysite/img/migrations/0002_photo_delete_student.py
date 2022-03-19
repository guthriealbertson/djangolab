# Generated by Django 4.0.3 on 2022-03-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]