# Generated by Django 4.2.14 on 2024-09-03 06:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_alter_bedbooking_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('customer_name', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(max_length=100, unique=True)),
                ('phone_with_code', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.EmailField(blank=True, max_length=250, null=True)),
                ('password', models.TextField()),
                ('remember_token', models.CharField(blank=True, max_length=100, null=True)),
                ('profile_picture', models.CharField(default='static_images/avatar.png', max_length=250)),
                ('pre_existing_disease', models.TextField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.IntegerField(blank=True, null=True)),
                ('wallet', models.FloatField(default=0)),
                ('overall_ratings', models.FloatField(default=0)),
                ('no_of_ratings', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=1)),
                ('fcm_token', models.TextField(blank=True, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('age', models.FloatField(blank=True, null=True)),
                ('family_members', models.TextField(blank=True, null=True)),
                ('last_active_address', models.IntegerField(default=0)),
                ('height', models.CharField(blank=True, max_length=20, null=True)),
                ('weight', models.CharField(blank=True, max_length=20, null=True)),
                ('emergency_contact_no', models.CharField(blank=True, max_length=255, null=True)),
                ('allergies', models.CharField(blank=True, max_length=255, null=True)),
                ('current_medications', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('provider_id', models.CharField(blank=True, max_length=255, null=True)),
                ('firebase_user_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
