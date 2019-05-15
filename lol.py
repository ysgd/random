import random
import time
import webbrowser

while true:
	sites = random.choice(['https://google.com', 'https://facebook.com', 'https://youtube.com'])
	webbrowser.open(sites)
	t = random.randrange(5, 20)
	time.sleep(t)
	