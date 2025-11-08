#!/bin/python
import os
import requests
from shutil import rmtree
import zipfile

print("\033[32m█| █|█|  █|    █|█|  █|█|  █|    █|\033[0m")
print("\033[32m█|█| █|  █|    █|██| █|█|  █|    █|\033[0m")
print("\033[32m██|  █|  █|    █|█|█|█|█|  █|    █|\033[0m")
print("\033[32m█|█| █|  █|█|  █|█| ██|█|  █|█|  █|\033[0m")
print("\033[32m█| █|█████|█████|█|  █|█████|█████|\033[0m")
print("\033[32mMinecraft Kujnuj instalační skript \033[0m")
print("")

# TODO: modpack.json

version = "KUJNUJ 3.0.0"
useragent = {"User-Agent": "Kujnuj/3.0.0 (honzapkcz)"}
upstream = "https://hbmy.eu/modpack/"

cwd = os.getcwd()
newest = requests.get(upstream+"latest.txt", headers=useragent).text.splitlines()[0]
spec = requests.get(upstream+"kujnuj.json", headers=useragent).json()
modpack = "Žádný"
modcount = 0
if os.path.isdir("mods"):
    for thing in os.listdir("mods"):
        if thing.endswith(".jar"):
            modcount += 1
if os.path.exists(".VERSION"):
    f = open(".VERSION", "r")
    modpack = f.readline()
    f.close()
elif os.path.exists("INSTALACE.txt"):
    modpack = "KUJNUJ Manuální Instalace"
elif modcount > 0:
    modpack = "Neznámý"


def download(url, folder, i, count, partzip=False):
    file = os.path.basename(url)
    if partzip:
        file = ".part.zip"
    infostr = f"[{folder}] [{i} / {count}]"
    print(f"{infostr} Stahuji {os.path.basename(url)}")
    r = requests.get(url, headers=useragent)
    with open(file, "wb") as f:
        for chunk in r.iter_content(chunk_size=65535):
            f.write(chunk)


def fetch(array, folder):
    print(f"Otevírám složku {folder}")
    if not os.path.isdir(folder):
        os.mkdir(folder)
    oldpath = os.getcwd()
    os.chdir(folder)
    i = 1
    for item in array:
        file = os.path.basename(item)
        if os.path.exists(file):
            print(f"[{i} / {len(array)}] Přeskakuji {file}")
        else:
            download(item, folder, i, len(array))
        i += 1
    print(f"Opouštím složku {folder}")
    os.chdir(oldpath)


def extract(webpath, folder):
    download(webpath, folder, 1, 1, True)
    print(f"Rozbaluji do {folder}")
    # TODO
    if not zipfile.is_zipfile(".part.zip"):
        print(f"\033[31mSoubor {webpath} není zip soubor!\033[0m")
        os.remove(".part.zip")
        return
    with zipfile.ZipFile(".part.zip") as f:
        f.extractall(folder)
    os.remove(".part.zip")


def install():
    global modpack
    if modpack != "Žádný":
        print("\033[31mDetekován modpack. Ve složce máte módy, které mohou narušit fungování modpacku.\033[0m")
        print("\033[31mPřejete si přesto pokračovat? (Instalátor nebude pokoušet přepisovat soubory)\033[0m")
        yesno = input("[ano|ne] ")
        if yesno != "ano":
            print("Nic neprovedeno")
            return

    # TODO: os.path.splitroot
    if "extract" in spec:
        for k in spec["extract"]:
            extract(spec["extract"][k], k)
    if "fetch" in spec:
        for k in spec["fetch"]:
            extract(spec["fetch"][k], k)

    print("Vytvářím .VERSION soubor")
    with open(".VERSION", "w") as f:
        f.write(version)
        f.write("\n")
    modpack = version
    print(f"\033[32mModpack {version} úspěšně nainstalován!\033[0m")


def uninstall():
    global modpack
    print("\033[31mTato akce nejde vrátit zpět!\033[0m")
    print("\033[31mOpravdu si přejete nadobro vymazat všechny módy?\033[0m")
    if input("[ano|ne] ") == "ano":
        print("Maži mods")
        rmtree("mods")
        os.mkdir("mods")
        print("\033[31mChcete vymazat i configy?\033[0m")
        if input("[ano|ne] ") == "ano":
            print("Maži config")
            rmtree("config")
            os.mkdir("config")
            os.remove("options.txt")
        print("Maži verze soubor")
        if os.path.exists("INSTALACE.txt"):
            os.remove("INSTALACE.txt")
        if os.path.exists(".VERSION"):
            os.remove(".VERSION")
        modpack = "Žádný"
        print("Úspěšně vymazáno")
    else:
        print("Nic neprovedeno")


def diagnose():
    modcount = 0
    if os.path.isdir("mods"):
        for thing in os.listdir("mods"):
            if thing.endswith(".jar"):
                modcount += 1
    print("\033[32mVerze Skriptu: \033[0m"+str(version))
    print("\033[32mDetekovaný Modpack: \033[0m"+str(modpack))
    print("\033[32mNejnovější Verze: \033[0m"+str(newest))
    print("\033[32mInstalační Cesta: \033[0m"+str(cwd))
    print("\033[32mPočet modů v mods složce: \033[0m"+str(modcount))
    print("\033[32mPočet modů v modpacku: \033[0m"+str(len(mods)))
    print("\033[32mUpstream: \033[0m"+str(upstream))
    print("")
    # TODO
    if cwd != "*.minecraft":
        print("\033[31mTato složka není '.minecraft', ujistěte se, že jste skript opravdu spustili v minecraft složce\033[0m")

    if modpack != "Žádný":
        print("\033[31mDetekován modpack. Při instalaci je nutno tuto verzi nejprve odinstalovat.\033[0m")

    if version != newest:
        print("\033[32mDostupná nová verze \033[0m"+str(newest))


diagnose()
while True:
    print("")
    print("Dostupné akce:")
    print("    1 - Nainstalovat Modpack")
    print("    2 - Odinstalovat/Vyčistit Modpack")
    print("    3 - Diagnostika")
    print("    4 - Odejít")
    print("")
    usin = input("[Akce] ")
    print("")

    if usin == "1":
        install()
    elif usin == "2":
        uninstall()
    elif usin == "3":
        diagnose()
    elif usin == "4":
        print("\033[32m[Konec]\033[0m")
        break
