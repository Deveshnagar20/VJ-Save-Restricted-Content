import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "85ef94c1c03dd427c4acb85bf66e4f6d")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://nagardevesh2004:D5ILZ4RAldMuzQsS@deveshngr.cd17t.mongodb.net/?retryWrites=true&w=majority&appName=Deveshngr")
