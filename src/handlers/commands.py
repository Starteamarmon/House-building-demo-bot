from bojango.core.routing import command
from bojango.action import ActionManager


@command('start')
async def start(update, context):
    await ActionManager.redirect('l_start', update, context)