from lxml import html
import requests
from time import sleep
from colorama import init
from colorama import Fore
init()

print(Fore.GREEN+'  __  __          _____ _      _____ ______ _   _') 
print(Fore.GREEN+' |  \/  |   /\   |_   _| |    / ____|  ____| \ | |')
print(Fore.GREEN+' | \  / |  /  \    | | | |   | |  __| |__  |  \| |')
print(Fore.GREEN+' | |\/| | / /\ \   | | | |   | | |_ |  __| | . ` |')
print(Fore.GREEN+' | |  | |/ ____ \ _| |_| |___| |__| | |____| |\  |')
print(Fore.GREEN+' |_|  |_/_/    \_\_____|______\_____|______|_| \_|')
print(Fore.GREEN+'===================================================')
print('')

number = input(Fore.GREEN+'How many emails do you need ?\n')                   
url = 'http://generator.email/'

f = open("emails.txt","w+")

def getEmail(url):
    page = ''
    while page == '':
        try:
            page = requests.get(url)
            tree = html.fromstring(page.content)
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            print("ZZzzzz...")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue
    email = tree.xpath('//span[@id="email_ch_text"]/text()')
    return email

for x in range(0,number):
    mail = getEmail(url)
    f.write(str(mail)[2:-2]+"\n")
    print(str(mail)+" successfully created !")
print("Done !")
f.close()


