from django.utils.translation import gettext_lazy as _
from asgiref.sync import sync_to_async

from apps.chatgpt_bot.models import Dialog

HELP_MESSAGE = str(_("""Commands:
⚪️ /retry – Regenerate last bot answer
⚪️ /new – Start new dialog
⚪️ /mode – Select chat mode
⚪️ /settings – Show settings
⚪️ /balance – Show balance
⚪️ /help – Show help

🎨 Generate images from text prompts in <b>👩‍🎨 Artist</b> /mode
👥 Add bot to <b>group chat</b>: /help_group_chat
🎤 You can send <b>Voice Messages</b> instead of text
"""))

START_MESSAGE = str(_("Hi! I'm ChatGPT bot 🤖"))

IMPORTANT_MESSAGE = str(_("""Important notes:
1. The longer your dialog, the more tokens are spent with each new message. To start new dialog, send /new command
2. Write in 🇬🇧 English for a better quality of answers
3. GPT-4 Turbo consumes 10x more tokens than ChatGPT. So use it when you really need it"""))


def split_text_into_chunks(text, chunk_size):
    """Split text into chunks of 500 characters."""
    return [text[i: i + chunk_size] for i in range(0, len(text), chunk_size)]


@sync_to_async
def get_current_model(chat_gpt_user):
    if chat_gpt_user.current_model.model != "null" or chat_gpt_user.current_model.model is not None:
        return chat_gpt_user.current_model.model
    else:
        return "gpt-3.5-turbo-16k"


@sync_to_async
def get_user_token(chat_gpt_user):
    return chat_gpt_user.user_token


@sync_to_async
def get_current_chat_mode(chat_gpt_user):
    return chat_gpt_user.current_chat_mode.prompt_start


@sync_to_async
def save_custom_language(chat_gpt_user,id):
    chat_gpt_user.language_choice=id
    chat_gpt_user.save()

@sync_to_async
def new_diaolog(user):
    if Dialog.objects.filter(user=user,end=False).exists():
        Dialog.objects.filter(user=user, end=False).update(end=True)
        return True
    else:
        return False




def new_diaolog_sync(user):
    if Dialog.objects.filter(user=user,end=False).exists():
        Dialog.objects.filter(user=user, end=False).update(end=True)
        return True
    else:
        return False





