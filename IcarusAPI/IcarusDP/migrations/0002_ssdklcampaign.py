# Generated by Django 2.1.2 on 2018-10-13 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IcarusDP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SSDKLCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssdkl', models.CharField(max_length=200)),
                ('campaign', models.CharField(max_length=200)),
            ],
        ),
    ]
