import requests
from bs4 import BeautifulSoup
import time
import random
import cloudscraper
import os
 
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
 
def extractURL(scraper, url):
    results = []
    try:
        time.sleep(random.uniform(1, 2))
        response = scraper.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # ebb: So, what you want to do is take what cloudscraper pulls in (whole page HTM),
        # and deliver it to Beautiful Soup which can pull the specific portions of the
        # page you want. To target more specific
        # content on the page (like, just the lore/biography section rather than
        # all paragraphs), go study the HTML on the wiki page and 
        # find the unique HTML element that wraps that section
        # Try looking at it in a web browser's DevTools (right-click → Inspect).
        # I set up a soup.select_one() swap the soup.select_one() call below with that selector. For example:
        #
        #   content = soup.select_one("div.character-lore")  # MADE UP example (I have not looked at your source files)
        # You can usually just set up a nice CSS selector for Beautiful Soup. 
        #
        # From there you can chain .find_all(), .find(), or .select() to drill
        # down to exactly the tags you need (headings, list items, tables, etc.).
        content = soup.select_one("div.mw-parser-output")
 
        if not content:
            print("No content block found")
            return []
            
        paragraphs = []
 
        for p in content.find_all("p"):
            text = p.get_text(" ", strip=True)
            
            if text and len(text) > 30:
                paragraphs.append(text)
        
        return paragraphs
        
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []
 
def getOutputFilename(url, outputDir):
    """Derive a .txt filename from the last segment of the URL path."""
    pageName = url.rstrip("/").split("/")[-1]   # e.g. 'Henry_Creel'
    return os.path.join(outputDir, f"{pageName}.txt")
 
def saveResults(url, data, outputDir):
    outputFile = getOutputFilename(url, outputDir)
    with open(outputFile, "w", encoding="utf-8") as f:
        f.write(f"--- {url} ---\n\n")
        for line in data:
            f.write(line + "\n")
    return outputFile

def main():
    urls = [
    "https://deadbydaylight.wiki.gg/wiki/Henry_Creel",
	"https://deadbydaylight.wiki.gg/wiki/Burong_Sukapat",
	"https://deadbydaylight.wiki.gg/wiki/Animatronic",
    "https://deadbydaylight.wiki.gg/wiki/Ghoul",
    "https://deadbydaylight.wiki.gg/wiki/Houndmaster",
    "https://deadbydaylight.wiki.gg/wiki/Dark_Lord",
    "https://deadbydaylight.wiki.gg/wiki/Lich",
    "https://deadbydaylight.wiki.gg/wiki/Unknown",
    "https://deadbydaylight.wiki.gg/wiki/Good_Guy",
    "https://deadbydaylight.wiki.gg/wiki/Xenomorph",
    "https://deadbydaylight.wiki.gg/wiki/Singularity",
    "https://deadbydaylight.wiki.gg/wiki/Skull_Merchant",
    "https://deadbydaylight.wiki.gg/wiki/Knight",
    "https://deadbydaylight.wiki.gg/wiki/Mastermind",
    "https://deadbydaylight.wiki.gg/wiki/Dredge",
    "https://deadbydaylight.wiki.gg/wiki/Onryō",
    "https://deadbydaylight.wiki.gg/wiki/Artist",
    "https://deadbydaylight.wiki.gg/wiki/Cenobite",
    "https://deadbydaylight.wiki.gg/wiki/The_Nemesis",
    "https://deadbydaylight.wiki.gg/wiki/Trickster",
    "https://deadbydaylight.wiki.gg/wiki/Twins",
    "https://deadbydaylight.wiki.gg/wiki/Blight",
    "https://deadbydaylight.wiki.gg/wiki/Executioner",
    "https://deadbydaylight.wiki.gg/wiki/Deathslinger",
    "https://deadbydaylight.wiki.gg/wiki/Oni",
    "https://deadbydaylight.wiki.gg/wiki/Demogorgon",
    "https://deadbydaylight.wiki.gg/wiki/Ghost_Face",
    "https://deadbydaylight.wiki.gg/wiki/Plague",
    "https://deadbydaylight.wiki.gg/wiki/Legion",
    "https://deadbydaylight.wiki.gg/wiki/Spirit",
    "https://deadbydaylight.wiki.gg/wiki/Clown",
    "https://deadbydaylight.wiki.gg/wiki/Pig",
    "https://deadbydaylight.wiki.gg/wiki/Nightmare",
    "https://deadbydaylight.wiki.gg/wiki/Cannibal",
    "https://deadbydaylight.wiki.gg/wiki/Huntress",
    "https://deadbydaylight.wiki.gg/wiki/Doctor",
    "https://deadbydaylight.wiki.gg/wiki/Hag",
    "https://deadbydaylight.wiki.gg/wiki/Shape",
    "https://deadbydaylight.wiki.gg/wiki/Nurse",
    "https://deadbydaylight.wiki.gg/wiki/Hillbilly",
    "https://deadbydaylight.wiki.gg/wiki/Wraith",
    "https://deadbydaylight.wiki.gg/wiki/Trapper"
    ]

    outputDir = "lore"
    os.makedirs(outputDir, exist_ok=True)   # create lore/ if it doesn't exist
 
    scraper = cloudscraper.create_scraper()
    scraper.headers.update(HEADERS)
    
    for i, url in enumerate(urls):
        print(f"Fetching ({i+1}/{len(urls)}): {url}")
        
        extracted = extractURL(scraper, url)
        print(f"  Paragraphs extracted: {len(extracted)}")
        
        if extracted:
            savedTo = saveResults(url, extracted, outputDir)
            print(f"  Saved → {savedTo}")
                
        time.sleep(random.uniform(2, 4))
    
    print(f"\nDone! All lore files are in the '{outputDir}/' directory.")
    
if __name__ == "__main__":
    main()
 