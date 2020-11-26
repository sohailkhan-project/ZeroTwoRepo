"""from SaitamaRobot import telethn
import time
from telethon import events

def get_arg(message):
    return message.get_args().split(' ')[0]

@telethn.on(events.NewMessage(pattern="^[!/]zombies$"))
async def zombie_clean(message):
    chat_id = message.chat.id
    check_user = await message.client.get_chat_member(message.chat.id, message.from_user.id)
    arg = get_arg(message).lower()
    rm_delaccs = clean in arg
    can_clean = check_user.status in ("administrator", "creator")
    if rm_delaccs:
        del_users = 0
        del_admins = 0
        del_total = 0
        del_stats = r"No deleted accounts found, Group is clean."
        if can_clean:
            await message.edit("Hang on!! cleaning zombie accounts from this chat..")
            async for member in message.client.iter_chat_members(chat_id):
                if member.user.is_deleted:
                    try:
                        await message.client.kick_chat_member(
                            chat_id,
                            member.user.id, int(time.time() + 45))
                    except UserAdminInvalid:
                        del_users -= 1
                        del_admins += 1
                    except FloodWait as e_f:
                        time.sleep(e_f.x)
                    del_users += 1
                    del_total += 1
            if del_admins > 0:
                del_stats = f"`Found` **{del_total}** zombies..\
                \nCleaned **{del_users}** zombie (deleted) accounts from this chat..\
                \n**{del_admins}** deleted admin accounts are skipped!!"
            else:
                del_stats = f"Found` **{del_total}** total zombies..\
                \nCleaned **{del_users}** zombie (deleted) accounts from this chat.."
            await message.edit(f"{del_stats}", del_in=5)
        else:
            await message.edit(r"i don't have proper permission to do that!", del_in=5)
    else:
        del_users = 0
        del_stats = r"Zero zombie accounts found in this chat"
        await message.edit("Searching for zombie accounts in this chat..")
        async for member in message.client.iter_chat_members(chat_id):
            if member.user.is_deleted:
                del_users += 1
        if del_users > 0:
            del_stats = f"Found **{del_users}** zombie accounts in this chat."
            await message.edit(
                f"{del_stats} you can clean them using `/zombies clean`", del_in=5)
        else:
            await message.edit(f"{del_stats}", del_in=5)
"""
