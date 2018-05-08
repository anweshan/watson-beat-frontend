import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-c", "--complexity", default="super_simple", help="super_simple, simple, semi_complex")
ap.add_argument("-st", "--section", default=0,help="section")
ap.add_argument("-t", "--tse", default='4/4',help="time signature")
ap.add_argument("-b", "--bpm", default='100',help="bpm")
ap.add_argument("-e", "--energy", default='low',help="energy")
ap.add_argument("-du", "--duration", default='10 to 20 seconds',help="min and max number of seconds per section")
ap.add_argument("-dm", "--durationInMeasures", default='4',help="number of measures per section")
ap.add_argument("-sl", "--slope", default='stay',help="stay, gradual, steep")
ap.add_argument("-di", "--direction", default='up',help="up, down")
ap.add_argument("-n", "--name", default='Custom.ini',help="Ini name")
ap.add_argument("-p", "--root", default="/media/whi-gpu01/fd2bf426-d2ee-4129-8a76-35c8216ac3a3/music/src/Ini", help="root file path")
args = vars(ap.parse_args())

def construct_ini(complexity, section, tse, bpm, energy, duration,
                  durationInMeasures, slope, direction, name, root):
    ini_file = open(root + name,"w")
    ini_file.write("numMovements: 1 \n")
    ini_file.write("\n")
    ini_file.write("movementId: 0 \n")
    ini_file.write("movementDuration: " + duration + "\n")
    ini_file.write("\n")
    ini_file.write("mood: " + name[0:-4] + "\n")
    ini_file.write("rhythmSpeed: " + "medium \n")
    ini_file.write("complexity: " + complexity + "\n")
    ini_file.write("\n")
    ini_file.write("section: id:0, tse:\'" + tse + "\', bpm:" + bpm +
                   ", energy:\'" + energy + "\', durationInMeasures:\'" +
                   durationInMeasures + "\', slope:\'" + slope + "\', direction:\'" + direction + "\'\n")
    ini_file.close()

if __name__=='__main__':
    ini_file = construct_ini(args["complexity"], args["section"], args["tse"], args["bpm"],
                             args["energy"], args["duration"], args["durationInMeasures"],
                             args["slope"], args["direction"], args["name"], "./")
    file = open(args["name"], "r")
    print file.read()