import re # for regular expressions  
import random # for generating random numbers
import requests # for sending https requests
from bs4 import BeautifulSoup # to extract the data out of html files
import networkx as nx # to generate the graph
import matplotlib.pyplot as plt # to visualize the generated graph

# function to return a random link from the already explored links
def getRandomLink(filePath):
    links = open(filePath).read().splitlines()
    # if no link has been written to the file
    if len(links) == 0:
        return ""
    return random.choice(links)

# function to perform a random walk on the web
def webSurf(url, base, filePath, depth, teleportationProbability):
    file = open(filePath, "w", buffering=1) # opening the file to write the links to
    visitedPages = set()
    isFileEmpty = True

    # initialising the graph of the links
    G = nx.Graph() 

    # perfoms the random walk for 'depth' number of iterations
    for ite in range(depth):
        G.add_node(url)
        connectionError = False
        num = random.randint(1,10) / 10

        # to teleport to a random link with a probability of 'teleportationProbability'
        if num <= teleportationProbability and isFileEmpty == False:
            url = getRandomLink(filePath)
            print(f"TELEPORTING TO: {url}")
        # to extract the links of the current page, and then surf to a random link
        else:
            # for handling connection errors
            try:
                page = requests.get(url)
                soup = BeautifulSoup(page.content,'html.parser')
            except:
                connectionError = True

            if connectionError == True:
                if isFileEmpty == True:
                    print("UNABLE TO SET CONNECTION WITH THE INITIAL URL!")
                    break
                else:
                    print(f"CONNECTION ERROR WITH: {url}")
                    url = getRandomLink(filePath)
                    print(f"TELEPORTING TO: {url}")
                    continue
            
            # extracting all the links of the current page
            links = set()
            for item in soup.find_all('a'):
                if 'href' in item.attrs:
                    link = str(item['href'])
                    # if 'iitrpr' not in link:
                    #     continue

                    # cleaning of the links
                    if 'http' not in link[:5]:
                        link = base + link

                    if ('#' in link) or ('&' in link) or ('%' in link) or ('?' in link):
                        continue
                    links.add(link)

            # if no links found at the current page
            if len(links) == 0:
                if isFileEmpty == True:
                    print("NO LINKS FOUND AT THE INITIAL URL!")
                    break
                else:
                    print(f"NO LINKS FOUND AT: {url}")
                    url = getRandomLink(filePath)
                    print(f"TELEPORTING TO: {url}")
                    continue
            
            # if we are at a new page, then write all the extracted links to the output file
            if url not in visitedPages:
                visitedPages.add(url)
                for link in links:
                    encodedLink = str(link.encode('utf-8'))
                    # for handling encoding errors
                    try:
                        file.write(encodedLink[2:-1])
                        file.write('\n')
                        G.add_node(encodedLink[2:-1])
                        G.add_edge(url,encodedLink[2:-1]) # adding edges to the graph
                        isFileEmpty = False
                    except:
                        # continue
                        print(f"ENCODING ERROR WITH: {encodedLink[2:-1]}")

            # selecting a random link to surf to
            url = random.choice(list(links))
            print(f"NOW VISITING: {url}")
            pattern = re.search('//(.+?)/', url)
            if pattern:
                found = 'https://' + pattern.group(1)
                if found != base:
                    print(f"NEW DOMAIN ENCOUNTERED: {found}")
                base = found

    # to view the generated graph
    nx.draw(G, with_labels=True)
    plt.show()



filePath = "Links.txt"
base = "https://iitrpr.ac.in"
url = "https://iitrpr.ac.in"
webSurf(url, base, filePath, 30, 0.2)
