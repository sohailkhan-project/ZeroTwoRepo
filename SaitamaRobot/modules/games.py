import html
import random
import time

from telegram import ParseMode, Update, ChatPermissions
from telegram.ext import CallbackContext, run_async
from telegram.error import BadRequest

import SaitamaRobot.modules.fun_strings as fun_strings
from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from SaitamaRobot.modules.helper_funcs.chat_status import (is_user_admin)
from SaitamaRobot.modules.helper_funcs.extraction import extract_user


@run_async
def truth(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.TRUTH_STRINGS))


@run_async
def dare(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.DARE_STRINGS))


@run_async
def tord(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.TORD_STRINGS))

@run_async
def wyr(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.WYR_STRINGS))
    
TNG = "https://telegra.ph/file/2632bf79c7a184cac562c.png"    
    
@run_async
def tng(update, context):
    number = random.choice(range(1, 147))
    update.effective_message.reply_photo(TNG, caption=number,
                        parse_mode=ParseMode.MARKDOWN)    


__help__ = """
 • `/truth`*:* asks you a question
 • `/dare`*:* gives you a dare
 • `/tord`*:* can be a truth or a dare
 • `/rather`*:* would you rather
 • `/tng`*:* TNG: The Number Game, answer the question respective to the number.
  """

TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)
TORD_HANDLER = DisableAbleCommandHandler("tord", tord)
WYR_HANDLER = DisableAbleCommandHandler("rather", wyr)
TNG_HANDLER = DisableAbleCommandHandler("tng", tng)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(TORD_HANDLER)
dispatcher.add_handler(WYR_HANDLER)
dispatcher.add_handler(TNG_HANDLER)

__mod_name__ = "Games"
__command_list__ = [
   "truth", "dare", "tord", "rather", "tng"
]

__handlers__ = [
    TRUTH_HANDLER, DARE_HANDLER, TORD_HANDLER, WYR_HANDLER, TNG_HANDLER
]
