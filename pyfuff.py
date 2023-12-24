########################
##      IMPORTS       ##
########################

# Literalmente pan con mermelada -> Hacer Hilos y colores

import re
import time
import os, sys
import platform
import requests as rq
from colorama import Fore

#########################
##      VARIABLES      ##
#########################

menu = f"""ᴾʸᵗʰᵒⁿ ᶠᵘᶻᶻⁱⁿᵍ ᵗᵒᵒˡ ᶠᵒʳ ᵈⁱʳᵉᶜᵗᵒʳⁱᵉˢ ᵃⁿᵈ ˢᵘᵇᵐᵃⁱⁿˢ ˡⁱˢᵗⁱⁿᵍ ᵇʸ ʸᵒˢʰˡ :⁾
 {Fore.WHITE}.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |   {Fore.MAGENTA}______     {Fore.WHITE}| || |  {Fore.MAGENTA}____  ____  {Fore.WHITE}| || |  {Fore.MAGENTA}_________   {Fore.WHITE}| || | {Fore.MAGENTA}_____  _____ {Fore.WHITE}| || |  {Fore.MAGENTA}_________   {Fore.WHITE}| || |  {Fore.MAGENTA}_________   {Fore.WHITE}| |
| |  {Fore.MAGENTA}|_   __ \   {Fore.WHITE}| || | {Fore.MAGENTA}|_  _||_  _| {Fore.WHITE}| || | {Fore.MAGENTA}|_   ___  |  {Fore.WHITE}| || |{Fore.MAGENTA}|_   _||_   _|{Fore.WHITE}| || | {Fore.MAGENTA}|_   ___  |  {Fore.WHITE}| || | {Fore.MAGENTA}|_   ___  |  {Fore.WHITE}| |
| |    {Fore.MAGENTA}| |__) |  {Fore.WHITE}| || |   {Fore.MAGENTA}\ \  / /   {Fore.WHITE}| || |   {Fore.MAGENTA}| |_  \_|  {Fore.WHITE}| || |  {Fore.MAGENTA}| |    | |  {Fore.WHITE}| || |   {Fore.MAGENTA}| |_  \_|  {Fore.WHITE}| || |   {Fore.MAGENTA}| |_  \_|  {Fore.WHITE}| |
| |  {Fore.MAGENTA}  |  ___/   {Fore.WHITE}| || | {Fore.MAGENTA}   \ \/ /    {Fore.WHITE}| || | {Fore.MAGENTA}  |  _|      {Fore.WHITE}| || | {Fore.MAGENTA} | '    ' |  {Fore.WHITE}| || | {Fore.MAGENTA}  |  _|      {Fore.WHITE}| || | {Fore.MAGENTA}  |  _|      {Fore.WHITE}| |
| |  {Fore.MAGENTA} _| |_      {Fore.WHITE}| || | {Fore.MAGENTA}   _|  |_    {Fore.WHITE}| || | {Fore.MAGENTA} _| |_       {Fore.WHITE}| || | {Fore.MAGENTA}  \ `--' /   {Fore.WHITE}| || | {Fore.MAGENTA} _| |_       {Fore.WHITE}| || | {Fore.MAGENTA} _| |_       {Fore.WHITE}| |
| |  {Fore.MAGENTA}|_____|     {Fore.WHITE}| || | {Fore.MAGENTA}  |______|   {Fore.WHITE}| || | {Fore.MAGENTA}|_____|      {Fore.WHITE}| || | {Fore.MAGENTA}   `.__.'    {Fore.WHITE}| || | {Fore.MAGENTA}|_____|      {Fore.WHITE}| || | {Fore.MAGENTA}|_____|      {Fore.WHITE}| |
| |  {Fore.MAGENTA}            {Fore.WHITE}| || | {Fore.MAGENTA}             {Fore.WHITE}| || | {Fore.MAGENTA}             {Fore.WHITE}| || | {Fore.MAGENTA}             {Fore.WHITE}| || | {Fore.MAGENTA}             {Fore.WHITE}| || | {Fore.MAGENTA}             {Fore.WHITE}| |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
"""

#########################
##       CLASSES       ##
#########################
class STM():
    def __init__(self, url, status_code):
        self.url = url
        self.st_code = status_code

