def download(fileName, url):
    import requests
    import pickle
    from bs4 import BeautifulSoup
    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36', \
                'Accept-Language': 'en-US, en;q=0.5'})
    print("Download Mode")
    response = requests.get(url).text
    with open(fileName, "wb") as f:
        soup = BeautifulSoup(response, 'html.parser')
        pickle.dump(soup, f)
        f.close()
        return soup


def loadSoup(fileName):  ##DebugMode
    from bs4 import BeautifulSoup
    import pickle
    with open(fileName, "rb") as f:
        soup = pickle.load(f)
        return soup
