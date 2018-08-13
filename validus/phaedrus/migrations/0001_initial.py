# Generated by Django 2.1 on 2018-08-11 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GBPEUR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('currency_pair', models.CharField(max_length=200)),
                ('fx_value', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True)),
            ],
        ),
    ]
