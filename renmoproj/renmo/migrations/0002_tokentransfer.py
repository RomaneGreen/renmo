# Generated by Django 2.1.5 on 2019-01-29 04:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('renmo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('tokens', models.IntegerField(default=5)),
                ('transfer_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to='renmo.UserProfile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='renmo.UserProfile')),
            ],
        ),
    ]
