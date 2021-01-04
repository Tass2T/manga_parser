import requests
import os
from bs4 import BeautifulSoup
import lxml


def scrapManga(manga_name, path) : 
    
    os.chdir(path)

    baseUrl = 'https://www.mangareader.net'

    try:
        os.mkdir("manga")
    except FileExistsError:
        print("manga folder ready")

    # number is used for chapter file incrementation
    number = 1
    # my functions
    def createDirAndMoveIntoIt() : 
        os.mkdir('./manga/'+manga_name+'/chapter'+str(number))
        os.chdir('./manga/'+manga_name+'/chapter'+str(number))
        print('Directory created for chapter', str(number))




    # gets the main page with the chapter list
    response= requests.get(baseUrl+'/'+manga_name)
    soup = BeautifulSoup(response.text, 'lxml')

    listChapters = soup.find_all('table')

    # if the manga doesn't exist, no need to continue.
    if not listChapters:
        print('manga not found')
        quit()


    # create folder for the manga if it exists
    try:
        os.mkdir("./manga/"+manga_name)
        print('Directory ', manga_name, ' has been created')
    except FileExistsError:
        print('Directory ', manga_name, ' already exist')



    chapterLinks = listChapters[1].find_all('a')
    # first iteration on chapters
    for chapterLink in chapterLinks:
        chapterURL = chapterLink.get('href')
        try:
            createDirAndMoveIntoIt()
            for x in range(1, 100):
                pageUrl = baseUrl + chapterURL if x == 1 else baseUrl+chapterURL+'/'+ str(x)
                chapter = requests.get(pageUrl)
                chapterSoup = BeautifulSoup(chapter.text, 'lxml')
                pageImg = chapterSoup.find('img',{'id' : "ci"})
                
                if chapter.url == pageUrl:
                    link = 'https:'+pageImg.get('src')
                    with open('page'+str(x)+'.jpg', 'wb') as f:
                        image = requests.get(link)
                        f.write(image.content)
                else: 
                    break
            os.chdir('../../..')
            number += 1
        except FileExistsError:
            print('Chapter file already exist')
            number += 1