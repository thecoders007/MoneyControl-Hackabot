from stocktalk import streaming

# Credentials to access Twitter API 
API_KEY = 'xCAwmo5zvuAm8WxbglE48o0MR'
API_SECRET = 'v6R80J38uQgLC5VtwLsk5fgff7GGtn1U43QgRFXTuS1am9wSJe'
ACCESS_TOKEN = '3256740685-x4860mnThe0sggkWqdDjpGQnUBSMjjdAanZi9Wo'
ACCESS_TOKEN_SECRET = '1xAHMYd9cWXFqBImyE71YOt4Ft8D4GfRpHmimn0nhO4W5'
credentials = [API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET]

# First element must be ticker/name, proceeding elements are extra queries
ABB = ['ABB']
DMART = ['DMART']
BHEL = ['TATAPOWER']
TITAN = ['TITAN']

INDIGO = ['INDIGO']
IDEA = ['IDEA']
MRF = ['MRF']
GODREJCP = ['GODREJCP']
LICHSGFIN = ['LICHSGFIN']
JSWSTEEL = ['JSWSTEEL']
PNB = ['PNB']

# Variables
tickers = [ABB,DMART,BHEL,TITAN,INDIGO,IDEA,MRF,GODREJCP,LICHSGFIN,JSWSTEEL,PNB]  # Used for identification purposes
queries = ABB+DMART+BHEL+TITAN+INDIGO+IDEA+MRF+GODREJCP+LICHSGFIN+JSWSTEEL+PNB   # Filters tweets containing one or more query 
refresh = 30                     # Process and log data every 30 seconds

# Create a folder to collect logs and temporary files
path = "/home/krutik/MoneyControl-Hackabot/financial_modeling_tool/stock_prediction/"

streaming(credentials, tickers, queries, refresh, path, \
realtime=True, logTracker=True, logTweets=True, logSentiment=True, debug=True)