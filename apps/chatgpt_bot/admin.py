# apps/your_app/admin.py

from django.contrib import admin

from .models import (
    Chat_mode,
    ChatGptUser,
    Config,
    Dialog,
    GptModels,
    Messages_dialog,
    Subscribtion,
    TextModel,
    TokenPackage,
)


@admin.register(TextModel)
class TextModelAdmin(admin.ModelAdmin):
    list_display = ("name", "key")


@admin.register(Subscribtion)
class SubscribtionAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "n_tokens", "n_images", "n_tts")


@admin.register(TokenPackage)
class TokenPackageAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "n_tokens", "n_images", "n_tts")


@admin.register(ChatGptUser)
class ChatGptUserAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "chat_id", "last_interaction", "current_chat_mode", "current_model")


@admin.register(Dialog)
class DialogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "chat_mode", "start_time", "gpt_model", "bot", "input_tokens", "output_tokens", "end")


@admin.register(Messages_dialog)
class MessagesDialogAdmin(admin.ModelAdmin):
    list_display = ("user", "bot", "dialog", "input_tokens", "output_tokens")


@admin.register(Chat_mode)
class ChatModeAdmin(admin.ModelAdmin):
    list_display = ("key", "model_name", "model_type", "parse_mode", "created_at", "updated_at")


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = (
        "openai_api_base",
        "new_dialog_timeout",
        "return_n_generated_images",
        "n_chat_modes_per_page",
        "image_size",
        "enable_message_streaming",
        "chatgpt_price_per_1000_tokens",
        "gpt_price_per_1000_tokens",
        "whisper_price_per_1_min",
    )


@admin.register(GptModels)
class GptModelsAdmin(admin.ModelAdmin):
    list_display = ("model", "config")
