import os
from distutils.util import strtobool
from os import getenv
from X.helpers.cmd import cmd
from dotenv import load_dotenv

load_dotenv("config.env")

ALIVE_EMOJI = getenv("ALIVE_EMOJI", "🥵")
ALIVE_LOGO = getenv("ALIVE_LOGO", "https://mallucampaign.in/images/img_1708914936.jpg")
ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "Hey, I am alive.")
API_HASH = getenv("API_HASH", "7bc7d1f9b2f3d3f1bfd272db56ac0ba1")
API_ID = getenv("API_ID", "26724473")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "3.0.0@main"
BRANCH = getenv("BRANCH", "main") #don't change this line 
CMD_HNDLR = cmd
OWNER_ID = getenv("OWNER_ID", "940232666")
BOT_TOKEN = getenv("BOT_TOKEN", "6674916212:AAFR7m4fB5Z98YxMh7pVNKf12v21rZBs4Y0")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "")
CHANNEL = getenv("CHANNEL", "MusicStreamMp3")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "postgres://igzvmvzd:4G6i3O51PB9ZBSO0RcArUlcBBoWMv-es@bubble.db.elephantsql.com/igzvmvzd")
GIT_TOKEN = getenv("GIT_TOKEN", "")
GROUP = getenv("GROUP", "MusicStreamSupport")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/Vooyage21/Zubot.git")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGXyHkAuq5VN9x9RfN7zt7wednQUB0PgBHtLZ4-OvC9RIah4QxTQfLNrwb0_kVcB_7Jhz5fbA6T18YUca52i5Y8LU-y0F_lOvkfukoKBZcSQOKP-aCdJlJKpITT-jzUMW8uqDDk5fX8NrlANSeY6MXOBtZpQ7DS0FZVaCdQJrxXrORuZQxSDuwvedUoex2wNcZPQxno6zSgAt8xy3mfn9Q-DraPxnplGLllYeKn3q7kd5_cE9JbtqqDcOe0u6qoUaijN_Ff85DK58zn7KZkE7KvysoainCbFktH4VdbL7edasxG3GTAcPeZ9i6k8sO1NWea7l1N9D-XA7SU3fktBDtQkOr8QQAAAAA4Cs_aAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "940232666").split()))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001627039023]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "-1001627039023").split()}
