from bs4 import BeautifulSoup
import cloudscraper
import os
import random
import requests
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def extractURL(scraper, url):
    try:
        time.sleep(random.uniform(1, 2))
        response = scraper.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        loreHeading = soup.find("span", {"id": "Lore"})
        if not loreHeading:
            print("No Lore section found")
            return[]
            
        h2 = loreHeading.find_parent("h2")
        
        results = []
        
        for sibling in h2.find_next_siblings():
            if sibling.name == "h2":
                break
                
            if sibling.name == "p":
                text = sibling.get_text(" ", strip = True)
                if text:
                    results.append(text)
                
        return results
        
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []
    
def urlToFileName(url):
    name = url.split("/wiki/")[-1]
    return f"{name}.txt"
    
def saveResults(url, data, outputFile):
    with open(outputFile, "a", encoding="utf-8") as f:
        f.write(f"\n\n--- {url} ---\n\n")
        for line in data:
            f.write(line + "\n")

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

    outputFile = "lore.txt"

    scraper = cloudscraper.create_scraper()
    scraper.headers.update(HEADERS)
    
    for i, url in enumerate(urls):
        print(f"Fetching ({i+1}/{len(urls)}): {url}")
        
        outputFile = urlToFileName(url)
        
        extracted = extractURL(scraper, url)
        print("EXTRACTED:", len(extracted))
        
        if extracted:
            saveResults(url, extracted, outputFile)
                
        time.sleep(random.uniform(2, 4))
    
    print("Lore has been compiled in", outputFile)
    
if __name__ == "__main__":
    main()