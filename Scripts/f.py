import requests as rq

class DIR():
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

    def FUNshowCode(self):
        for directory in map(str.strip, open(self.wordlist, "r").readlines()):
            petition = self.make_request(self.url, directory, self.timeout)

            if '200' in self.showCode and 200 <= petition.status_code < 300 or '200' not in self.avoidCode and 200 <= petition.status_code < 300:
                self.display_status('dir', petition)

            elif '300' in self.showCode and 300 <= petition.status_code < 400 or '300' not in self.avoidCode and 300 <= petition.status_code < 400:
                self.display_status('dir', petition)

            elif '400' in self.showCode and 400 <= petition.status_code < 500 or '400' not in self.avoidCode and 400 <= petition.status_code < 500:
                self.display_status('dir', petition)

            elif '500' in self.showCode and 500 <= petition.status_code < 600 or '500' not in self.avoidCode and 500 <= petition.status_code < 600:
                self.display_status('dir', petition)

    @staticmethod
    def display_status(status_type, petition):
        if status_type == 'dir':
            STMSuccess.display_status_dir(STMSuccess(url=petition.url, status_code=petition.status_code))
        elif status_type == 'dns':
            STMSuccess.display_status_dns(STMSuccess(url=petition.url, status_code=petition.status_code))
        else:
            # Manejar otro tipo de estado si es necesario
            pass

# Uso del método FUNshowCode
dir_instance = DIR(url="tu_url", wordlist="tu_wordlist")
dir_instance.FUNshowCode()
