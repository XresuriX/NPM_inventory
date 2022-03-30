# Generated by Django 4.0 on 2022-03-27 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='report.ingredients', unique=True)),
                ('opening_bgs', models.BigIntegerField(blank=True, null=True)),
                ('opening_kgs', models.FloatField(blank=True, null=True)),
                ('recieved', models.BigIntegerField(blank=True, null=True)),
                ('bags_used_bin', models.BigIntegerField(blank=True, null=True)),
                ('bags_used_Th3', models.BigIntegerField(blank=True, null=True)),
                ('kgs_used_Th3', models.FloatField(blank=True, null=True)),
                ('lot_number', models.CharField(blank=True, max_length=200, null=True)),
                ('current_bgs', models.BigIntegerField(blank=True, null=True)),
                ('current_kgs', models.FloatField(blank=True, null=True)),
                ('total_used_kgs', models.FloatField(blank=True, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('comment_body', models.TextField()),
            ],
        ),
    ]