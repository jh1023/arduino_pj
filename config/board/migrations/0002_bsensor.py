# Generated by Django 3.1.5 on 2021-01-20 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BSensor',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('s_data', models.CharField(blank=True, max_length=255, null=True)),
                ('s_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'b_sensor',
                'managed': False,
            },
        ),
    ]
