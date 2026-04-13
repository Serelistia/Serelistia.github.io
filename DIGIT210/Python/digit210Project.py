import requests
from bs4 import BeautifulSoup
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

    return results


def saveResults(url, results, outputFile):
    """Saving the lore to a separate text file"""
    with open(outputFile, "a", encoding="utf-8") as f:
        f.write(f"URL: {url}\n")
        f.write("-" * 50 + "\n")

        for item in results:
            f.write(f"- {item}\n")

        f.write("\n\n")


if __name__ == "__main__":
    outputFile = "output.txt"

    # selection of links to be grabbed
    urls = [
        "https://deadbydaylight.wiki.gg/wiki/Evan_MacMillan",
        "https://deadbydaylight.wiki.gg/wiki/Philip_Ojomo",
		"https://deadbydaylight.wiki.gg/wiki/Max_Thompson_Jr.",
		"https://deadbydaylight.wiki.gg/wiki/Sally_Smithson",
		"https://deadbydaylight.wiki.gg/wiki/Michael_Myers",
		"https://deadbydaylight.wiki.gg/wiki/Lisa_Sherwood",
		"https://deadbydaylight.wiki.gg/wiki/Herman_Carter",
		"https://deadbydaylight.wiki.gg/wiki/Anna",
		"https://deadbydaylight.wiki.gg/wiki/Bubba_Sawyer",
		"https://deadbydaylight.wiki.gg/wiki/Freddy_Krueger",
		"https://deadbydaylight.wiki.gg/wiki/Amanda_Young",
		"https://deadbydaylight.wiki.gg/wiki/Kenneth_Chase_alias_Jeffrey_Hawk",
		"https://deadbydaylight.wiki.gg/wiki/Rin_Yamaoka",
		"https://deadbydaylight.wiki.gg/wiki/Frank,_Julie,_Susie_,Joey",
		"https://deadbydaylight.wiki.gg/wiki/Adiris",
		"https://deadbydaylight.wiki.gg/wiki/Danny_Johnson_alias_Jed_Olsen",
		"https://deadbydaylight.wiki.gg/wiki/The_Demogorgon",
		"https://deadbydaylight.wiki.gg/wiki/Kazan_Yamaoka",
		"https://deadbydaylight.wiki.gg/wiki/Caleb_Quinn",
		"https://deadbydaylight.wiki.gg/wiki/Pyramid_Head",
		"https://deadbydaylight.wiki.gg/wiki/Talbot_Grimes",
		"https://deadbydaylight.wiki.gg/wiki/Charlotte_%26_Victor_Deshayes",
		"https://deadbydaylight.wiki.gg/wiki/Hak_Ji-woon",
		"https://deadbydaylight.wiki.gg/wiki/Nemesis_T-Type",
		"https://deadbydaylight.wiki.gg/wiki/Elliot_Spencer",
		"https://deadbydaylight.wiki.gg/wiki/Carmina_Mora",
		"https://deadbydaylight.wiki.gg/wiki/Sadako_Yamamura",
		"https://deadbydaylight.wiki.gg/wiki/The_Dredge",
		"https://deadbydaylight.wiki.gg/wiki/Albert_Wesker",
		"https://deadbydaylight.wiki.gg/wiki/Tarhos_Kovács",
		"https://deadbydaylight.wiki.gg/wiki/Adriana_Imai",
		"https://deadbydaylight.wiki.gg/wiki/HUX-A7-13",
		"https://deadbydaylight.wiki.gg/wiki/The_Xenomorph",
		"https://deadbydaylight.wiki.gg/wiki/Charles_Lee_Ray",
		"https://deadbydaylight.wiki.gg/wiki/The_Unknown",
		"https://deadbydaylight.wiki.gg/wiki/Vecna",
		"https://deadbydaylight.wiki.gg/wiki/Dracula",
		"https://deadbydaylight.wiki.gg/wiki/Portia_Maye",
		"https://deadbydaylight.wiki.gg/wiki/Ken_Kaneki",
		"https://deadbydaylight.wiki.gg/wiki/William_Afton",
		"https://deadbydaylight.wiki.gg/wiki/Burong_Sukapat",
		"https://deadbydaylight.wiki.gg/wiki/Henry_Creel",
    ]
    
    with requests.Session() as session:
        session.headers.update(HEADERS) # ebb: Here we're sending the browser headers to show we're safe. 
        
        for i, url in enumerate(urls):
            print(f"Fetching ({i+1}/{len(urls)}): {url}")
            extracted = extractURL(session, url)
            if extracted:
                saveResults(url, extracted, outputFile)
            time.sleep(random.uniform(2, 5))  # ebb: This waits some random amount between 2 and 5 seconds between requests.
            print("Lore has been compiled in", outputFile)
