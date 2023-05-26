import os
import urllib.request
from urllib.error import HTTPError

alphabet = 'v'
start = 'z'
end = 'z'

names = []

def main():
    name_creator(alphabet)
    file_checker()
    download()

def name_creator(letter):
    j = ord(start)
    while j <= ord(end):
        if j == ord(':'):
            j += 39
        for i in range(1, 10):
            k = ord('0')
            while k <= ord('z'):
                if k == ord(':'):
                    k += 39
                k += 1
                name = f"{i}{letter}{chr(j)}{chr(k)}"
                names.append(name)
        j += 1

def download():
    for name in names:
        url = f"https://ftp.wwpdb.org/pub/pdb/data/structures/divided/pdb/{name[1:3]}/pdb{name}.ent.gz"
        destination = f"D:\\Protein Database\\{name[1]}\\{name[1:3]}\\pdb{name}.ent.gz"
        
        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        try:
            urllib.request.urlretrieve(url, destination)
            print(f"File {name} has been downloaded successfully.")
        except HTTPError:
            pass

def file_checker():
    c = 0
    while c < len(names):
        temp_file = f"D:\\Protein Database\\{names[c][1]}\\{names[c][1:3]}\\pdb{names[c]}.ent.gz"
        if os.path.exists(temp_file):
            print(f"File {names[c]} already exists.")
            names.pop(c)
            c -= 1
        else:
            c += 1

if __name__ == "__main__":
    main()