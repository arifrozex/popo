# (c) @Damantha_Jasinghe

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
silahkan jika anda mau mengunkan bot ini!
yang ingin memesan bot seerti ini anda bisa langsung hubungi developer.
🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})
🧑🏻‍💻 **Developer:** @ownersri
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @melna21
Terimakasih sudah menggunkan jasa kami. ingat semua file bisa kecuali foto. tolong Gunakan Hal yang Positif.
jika ada kekurangan dalam bot ini anda bisa langsung hubungi admin klik saja lapor
[lapor](https://t.me/ownersri) (lapor)
"""
	HOME_TEXT = """
Hi, [{}](tg://user?id={})\n\nThis is Permanent **link tempat file**.
silakan kirim file dan video anda di bot ini, jangan kirim foto ya. terimaksih telah mendukung! cek **tentang bot** di bawah ini.
"""
