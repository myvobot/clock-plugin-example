import logging
import modules.common.color as color
from modules.service.time_service import TimeService

TITLE = "Hello World"
initialized = None
lasttime = 0
counter = 0

#################################################


async def on_refresh(screen, config):
    global initialized, counter, lasttime

    if not initialized:
        initialized = True
        screen.fill(color.ORANGE) # clear screen

    now = TimeService().get_epoch()
    if now % 1 == 0 and now != lasttime:
        logging.debug("@%d", now)
        lasttime = now
        counter += 1
        screen.print_str("Hello Vobot!", 5, 80, color.WHITE, backColor=color.ORANGE, fontId=screen.FONT_ROBOTO_36PX)
        screen.print_str(str(counter), 5, 120, color.WHITE, backColor=color.ORANGE, fontId=screen.FONT_ROBOTO_36PX)


async def on_selected(scr, config):
    pass


async def on_leave(screen, config):
    global initialized
    initialized = False


async def on_enter(screen, config):
    pass


async def on_boot(screen, config):
    pass
