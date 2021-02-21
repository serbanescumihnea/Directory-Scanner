import requests


print("Directory Scanner\nVersion: 0.1\nAuthor:Serbanescu Mihnea\n");



inputFile = input("Enter dictionary... ")
inputUrl = input("Enter url you want to scan... ")




file = open(inputFile,"r")
count = 0
while True:
    line = file.readline().split('\n')
    if count>=15:
        madeUrl = inputUrl + str(line[0])
        requestUrl = requests.get(madeUrl)
        if requestUrl.status_code == 200:
            print("Url found -> ", madeUrl)       
        else:
            print("Url ",madeUrl," cannot be accessed!")
        
        if not line:
            break
    count = count + 1
file.close()
