import requests
from bs4 import BeautifulSoup

def extractURL(url):
import time # ebb: need to have the scraper wait a second between requests, so using this library
import random # ebb: we can use this to randomize the amount of time between requests.

# ebb: We need to send web browser headers so this little academic python scraper doesn't look like a threatening bot attack. 
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://deadbydaylight.wiki.gg/",
}

def extractURL(session, url):
# ebb: giving it 3 retries to work around 429 "too many requests" errors
    """Grabbing the lore of characters in Dead by Daylight"""
    results = []

    try:
        response = requests.get(url)
        response.raiseStatus()  # will raise an error if bad request

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")

        for p in soup.findAll("p"):
            iTag = p.find("i")
            if iTag and iTag.parent == p:
                text = iTag.getText(strip=True)
                if text:
                    results.append(text)

                break
    except Exception as e:
        print(f"Error fetching {url}: {e}")

		"https://deadbydaylight.wiki.gg/wiki/Burong_Sukapat",
		"https://deadbydaylight.wiki.gg/wiki/Henry_Creel",
    ]

    for url in urls:
        extracted = extractURL(url)
        if extracted:
            saveResults(url, extracted, outputFile)

    print("Lore has been compiled in", outputFile)
    
    with requests.Session() as session:
        session.headers.update(HEADERS) # ebb: Here we're sending the browser headers to show we're safe. 
        
        for i, url in enumerate(urls):
            print(f"Fetching ({i+1}/{len(urls)}): {url}")
            extracted = extractURL(session, url)
            if extracted:
                saveResults(url, extracted, outputFile)
            time.sleep(random.uniform(2, 5))  # ebb: This waits some random amount between 2 and 5 seconds between requests.
            print("Lore has been compiled in", outputFile)