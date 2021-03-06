# Generated by Django 3.0.2 on 2020-12-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100)),
                ('Email', models.CharField(blank=True, max_length=100)),
                ('Subject', models.CharField(blank=True, max_length=255)),
                ('Message', models.CharField(blank=True, max_length=255)),
                ('Note', models.CharField(blank=True, max_length=255)),
                ('Status', models.CharField(blank=True, choices=[('New', 'New'), ('Read', 'Read'), ('Closed', 'Closed')], default='New', max_length=100)),
                ('IP', models.CharField(blank=True, max_length=255)),
                ('Create_at', models.DateTimeField(auto_now_add=True)),
                ('Update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
