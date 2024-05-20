from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
logging.basicConfig(level=logging.DEBUG)

def generate_join_channels_keyboard():

    channel_links = [
        "https://t.me/Colourtrading",
        "https://t.me/addlist/WvSzEb1soLEzZTBl",
    ]
    keyboard = []
    for link in channel_links:
        button = InlineKeyboardButton("𝙈𝙐𝙎𝙏 𝙅𝙊𝙄𝙉 💰", url=link)  # Updated button text to "Join Channel"
        keyboard.append([button])
    
    
    
    
    
    keyboard.append([InlineKeyboardButton("𝙉𝙀𝙓𝙏 ➡️", callback_data="check_joined")])
    
    return InlineKeyboardMarkup(keyboard)

async def check_user_joined_channels(client, user_id, required_channel_ids):
    for channel_id in required_channel_ids:
        logging.debug(f"Checking membership for user {user_id} in channel {channel_id}")
        try:
            member = await client.get_chat_member(channel_id, user_id)
            logging.debug(f"User {user_id} membership status in {channel_id}: {member.status}")
            if member.status in ["left", "kicked"]:
                logging.debug(f"User {user_id} not a member of {channel_id}")
                return False
        except Exception as e:
            logging.error(f"Error checking membership for user {user_id} in channel {channel_id}: {e}")
            return False
    logging.debug(f"User {user_id} is a member of all required channels")
    return True
