from bojango.core.routing import callback
from bojango.action.dispatcher import ActionManager


@callback('l_start')
async def l_start(update, context):
    await ActionManager.redirect('s_start', update, context)