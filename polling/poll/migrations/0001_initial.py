# Generated by Django 3.0.7 on 2020-06-06 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('django_know', models.BooleanField(blank=True, default=False, null=True)),
                ('django_unknown', models.BooleanField(blank=True, default=False, null=True)),
                ('django_worked', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GraphqlPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graphql_know', models.BooleanField(blank=True, default=False, null=True)),
                ('graphql_unknown', models.BooleanField(blank=True, default=False, null=True)),
                ('graphql_worked', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RestPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_know', models.BooleanField(blank=True, default=False, null=True)),
                ('rest_unknown', models.BooleanField(blank=True, default=False, null=True)),
                ('rest_worked', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoapPoll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soap_know', models.BooleanField(blank=True, default=False, null=True)),
                ('soap_unknown', models.BooleanField(blank=True, default=False, null=True)),
                ('soap_worked', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeStamped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Polling',
            fields=[
                ('timestamped_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='poll.TimeStamped')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('django', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.DjangoPoll')),
                ('graphql', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.GraphqlPoll')),
                ('rest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.RestPoll')),
                ('soap', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='poll.SoapPoll')),
            ],
            bases=('poll.timestamped',),
        ),
    ]