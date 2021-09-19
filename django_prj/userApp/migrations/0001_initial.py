# Generated by Django 3.2.7 on 2021-09-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('phone_nr', models.CharField(blank=True, max_length=13)),
                ('age', models.IntegerField(blank=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1)),
            ],
        ),
    ]
