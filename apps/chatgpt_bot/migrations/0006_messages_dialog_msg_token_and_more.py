# Generated by Django 5.0.1 on 2024-02-01 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatgpt_bot", "0005_dialog_input_tokens_dialog_output_tokens"),
    ]

    operations = [
        migrations.AddField(
            model_name="messages_dialog",
            name="msg_token",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="messages_dialog",
            name="dialog",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages_dialog",
                to="chatgpt_bot.dialog",
            ),
        ),
    ]
