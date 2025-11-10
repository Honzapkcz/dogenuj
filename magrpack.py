#!/bin/python
import os
import sys
import subprocess
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


def modpack_get():
    if not os.path.exists(".VERSION"):
        return "Žádný"
    with open(".VERSION", "r") as f:
        return f.readline(), f.readline()


def modpack_set(modid, version):
    with open(".VERSION", "w") as f:
        f.write(modid+"\n")
        f.write(version+"\n")


def download(url, folder, i, count, partzip=False):
    file = os.path.basename(url)
    if partzip:
        file = ".part.zip"
    print(f"[{folder}] [{i} / {count}] Stahuji {os.path.basename(url)}")
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


def install(spec):
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
    modpack_set(spec["id"]+"\n"+spec["version"])
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


def packinfo(modid):
    print("Stahuji modpack info...")
    spec = requests.get(upstream+"spec/"+modid+".json", headers=useragent).json()  # noqa: E501
    while True:
        info = f"""{spec["name"]}
- {spec["author"]} [{spec["version"]}]
- {spec["loader"]} [{spec["website"]}]
{spec["description"]}"""
        if not dialog_yesno("MAGRPACK - Informace", info, ["--defaultno" "--no-label" "Zpátky" "--yes-label", "Instalovat"]):
            return
        if modpack_get() != "Žádný":
            if not dialog_yesno("MAGRPACK - Instalace", "Detekován modpack. Ve složce máte módy, které mohou narušit fungování modpacku. Přejete si přesto pokračovat? (Instalátor nebude pokoušet přepisovat soubory)", ["--defaultno"]):  # noqa: E501
                continue
        install(spec)
        return


def selectpack():
    print("Stahuji seznam modpacků...")
    seznam = requests.get(upstream+"packlist.txt", headers=useragent).text.splitlines()  # noqa: E501
    while True:
        ok, tag = dialog_menu("MAGRPACK - Instalace", "Vyberte modpack: ", seznam, ["--cancel-label", "Zpátky", "--ok-label", "Info"])
        if not ok:
            return
        packinfo(seznam[int(tag)])


def dialog_dialog(args):
    dialog = "./dialog" if os.name == "posix" else "dialog.exe"
    childr, childw = os.pipe()
    pid = os.fork()
    if pid == 0:  # child
        try:
            os.close(childr)  # dont need reading
            os.dup2(childw, 2)  # pipe stderr to parent
            os.execve(dialog, args, {})
        except Exception as e:
            print(e)
            os._exit(127)
        os._exit(126)  # should not happen
    # parent
    os.close(childw)  # dont need writing
    with os.fdopen(childr, "r") as f:
        output = f.read()
    retinfo = os.waitpid(pid, 0)[1]
    if os.WIFEXITED(retinfo):
        exitcode = os.WEXITSTATUS(retinfo)
    else:
        exitcode = 127
    return exitcode, output


def dialog_menu(title, text, tagitem, options=[]):
    args = ["--no-lines", "--no-tags", "--cr-wrap", "--title", title, *options, "--menu", text, "0", "0", "0"]
    for k in tagitem:
        args.append(str(k))
        args.append(str(tagitem[k]))
    ret, out = dialog_dialog(args)
    return ret == 0, out.rstrip("\r\n\t ")


def dialog_yesno(title, text, options=""):
    args = ["--no-lines", "--cr-wrap", "--title", title, *options, "--yesno", text, "0", "0"]  # noqa: E501
    ret, _ = dialog_dialog(args)
    return ret == 0


def diagnose():
    modcount = 0
    if os.path.isdir("mods"):
        for thing in os.listdir("mods"):
            if thing.endswith(".jar"):
                modcount += 1
    print("\033[32mVerze Skriptu: \033[0m"+str(version))
    print("\033[32mDetekovaný Modpack: \033[0m"+str(modpack))
    print("\033[32mInstalační Cesta: \033[0m"+str(os.getcwd()))
    print("\033[32mPočet modů v mods složce: \033[0m"+str(modcount))
    print("\033[32mUpstream: \033[0m"+str(upstream))
    print("")

# path bootstrap


version = "KUJNUJ 3.0.0"
useragent = {"User-Agent": "Kujnuj/3.0.0 (honzapkcz)"}
upstream = "https://hbmy.eu/modpack/"


def bootstrap_move(path):
    print("Přesouvám do: "+path)
    os.rename(sys.argv[0], os.path.normpath(path+"/magrpack.py"))
    os.chdir(os.path.normpath(path+"/magrpack.py"))
    with open(".magrpack", "w") as f:
        f.write("{}\n")
    print("OK Přesunuto.")


def bootstrap_1():
    if os.path.exists(".magrpack"):
        print("Soubor .magrpack nalezen, přeskakuji setup.")
    elif os.getcwd().find(".minecraft") != -1:
        print("Instalátor je v minecraft složce, přeskakuji setup.")
        return

    print("Instalátor není v .minecraft složce!")
    mcpath = ""
    if os.name == "posix" and os.path.isdir(os.path.expanduser("~/.minecraft")):  # noqa: E501
        mcpath = os.path.expanduser("~/.minecraft")
    if os.name == "posix" and os.path.isdir(os.path.expanduser("~/Library/Application Support/minecraft")):  # noqa: E501
        mcpath = os.path.expanduser("~/Library/Application Support/minecraft")
    if os.name == "nt" and os.path.isdir(os.path.expandvars("%appdata%/.minecraft")):  # noqa: E501
        mcpath = os.path.expandvars("%appdata%/.minecraft")

    if mcpath == "":
        print("Instalátor nenašel .minecraft složku.")
    else:
        print("Instalátor našel .minecraft složku: "+mcpath)
    print("Chcete nechat instalátor v této složce [n], přesunout ho [p] nebo zadat jinou .minecraft cestu [z]?")  # noqa: E501
    usin = ""
    while not usin.lower() in ["n", "p", "z"]:
        usin = input("[n/p/z] ")
        if usin.lower() == "p" and mcpath == "":
            usin = "z"
    if usin == "n":
        print("OK Nechávám.")
        with open(".magrpack", "w") as f:
            f.write("{}\n")
    elif usin == "z":
        print("Napište cestu vaší minecraft složky: ")
        while True:
            mcpath = os.path.expanduser(os.path.expandvars(input("[kam?] ")))
            if os.path.isdir(mcpath):
                break
            print("Složka neexistuje!")
        bootstrap_move(mcpath)
    elif usin == "p":
        bootstrap_move(mcpath)

# dialog bootstrap


bootstrap_1()

if os.name == "posix" and not os.path.exists("dialog"):
    print("Dialog nenalezen, stahuji...")
    download(upstream+"dialog", ".", 1, 1)
if os.name == "nt" and not os.path.exists("dialog.exe"):
    print("Dialog.exe nenalezen, stahuji...")
    download(upstream+"dialog.exe", ".", 1, 1)

print("Bootstrap dokončen.")

spec = False  # requests.get(upstream+"kujnuj.json", headers=useragent).json()
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


while True:
    ok, tag = dialog_menu("MAGRPACK", "Nainstalovaný Modpack: "+modpack+"\nDostupné akce: ", {
        "i": "Instalovat Modpack",
        "r": "Odstranit modpack",
        "d": "Diagnostika",
        "x": "Odejít"
    }, ["--no-cancel"])  # noqa: E501

    if tag == "i":
        selectpack()
    elif tag == "r":
        uninstall()
    elif tag == "d":
        diagnose()
    elif tag == "x":
        print("\033[32m[Konec]\033[0m")
        break
