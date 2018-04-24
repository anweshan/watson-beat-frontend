import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ini", help="ini file name")
ap.add_argument("-m", "--mood", help="ini mood")
ap.add_argument("-p", "--root", default="/media/whi-gpu01/fd2bf426-d2ee-4129-8a76-35c8216ac3a3/music/", help="root file path")
args = vars(ap.parse_args())

def find_ini(ini=None, mood=None, root="/media/whi-gpu01/fd2bf426-d2ee-4129-8a76-35c8216ac3a3/music/"):
    if ini==None and mood==None:
        print("No ini or mood selected. Use Space.ini")
        ini_path = root + "Ini/Space.ini"
    elif ini==None:
        print("User selected mood")
        ini_path = root + "Ini/" + mood + ".ini"
    else:
        print("User selected ini")
        ini_path = root + "Ini/" + ini + ".ini"
    return ini_path

if __name__=='__main__':
    ini_path = find_ini(args["ini"], args["mood"], args["root"])
    print(ini_path)