import os

def checkWordlist(dir_path: str) -> bool:
    if dir_path is None:
        return False
    return os.path.exists(dir_path)

def getDirs(url: str, wordlist: str = None):
    if checkWordlist(wordlist):
        # Realiza las acciones relacionadas con la lista de palabras (wordlist)
        print('a')
    else:
        print("Wordlist is not valid.")
        return

# Ejemplo de uso:
getDirs("https://example.com", wordlist="a.py")
