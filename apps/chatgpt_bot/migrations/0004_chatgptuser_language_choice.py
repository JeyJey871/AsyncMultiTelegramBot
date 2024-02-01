# Generated by Django 5.0.1 on 2024-02-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatgpt_bot', '0003_alter_chatgptuser_current_chat_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgptuser',
            name='language_choice',
            field=models.CharField(choices=[('uz', 'Uzbek'), ('en', 'English'), ('ru', 'Russian'), ('es', 'Spanish'), ('fr', 'French'), ('de', 'German')], default='uz', max_length=255, null=True),
        ),
    ]
