import decouple

DEBUG = decouple.config("DEBUG", cast=bool)
DB_URL = decouple.config("DB_URL")
