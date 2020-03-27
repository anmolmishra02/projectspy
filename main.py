from plyer import notification
import requests
import time
from bs4 import BeautifulSoup

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon='D:/New folder/iconc.ico',
        timeout=20
    )

def getdata(url):
    r=requests.get(url)
    return r.text
if __name__=="__main__":
    while True:
        # notifyMe("anmol","lets stop corona")
        myhtmldata=getdata('https://www.mohfw.gov.in/')
        # print(myhtmldata)
        soup=BeautifulSoup(myhtmldata,'html.parser')
        # print(soup.prettify())
        mystr=""
        for tr in soup.find_all('tbody')[-1].find_all('tr'):
            mystr+=tr.get_text()
        mystr=mystr[1:]
        itemlist=mystr.split("\n\n")
        states=['Delhi','Chandigarh','Gujrat','Haryana','Punjab','Kerala']
        for item in itemlist[0:22]:
            datalist= item.split('\n')
            if datalist[1] in states:
                print(datalist)
                ntitle='Cases of Covid-19'
                ntext=f"STATE :{datalist[1]}\n Indian :{datalist[2]}  Foreign :{datalist[3]} \n cured :{datalist[4]}\n deaths :{datalist[5]}"
                notifyMe(ntitle,ntext)
                time.sleep(3)
        time.sleep(3600)
