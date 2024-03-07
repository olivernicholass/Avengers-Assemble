# Generated by Django 5.0.2 on 2024-03-07 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tixx', '0002_event_delete_testmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('userId', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('userEmail', models.EmailField(max_length=254)),
                ('userPhoneNumber', models.CharField(max_length=10)),
                ('userAddress', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='eventDate',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='eventName',
        ),
        migrations.RemoveField(
            model_name='event',
            name='id',
        ),
        migrations.AddField(
            model_name='event',
            name='eventDescription',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AddField(
            model_name='event',
            name='eventId',
            field=models.IntegerField(default='', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='eventLocation',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='eventStatus',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('paymentId', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('paymentAmount', models.FloatField()),
                ('paymentMethod', models.CharField(max_length=10)),
                ('paymentDate', models.DateField()),
                ('transactionId', models.CharField(max_length=10)),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tixx.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewRating', models.IntegerField()),
                ('reviewTitle', models.CharField(max_length=10)),
                ('reviewText', models.CharField(max_length=50)),
                ('reviewDate', models.DateField()),
                ('eventID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tixx.event')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticketId', models.IntegerField(primary_key=True, serialize=False)),
                ('seatNum', models.CharField(max_length=5)),
                ('ticketQR', models.CharField(max_length=250)),
                ('ticketPrice', models.IntegerField()),
                ('ticketType', models.CharField(max_length=10)),
                ('eventId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tixx.event')),
            ],
        ),
    ]