class STMSuccess(STM):
    def __init__(self, url, status_code, status_type):
        super().__init__(url, status_code)
        self.status_type = status_type

    def identify_method(self):
        self.display_status_dir() if self.status_type == 'dir' else self.display_status_dns()

    def display_status_dir(self):
        print(f"Success - Directory: {self.url} - {self.st_code}")

    def display_status_dns(self):
        print(f"Success - DNS: {self.url} - {self.st_code}")

class STMRedirection(STM):
    def __init__(self, url, status_code, status_type):
        super().__init__(url, status_code)
        self.status_type = status_type

    def identify_method(self):
        self.display_status_dir() if self.status_type == 'dir' else self.display_status_dns()

    def display_status_dir(self):
        print(f"Success - Directory: {self.url} - {self.st_code}")

    def display_status_dns(self):
        print(f"Success - DNS: {self.url} - {self.st_code}")
        
class STMForbidden(STM):
    def __init__(self, url, status_code, status_type):
        super().__init__(url, status_code)
        self.status_type = status_type

    def identify_method(self):
        self.display_status_dir() if self.status_type == 'dir' else self.display_status_dns()

    def display_status_dir(self):
        print(f"Success - Directory: {self.url} - {self.st_code}")

    def display_status_dns(self):
        print(f"Success - DNS: {self.url} - {self.st_code}")    

class STMServerError(STM):
    def __init__(self, url, status_code, status_type):
        super().__init__(url, status_code)
        self.status_type = status_type

    def identify_method(self):
        self.display_status_dir() if self.status_type == 'dir' else self.display_status_dns()

    def display_status_dir(self):
        print(f"Success - Directory: {self.url} - {self.st_code}")

    def display_status_dns(self):
        print(f"Success - DNS: {self.url} - {self.st_code}")

class DIR():
    @staticmethod
    def FUNgetSC():
        if args.avoid != None:
            dir_instance.filterAvoidCode()

        elif args.show != None:
            dir_instance.filterGoodCode()

        else:
            dir_instance.showAllCode()


    def __init__(self, url:str, wordlist:str, timeout:int=5, avoidCode:str='', showCode:str='', Threads:int=None):
        self.url = url
        self.wordlist = wordlist
        self.timeout = timeout
        self.avoidCode = avoidCode
        self.showCode = showCode
        self.Threads = Threads        

    @classmethod
    def make_request(cls, url, directory, timeout):
        return rq.get(url + directory, timeout=timeout)

    @property
    def requests(self):
        return self.make_request(self.url, self.wordlist, self.timeout)
    
    def showAllCode(self):
        for directory in self.wordlist:
            petition = self.make_request(self.url, directory, self.timeout)

            if 200 <= petition.status_code < 300:
                stm_success = STMSuccess(petition.url, petition.status_code, 'dir')
                stm_success.identify_method()

            elif 300 <= petition.status_code < 400:
                stm_success = STMRedirection(petition.url, petition.status_code, 'dir')
                stm_success.identify_method()

            elif 400 <= petition.status_code < 500:
                stm_success = STMForbidden(petition.url, petition.status_code, 'dir')
                stm_success.identify_method()

            elif 500 <= petition.status_code < 600:
                stm_success = STMServerError(petition.url, petition.status_code, 'dir')
                stm_success.identify_method()

    def filterGoodCode(self):
        for directory in self.wordlist:
            petition = self.make_request(self.url, directory, self.timeout)

            if '200' in args.show and 200 <= petition.status_code < 300:
                stm_success = STMSuccess(petition.url, petition.status_code, 'dir')
                stm_success.identify_method()

            elif '300' in args.show and 300 <= petition.status_code < 400:
                stm_success = STMRedirection(petition.url, petition.status_code, 'dir')
                stm_success.identify_method()

            elif '400' in args.show and 400 <= petition.status_code < 500:
                stm_success = STMForbidden(petition.url, petition.status_code, 'dir')
                stm_success.identify_method()

            elif '500' in args.show and 500 <= petition.status_code < 600:
                stm_success = STMServerError(petition.url, petition.status_code, 'dir')
                stm_success.identify_method()

    def filterAvoidCode(self):
        for directory in self.wordlist:
            petition = self.make_request(self.url, directory, self.timeout)

            if '200' not in args.avoid and 200 <= petition.status_code < 300:
                stm_success = STMSuccess(petition.url, petition.status_code, 'dir')
                stm_success.identify_method()

            elif '300' not in args.avoid and 300 <= petition.status_code < 400:
                stm_success = STMRedirection(petition.url, petition.status_code, 'dir')
                stm_success.identify_method()

            elif '400' not in args.avoid and 400 <= petition.status_code < 500:
                stm_success = STMForbidden(petition.url, petition.status_code, 'dir')
                stm_success.identify_method()

            elif '500' not in args.avoid and 500 <= petition.status_code < 600:
                stm_success = STMServerError(petition.url, petition.status_code, 'dir')
                stm_success.identify_method()

    
