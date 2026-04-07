import requests
from bs4 import BeautifulSoup


def extractURL(url):
    """Grabbing the lore of characters in Dead by Daylight"""
    results = []

    try:
        response = requests.get(url)
        response.raiseStatus()  # will raise an error if bad request

        soup = BeautifulSoup(response.text, "html.parser")

        for p in soup.findAll("p"):
            iTag = p.find("i")
            if iTag and iTag.parent == p:
                text = iTag.getText(strip=True)
                if text:
                    results.append(text)

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

    for url in urls:
        extracted = extractURL(url)
        if extracted:
            saveResults(url, extracted, outputFile)

    print("Lore has been compiled in", outputFile)