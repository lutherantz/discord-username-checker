
import os
import fade
import string
import random
import requests
from colorama import Fore

class Checker:
    def __init__(self):
        if os.path.exists("proxies.txt"):
            self.proxy = f"{Fore.LIGHTGREEN_EX}Enable"
        else:
            self.proxy = f"{Fore.LIGHTRED_EX}Disable"
        self.banner = """
                               ___  _                     __  _______           __          
                              / _ \(_)__ _______  _______/ / / ___/ /  ___ ____/ /_____ ____
                             / // / (_-</ __/ _ \/ __/ _  / / /__/ _ \/ -_) __/  '_/ -_) __/
                            /____/_/___/\__/\___/_/  \_,_/  \___/_//_/\__/\__/_/\_\\\__/_/"""
        self.banner = fade.pinkred(self.banner)
        detext =f"""                                                🚀  {Fore.WHITE}FREE & OPEN SOURCE  🚀"""
        menu = f"                                                   {Fore.LIGHTMAGENTA_EX}[ {Fore.WHITE}Proxy {Fore.LIGHTMAGENTA_EX}] {Fore.WHITE}> {self.proxy}"
        print(self.banner + "\n" + detext + "\n" + menu)

        length = int(input(f"{Fore.MAGENTA}╭──{Fore.WHITE}[{Fore.MAGENTA}Username Length{Fore.WHITE}]\n{Fore.MAGENTA}╰──────$ {Fore.RESET}"))
        if length <= 0:
            print("                                         La longueur doit être supérieure à zéro.")
            exit()

        while True:
            random_username = str(''.join(random.choices(string.ascii_letters + string.digits, k=length)))
            self.check(random_username)

    def check(self, username):
        url = "https://discord.com/api/v9/unique-username/username-attempt-unauthed"
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Content-Type": "application/json",
            "Origin": "https://discord.com",
            "Referer": "https://discord.com/register?email=staymfe%40gmail.com",
            "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": self.useragents(),
            "X-Debug-Options": "bugReporterEnabled",
            "X-Discord-Locale": "fr",
            "X-Discord-Timezone": "Europe/Paris",
        }

        payload = {
            "username": username
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                if "taken" in data and data["taken"]:
                    print(f"{Fore.LIGHTMAGENTA_EX}Username{Fore.WHITE}: '{Fore.LIGHTRED_EX}{username}{Fore.WHITE}' is {Fore.LIGHTRED_EX}taken")
                else:
                    print(f"{Fore.LIGHTMAGENTA_EX}Username{Fore.WHITE}: '{Fore.LIGHTGREEN_EX}{username}{Fore.WHITE}' is {Fore.LIGHTGREEN_EX}not taken")
            else:
                print(f"{Fore.LIGHTRED_EX}Requests Error :", response.status_code)
        except Exception:
            print(f"{Fore.LIGHTRED_EX}Requests Error :", response.status_code)

    def useragents(self):
        url = "https://api.apilayer.com/user_agent/generate?desktop=true&windows=true"
        headers = {
            "apikey": "hFWHtCwAyG8Vr6evPGnBF83Wks6ocfZw"
        }

        response = requests.get(
            url = url,
            headers = headers
            )

        return response.json()["ua"]

if __name__ == "__main__":
    checker = Checker()