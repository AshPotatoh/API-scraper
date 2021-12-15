import json
import time
import requests
from requests.models import Response
import random
import pandas as pd
import csv
import openpyxl


#Pulls JSONs from URLs list and converts into a JSON array, then saves file
#random wait times to avoid rate limiting, remove if no rate limit
def test():
        
    
    with open('info.json', 'a') as f:

        f.write("{ \n")
        f.write('    "info": [ \n')

    URLs = []
    for url in URLs:
        succes = 0

        data = requests.get(url, allow_redirects=False)
        data.headers.update({'Host': 'order.dominos.com',
                            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/93.0',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
                            'Accept-Encoding': 'gzip, deflate',
                            'Connection': 'keep-alive',
                            'Pragma': 'no-cache',
                            'Cache-Control': 'no-cache'})

        #If not a successful connection, waits a random time, and continues down the list
        if data.status_code != 200:
            print(url)
            print(data.status_code)
            waittime = random.randint(2,8)
            print('waiting ' + str(waittime) + " seconds...")
            time.sleep(waittime)
            continue
        #On successful connection saves json into masterfile.    
        jsonOut = data.json()
        with open('info.json', 'a') as f:
            
            if url == URLs[-1]:
                f.write("    ")
                json.dump(jsonOut, f)
                f.write("\n ] \n}")
                f.close
                print("Finished!")
                continue

            f.write("    ")
            json.dump(jsonOut, f)
            f.write(",\n")    

        waitsuc = random.randint(3,6)
        print("Success! Waiting " + str(waitsuc) + " seconds...")
        time.sleep(waitsuc)
        f.close




def convertCsv():

    with open('info.json', encoding="utf-8") as json_file:
        data = json.load(json_file) 

    df = pd.DataFrame(data['info'])

    print(df)


    df.to_excel("info.xlsx", index=False)


test()
convertCsv()

