import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21247842"))
    API_HASH = os.environ.get("API_HASH", "9cdb0caff1fae351aa3bcaf997560b7b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5846369400:AAFt0S1Jt3CrdFIt8R12tCCMkJvfbXDH_mE)
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzUBu1H2D0Sbv8GMjG12Le5mV8KjNWKaTz8laHENvzfsMGYtMD93E_qhKsJznXbQw4UewauDVrLiIQ5Yq7hSjHbqV3AhgcGbt8okc-2wRqcBoxpRzlBKPhmSTBKQAiyIkO-EzZ2g8D3_WYBRZUlI1r2f4NomVh2Qks0vm0W1heD2sJtRMiBla2vC9-oVNSS5QYUQmXYFhZeLIdO0dduqm4ZL9lWY954jG5S_1b9EfeICLHEc0e8OiELUU_MXZdszV_NStX--ZaesMehKlhWx1qe7bl7cr2_iYxaL6ixumWAfmsEKsB4aw-zlKgJUYj9qdfuj5V5xY_ZiXFnxKcb7fmyndeg=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Vcplayertes_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5891780479")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
