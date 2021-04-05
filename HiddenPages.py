import requests
import time

URL = input("\nEnter URL:-> ")
ulist = input("Enter the URLlist's file path:-> ")
ask_src = input("Do you want source code to be enabled? (y/n):-> ")
if ask_src in ['Yes', 'yes', 'Y', 'y']:
    src = True
else:
    src = False

for line in open('{}'.format(ulist)):
    page = line.strip()
    full_url = URL + '/' + page
    try:
        responce = requests.get(full_url)
    except:
        print("\nOops, something went wrong.\n")

    print('~~~~~~~~~~', page, '~~~~~~~~~~')

    if responce:
        if src == True:
            print(responce.text)
        print("[+] URL FOUND:", responce.url)

        pause = input("\nPress enter to keep crawling, otherwise type exit:-> ")
        if pause == 'exit':
            exit()


while True:
    chunk = page
    if chunk == 'dir-prop-base':
        print("\nSession finished!")
        exit()
