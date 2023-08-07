global url,inputName, csrfName, status
url,inputName,csrfName,status="","","",""
def set(URL,input,csrf):
    global url,inputName,csrfName
    url=URL
    inputName=input
    csrfName=csrf
def seturl(URL):
    global url
    url=URL
def setinput(input):
    global inputName
    inputName=input
def setcsrf(csrf):
    global csrfName
    csrfName=csrf
def check(gstin):
    import requests
    from bs4 import BeautifulSoup
    global url,inputName,csrfName
    if (url==""):
        url="https://www.knowyourgst.com/gst-number-search/"
    if (inputName==""):
        inputName="gstnum"
    if (csrfName==""):
        csrfName="csrfmiddlewaretoken"
    client=requests.session()
    global status
    status=""
    client.get(url)
    if(client.get(url).status_code!=200):
        status+="[GET URL Failure]"
    if 'csrftoken' in client.cookies:
        csrftoken = client.cookies['csrftoken']
    else:
        csrftoken = client.cookies['csrf']
    data={inputName:gstin,csrfName:csrftoken}
    r = client.post(url,data=data,headers=dict(Referer=url))
    if (r.content):
        pass
    else:
        status+="[Content retrival failure]"
    try:
        soup=BeautifulSoup(r.text,'html.parser')
        table=soup.find('table',class_="striped highlight questionlist").find_all('tr')
        data=[]
        for tr in table:
            data.append([td.text for td in tr.find_all('td')])
        reqData=[]
        for i in range(len(data)):
                tempList=data[i]
                reqData.append(tempList[1])
        global name,pan,person,type,add,nature,date
        name = str(reqData[0])
        pan=str(reqData[1])
        person=str(reqData[2])
        type=str(reqData[4])
        add=str(reqData[6].split(",")[0])
        date=str(reqData[8].split("T")[0])
        nature=str(reqData[7].split("],")[1])
        status+="[No Errors]"
    except:
        status+="[Parsing Failure]"
def disp(input):
    print(input)
def printall():
    print(name,pan,person,type,add,nature,date)
def printwith(spacer):
    print(name,spacer,pan,spacer,person,spacer,type,spacer,add,spacer,nature,spacer,date)
def checkstatus():
    global status
    if (status==""):
        status+="[Offline]"
        print("g")
    else:
        print("g")
