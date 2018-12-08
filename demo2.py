import requests
import bs4
import time

def open_url(url):
    headers = {'user-agent':'IE/10.0'}
    r = requests.get(url,headers=headers,timeout=30)
    r.raise_for_status()
    
    return r

def find_movies(r):
    soup = bs4.BeautifulSoup(r.text,"html.parser")
    
    #name
    movies = []
    targets = soup.find_all("div",class_="pl2")
    for each in targets:
        a = each.a.text.replace(' ','')
        b = a.replace('\n','')
        movies.append(b)

    #mark
    mark = []
    targets = soup.find_all("span",class_="rating_nums")
    for each in targets:
        mark.append(each.text)

    result = []
    count = 1
    lenth = len(movies)
    for i in range(lenth):
       # if float(mark[i]) >= 7.8:
            result.append('%s.'% count + movies[i] +"   "+mark[i]+ '\n\n')
            count += 1

    return result

def main():
    url = "https://movie.douban.com/chart"   
    r = open_url(url)
    result = find_movies(r)

    ISOTIMEFORMAT = '%Y-%m-%d'

    str1 = time.strftime(ISOTIMEFORMAT,time.localtime()) 

    with open("优秀新片" + str1 + ".txt","w",encoding=r.apparent_encoding) as f:
        for each in result:
            f.write(each)
        f.close()

if __name__=="__main__":
    main()

