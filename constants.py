import os
from kivy.config import Config

width, height = 1920, 1080

Config.set('graphics','width',width)
Config.set('graphics','height',height)
Config.set('graphics','fullscreen','True')

EMAIL= os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

# Fetch API endpoint URLs and keys from environment variables
IP_ADDR_API_URL = os.environ.get("IP_ADDR_API_URL")
NEWS_FETCH_API_URL = os.environ.get("NEWS_FETCH_API_URL")
NEWS_FETCH_API_KEY = os.environ.get("NEWS_FETCH_API_KEY")
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Fetch SMTP server configuratiomn from environment variables
SMTP_URL = os.environ.get("SMTP_URL")
SMTP_PORT = os.environ.get("SMTP_PORT")

# Retrieve the screen dimensions from the configuration
SCREEN_WIDTH = Config.getint('graphics', 'width')
SCREEN_HEIGHT = Config.getint('graphics', 'height')

random_text = "This is a random text"


