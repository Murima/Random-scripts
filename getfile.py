#written by Murima
#!/usr/bin/python3
#get the files from thinkpython website
import requests
import bs4
import urllib

def getfile(file):
    count = 0

    for i, e in enumerate(file):
        count = count+1
        print('downloading file{0} which is {1}'.format(count, e))
        urllib.urlretrieve(file[i], filename  =e.split('/')[-1])
        i = i+1

def dump(link):
    response = requests.get(link) #gets response 
    soup = bs4.BeautifulSoup(response.text)#soup gets the html using the response from requests
    #list comprehension to get the attributes of a tab which is href`
    links = [x.attrs.get('href') for x in soup.findAll('a')]
    links = [link+x for x in links]



    return links  #returns full links

def main():

    result = dump("http://www.greenteapress.com/thinkpython/code/")
    getfile(result)

if __name__ ==  '__main__':
    main()
