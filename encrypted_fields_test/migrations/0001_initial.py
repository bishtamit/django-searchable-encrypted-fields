# Generated by Django 2.1 on 2020-10-08 09:46

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import encrypted_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('_username', encrypted_fields.fields.EncryptedCharField(max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()])),
                ('username', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='_username', error_messages={'unique': 'Custom error message for already exists.'}, hash_key='abc123', max_length=66, null=True, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DemoMigrationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(default='hi', max_length=10)),
                ('info', models.CharField(default='', max_length=10)),
                ('encrypted_data', encrypted_fields.fields.EncryptedCharField(default='hi', max_length=20)),
                ('searchable_encrypted_info', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='encrypted_info', hash_key='abc', max_length=66, null=True)),
                ('encrypted_info', encrypted_fields.fields.EncryptedCharField(default='', max_length=20)),
                ('_encrypted_data', encrypted_fields.fields.EncryptedCharField(default='hi', max_length=20)),
                ('searchable_encrypted_data', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='_encrypted_data', hash_key='abcd', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DemoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_email_data', encrypted_fields.fields.EncryptedEmailField(max_length=254)),
                ('email', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='_email_data', hash_key='123abc', max_length=66, null=True)),
                ('_name_data', encrypted_fields.fields.EncryptedCharField(blank=True, help_text='This field is not required.', max_length=10, null=True)),
                ('name', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='_name_data', hash_key='123abc', max_length=66, null=True)),
                ('_date_data', encrypted_fields.fields.EncryptedDateField()),
                ('date', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='_date_data', hash_key='123abc', max_length=66, null=True)),
                ('date_2', encrypted_fields.fields.EncryptedDateField(blank=True, help_text='This field is just encrypted and is not required.', null=True)),
                ('_number_data', encrypted_fields.fields.EncryptedPositiveSmallIntegerField()),
                ('number', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='_number_data', hash_key='123abc', max_length=66, null=True)),
                ('text', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='_text_data', hash_key='123abc', max_length=66, null=True)),
                ('_text_data', encrypted_fields.fields.EncryptedTextField(help_text='A text area. Not typically used with a SearchField.')),
                ('info', encrypted_fields.fields.EncryptedCharField(blank=True, help_text='Char field, required at db level, without a default and blank=True', max_length=20)),
                ('_default_date_data', encrypted_fields.fields.EncryptedDateField(default=datetime.date.today)),
                ('default_date', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='_default_date_data', hash_key='123abc', max_length=66, null=True)),
                ('_default_number_data', encrypted_fields.fields.EncryptedPositiveSmallIntegerField(default=1)),
                ('default_number', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='_default_number_data', hash_key='123abc', max_length=66, null=True)),
                ('_default_char_data', encrypted_fields.fields.EncryptedCharField(default='foo default', max_length=20)),
                ('default_char', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='_default_char_data', hash_key='123abc', max_length=66, null=True)),
                ('created_at', encrypted_fields.fields.EncryptedDateTimeField(auto_now_add=True)),
                ('updated_at', encrypted_fields.fields.EncryptedDateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EncryptedChar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedCharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='EncryptedDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedDateField()),
            ],
        ),
        migrations.CreateModel(
            name='EncryptedDateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedDateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EncryptedEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedEmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='EncryptedInt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EncryptedNullable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EncryptedText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedTextField()),
            ],
        ),
        migrations.CreateModel(
            name='SearchBigInt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedBigIntegerField()),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchChar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedCharField(max_length=25)),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchCharWithDefault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedCharField(default='foo', max_length=25)),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedDateField()),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchDateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedDateTimeField()),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchDateWithDefault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedDateField(default=datetime.date.today)),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedEmailField(max_length=254)),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchInt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchIntWithDefault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedIntegerField(default=2, validators=[django.core.validators.MaxValueValidator(10)])),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchPosInt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedPositiveIntegerField()),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchPosSmallInt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedPositiveSmallIntegerField()),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchSmallInt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedSmallIntegerField()),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', encrypted_fields.fields.EncryptedTextField()),
                ('search', encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='value', hash_key='abc123', max_length=66, null=True)),
            ],
        ),
    ]
