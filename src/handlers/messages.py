from bojango.core.routing import message, callback
from bojango.action.dispatcher import ActionManager
import re

@message()
async def handle_comment(update, context):
    text = update.message.text.strip()
    if context.user_data.get('awaiting') == 'comment':
        await ActionManager.redirect('s_comment_save', update, context)
    elif context.user_data.get('awaiting') == 'phone':
        if re.fullmatch(r'^\+7\d{10}$', text):
            await ActionManager.redirect('s_name', update, context)
        else:
            await update.message.reply_text("❗ Неверный формат. Введите номер в формате: +7XXXXXXXXXX")
    elif context.user_data.get('awaiting') == 'name':
        context.user_data['u_name'] = text
        await ActionManager.redirect('s_finale',update, context)