# Functions to write an ini file given paramters
from collections import defaultdict

# Have to write numbers instead of strings for some values
NUMBER_FIELDS = ["bpm"]

def get_param_dict(params):
    d = defaultdict(dict)
    for key, val in params.iteritems():
        if key.startswith('input-'):
            continue
        parts = key.split('-')
        if len(parts) == 3: # movement-level param
            _, movement_num, param_name = parts
            d[movement_num][param_name] = val
        elif len(parts) == 5: # section-level param
            _, movement_num, _, section_num, param_name = parts
            if "sections" not in d[movement_num]:
                d[movement_num]["sections"] = defaultdict(
                    lambda: defaultdict(dict))
            d[movement_num]["sections"][section_num][param_name] = val
        else:
            print "Can't parse key {}".format(key)
    return d


def add_movement_params(movement, movement_id, lines):
    lines.append("movement settings")
    lines.append("movementId: {}".format(movement_id))
    lines.append("movementDuration: {}".format(movement["movementDuration"]))
    lines.append("")
    lines.append("#WB Levers")
    movement["rhythmSpeed"] = "medium"
    for key in ["mood", "rhythmSpeed", "complexity"]:
        lines.append("{}: {}".format(key, movement[key]))
    lines.append("")

   
def get_section_line(section, section_id):
    line = ["section:  id:{}".format(section_id)]
    for key in ["tse", "bpm", "energy", "durationInMeasures",
                "slope", "direction"]:
        if key in NUMBER_FIELDS:
            line.append("{}:{}".format(key, section[key]))
        else:
            line.append("{}:'{}'".format(key, section[key]))
    return ', '.join(line)


def add_section_params(movement, lines):
    lines.append("#section settings")
    for i in xrange(len(movement['sections'])):
        line = get_section_line(movement['sections'][str(i)], i)
        lines.append(line)
    lines.append("")
                    

def get_ini(params):
    d = get_param_dict(params)
    num_movements = len(d)
    lines = [
        "#composition settings",
        "numMovements: {}".format(num_movements),
        ""
    ]
    for i in xrange(num_movements):
        add_movement_params(d[str(i)], i, lines)
        add_section_params(d[str(i)], lines)
        lines.append("#end movement")
    return '\n'.join(lines)  

