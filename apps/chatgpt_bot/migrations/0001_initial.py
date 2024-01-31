# Generated by Django 5.0.1 on 2024-01-31 21:42

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bot_main_setup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_mode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('model_name', models.CharField(max_length=200)),
                ('model_type', models.CharField(blank=True, max_length=200, null=True)),
                ('welcome_message', models.TextField()),
                ('prompt_start', models.TextField(blank=True, null=True)),
                ('parse_mode', models.CharField(blank=True, default='html', max_length=200, null=True)),
                ('extra_field', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openai_api_base', models.CharField(blank=True, max_length=200, null=True)),
                ('new_dialog_timeout', models.IntegerField(blank=True, default=600, null=True)),
                ('return_n_generated_images', models.IntegerField(default=1)),
                ('n_chat_modes_per_page', models.IntegerField(default=5)),
                ('image_size', models.CharField(default='512x512', max_length=200)),
                ('enable_message_streaming', models.BooleanField(default=True)),
                ('chatgpt_price_per_1000_tokens', models.FloatField(default=0.006)),
                ('gpt_price_per_1000_tokens', models.FloatField(default=0.002)),
                ('whisper_price_per_1_min', models.FloatField(default=0.006)),
                ('extra_field', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Config',
                'verbose_name_plural': 'Configs',
            },
        ),
        migrations.CreateModel(
            name='GptModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=200, unique=True)),
                ('config', models.JSONField()),
            ],
            options={
                'verbose_name': 'Gpt Model',
                'verbose_name_plural': 'Gpt Models',
                'db_table': 'gpt_models',
            },
        ),
        migrations.CreateModel(
            name='Subscribtion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('price', models.FloatField()),
                ('n_tokens', models.IntegerField()),
                ('n_images', models.IntegerField()),
                ('n_tts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TokenPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('price', models.FloatField()),
                ('n_tokens', models.IntegerField()),
                ('n_images', models.IntegerField()),
                ('n_tts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ChatGptUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chat_id', models.BigIntegerField(blank=True, null=True)),
                ('last_interaction', models.DateTimeField(auto_now=True)),
                ('first_seen', models.DateTimeField(auto_now_add=True, null=True)),
                ('current_chat_mode', models.CharField(default='assistant', max_length=255)),
                ('n_used_tokens', models.PositiveBigIntegerField(blank=True, null=True)),
                ('n_generated_images', models.IntegerField(blank=True, default=0, null=True)),
                ('n_transcribed_seconds', models.IntegerField(blank=True, default=0, null=True)),
                ('user_allowed', models.BooleanField(default=True)),
                ('is_blocked', models.BooleanField(default=False)),
                ('user_token', models.CharField(blank=True, default='747e7909a37d452c8e18407a7e60459a', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot_main_setup.telegramprofile', verbose_name='Telegram User')),
            ],
            options={
                'verbose_name': 'ChatGpt User',
                'verbose_name_plural': 'ChatGpt Users',
            },
        ),
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('chat_mode', models.CharField(default='assistant', max_length=255)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bot_main_setup.telegrambot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatgpt_bot.chatgptuser', verbose_name='ChatGpt User')),
            ],
            options={
                'verbose_name': 'Dialog',
                'verbose_name_plural': 'Dialogs',
                'db_table': 'dialog',
            },
        ),
        migrations.CreateModel(
            name='Messages_dialog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField()),
                ('bot', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('dialog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chatgpt_bot.dialog')),
            ],
        ),
        migrations.CreateModel(
            name='TextModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('key', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Text Model',
                'verbose_name_plural': 'Text Models',
                'db_table': 'text_model',
                'unique_together': {('name', 'key')},
            },
        ),
        migrations.AddField(
            model_name='dialog',
            name='gpt_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chatgpt_bot.textmodel'),
        ),
        migrations.AddField(
            model_name='chatgptuser',
            name='current_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='chatgpt_bot.textmodel'),
        ),
    ]
