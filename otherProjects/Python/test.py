import bs4
import requests
import os

archiveURL = "https://game-scripts-wiki.blogspot.com/2023/03/god-of-war-ragnarok-transcript.html"

def getScript():
	r = requests.get(archiveURL)
	s = bs4.BeautifulSoup(r.content, 'html.parser')
    
    text = []
    for item in s.findAll('p'):
		print(f"{item.text}")
        text.append(item.text)
    print(text)
    downloadFile(text)
    return
    
def downloadFile(text):
    fName = "output.txt"
    print("Downloading " + fName)
    wDir = os.getcwd()
    fDep = os.path.join(wDir, fName)
    print(fDep)
    with open(fDep, 'w') as f:
            for item in text:
                f.write(item + '\n')
                print("Downloaded " + item)
    return
    
if __name__ == "__main__":
    getLinks = getScript()