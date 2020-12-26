import requests
import os
from bs4 import BeautifulSoup
import lxml

baseUrl = 'https://www.mangareader.net'
manga = "martial-peak"
# will remove the line from the name
manga_name = manga.replace('-', ' ')
# number is used for chapter file incrementation
number = 1


# my functions
def createDirandMoveIntoIt() : 
    os.mkdir('./'+manga_name+'/chapter'+str(number))
    os.chdir('./'+manga_name+'/chapter'+str(number))
    print('Directory created for chapter', str(number))




# gets the main page with the chapter list
response= requests.get(baseUrl+'/'+manga)
soup = BeautifulSoup(response.text, 'lxml')

listChapters = soup.find_all('table')

# if the manga doesn't exist, no need to continue.
if not listChapters:
    print('manga not found')
    quit()


# create folder for the manga if it exists
try:
    os.mkdir(manga_name)
    print('Directory ', manga, ' has been created')
except FileExistsError:
    print('Directory ', manga, ' already exist')



chapterLinks = listChapters[1].find_all('a')
# first iteration on chapters
for chapterLink in chapterLinks:
    chapterURL = chapterLink.get('href')
    try:
        createDirandMoveIntoIt()
        for x in range(1, 18):
            chapter = requests.get(baseUrl + chapterURL) if x == 1 else requests.get(baseUrl+chapterURL+'/'+ str(x))
            chapterSoup = BeautifulSoup(chapter.text, 'lxml')
            pageImg = chapterSoup.find_all('img')
            if pageImg:
                link = 'https:'+pageImg[2].get('src')
                with open('page'+str(x)+'.jpg', 'wb') as f:
                    image = requests.get(link)
                    f.write(image.content)
            else: 
                continue
        os.chdir('..')
        number += 1
    except FileExistsError:
        print('Chapter file already exist')
        number += 1