class DNS():
    @staticmethod
    def FUNgetSC():
        if args.avoid != None:
            dns_instance.filterAvoidCode()

        elif args.show != None:
            dns_instance.filterGoodCode()

        else:
            dns_instance.showAllCode()


    def __init__(self, url:str, wordlist:str, timeout:int=5, avoidCode:str='', showCode:str='', Threads:int=None):
        self.url = url
        self.wordlist = wordlist
        self.timeout = timeout
        self.avoidCode = avoidCode
        self.showCode = showCode
        self.Threads = Threads        

    @classmethod
    def make_request(cls, url, directory, timeout):
        return rq.get(modURL(directory+'.'+url), timeout=timeout)

    @property
    def requests(self):
        return self.make_request(self.url, self.wordlist, self.timeout)
    
    def showAllCode(self):
        for directory in self.wordlist:
            petition = self.make_request(self.url, directory, self.timeout)

            if 200 <= petition.status_code < 300:
                stm_success = STMSuccess(petition.url, petition.status_code, 'dns')
                stm_success.identify_method()

            elif 300 <= petition.status_code < 400:
                stm_success = STMRedirection(petition.url, petition.status_code, 'dns')
                stm_success.identify_method()

            elif 400 <= petition.status_code < 500:
                stm_success = STMForbidden(petition.url, petition.status_code, 'dns')
                stm_success.identify_method()

            elif 500 <= petition.status_code < 600:
                stm_success = STMServerError(petition.url, petition.status_code, 'dns')
                stm_success.identify_method()

    def filterGoodCode(self):
        for directory in self.wordlist:
            petition = self.make_request(self.url, directory, self.timeout)

            if '200' in args.show and 200 <= petition.status_code < 300:
                stm_success = STMSuccess(petition.url, petition.status_code, 'dns')
                stm_success.identify_method()

            elif '300' in args.show and 300 <= petition.status_code < 400:
                stm_success = STMRedirection(petition.url, petition.status_code, 'dns')
                stm_success.identify_method()

            elif '400' in args.show and 400 <= petition.status_code < 500:
                stm_success = STMForbidden(petition.url, petition.status_code, 'dns')
                stm_success.identify_method()

            elif '500' in args.show and 500 <= petition.status_code < 600:
                stm_success = STMServerError(petition.url, petition.status_code, 'dns')
                stm_success.identify_method()

    def filterAvoidCode(self):
        for directory in self.wordlist:
            petition = self.make_request(self.url, directory, self.timeout)

            if '200' not in args.avoid and 200 <= petition.status_code < 300:
                stm_success = STMSuccess(petition.url, petition.status_code, 'dns')
                stm_success.identify_method()

            elif '300' not in args.avoid and 300 <= petition.status_code < 400:
                stm_success = STMRedirection(petition.url, petition.status_code, 'dns')
                stm_success.identify_method()

            elif '400' not in args.avoid and 400 <= petition.status_code < 500:
                stm_success = STMForbidden(petition.url, petition.status_code, 'dns')
                stm_success.identify_method()

            elif '500' not in args.avoid and 500 <= petition.status_code < 600:
                stm_success = STMServerError(petition.url, petition.status_code, 'dns')
                stm_success.identify_method()
#########################
##      FUNCTIONS      ##
#########################

#  COMPLEMENTARY FUNCTIONS  #
#############################
 
def modURL(url:str) -> str:

    ## DETECT IPv4##
    if re.match(r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$', url):
        # Doesn't need http
        pass

    ## DETECT IPv6 ##
    elif re.match(
            re.compile(
                r'^([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|'
                r'([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|'
                r'([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|'
                r'([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|'
                r':((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}'
                r'((25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])|'
                r'([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9])?[0-9])$'
            ),
            url
            ):
        
        url = '['+url+']'

    ## DETECT DOMAIN ##
    else:
        if not "http" in url or not "https" in url:
            url = "http://"+url

    if url[-1] != '/':
        return url+'/'

    return url

def checkWordlist(path:str) -> list:
    if path is None:
        print("Wordlist is not valid.")
        sys.exit()
    
    with open(path, "r") as my_file:
        return [line.strip() for line in my_file.readlines()]

#      MAIN FUNCTIONS       #
#############################
# Desactualizado
def getDNS(url:str, wordlist:list) -> list:
    if checkWordlist(wordlist):
        pass
    else:
        print("Wordlist is not valid.")
        sys.exit()

    foundedDNS = []
    redireccionDNS = []
    forbiddenDNS = []
    servererror = []

    for dns in wordlist:
        petition = rq.get(url+dns)

        if 200 <= petition.status_code < 300:
            foundedDNS.append(dns)
        
        elif 300 <= petition.status_code < 400:
            redireccionDNS.append(dns)

        elif 400 <= petition.status_code < 500:
            forbiddenDNS.append(dns)

        elif 500 <= petition.status_code < 600:
            servererror.append(dir)

    return foundedDNS, forbiddenDNS, servererror


######################################
##      ARGUMENTS CONFIGURATION     ##
######################################

import argparse

parser = argparse.ArgumentParser(description='Help guide for pyfuff')

parser.add_argument('--url', '-u', metavar='URL', type=str, help='URL option', required=True)
parser.add_argument('--wordlist', '-w', metavar="WORDLIST", type=str, help='WORDLIST DIRECTORY', required=True)

parser.add_argument('--timeout', '-t', help='Timeout option', type=int, default=1)
parser.add_argument('--avoid', '-ac', help="Avoid code option", type=str, default=None)
parser.add_argument('--show', '-sc', help="Show code option", type=str, default=None)

parser.add_argument('--dir',  '-d', help='Directory option',  action='store_true')
parser.add_argument('--subd', '-s', help='Subdomains option', action='store_true')


if __name__ == '__main__':
    status_list = [200,300,400,500] # For the output of the avoid option

    def checkOS() -> str:
        return "clear" if platform.system() != 'Windows' else "cls"
    def slowprint(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(1./50)
    def initial(command: str):
        info_menu = f"""
• ------------ • ------------ • ------------ • ------------ •

•• Version              >> Beta
•• URL                  >> {args.url}
•• Method               >> {'Directory scan' if args.dir else 'Subdirectory scan'}
•• Timeout              >> {args.timeout} seconds per request
•• Filter               >> Response status: {str(args.show).replace('0', 'x') if args.show is not None else str([num for num in status_list if num not in (map(int, args.avoid.split(',')) if args.avoid else [])]).split('[')[-1].replace(']','').replace('0','x')}

• ------------ • ------------ • ------------ • ------------ •
        """

#str(args.show).replace('0', 'x') if args.show != None else "2xx, 3xx, 4xx, 5xx"

        os.system(command)
        print(menu)
        print(info_menu)
    ###################################
    ##      ARGUMENTS IMPLEMENT      ##
    ###################################

    args = parser.parse_args()

    if args.dir and args.subd:
        print('Please provide only one of --dir or --subd, not both.')

    elif args.dir:
        initial(checkOS())
        dir_instance = DIR(modURL(args.url), wordlist=checkWordlist(args.wordlist), timeout=args.timeout, avoidCode=getattr(args, 'avoid', ''), showCode=getattr(args, 'show', ''))
        dir_instance.FUNgetSC()

    elif args.subd:
        initial(checkOS())
        dns_instance = DNS(args.url, wordlist=checkWordlist(args.wordlist), timeout=args.timeout, avoidCode=getattr(args, 'avoid', ''), showCode=getattr(args, 'show', ''))
        dns_instance.FUNgetSC()

    else:
        print('No additional option specified for --dir or --subd.')
