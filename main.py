import abjad
import random
import sys
from primePy import primes
import time

fn = str()

def make_scale(tone_string):
    voice_1 = abjad.Voice(tone_string, name="Voice_1")
    staff_1 = abjad.Staff([voice_1], name="Staff_1")
    abjad.show(staff_1)

def caesar(a, b, max_range_val):
    x = a + b
    res = random.randrange(1, max_range_val) + x
    return x

def index_to_tone(index):
    match index:
        case 1:
            return "c"

        case 2:
            return "d"
        
        case 3:
            return "e"

        case 4:
            return "f"

        case 5:
            return "g"

        case 6:
            return "a"

        case 7:
            return "b"

def get_note(values):
    values_size = len(values)
    assert values_size == 7
    strincc = str()

    index = 1

    for value in values:
        pure_tone = value % 2 == 0
        sharp_tone = value % 3 == 0
        flat_tone = value % 5 == 0

        tone = index_to_tone(index)

        if pure_tone:
            tone = tone + "'"

        else:
            if sharp_tone:
                tone = tone + "s" + "'"

            else:
                if flat_tone:
                    tone = tone + "f" + "'"

                else:
                    print("tf" + str(value))



        index = index + 1
        strincc = strincc + " " + tone

    #print(strincc)
    return strincc
   
def scramble_list(content_list):
    filename = "scrambled_" + fn + ".txt"
    file = open(filename, "w")

    for x in content_list:
        scrambled_a = random.randrange(1, x)
        scrambled_b = random.randrange(1, scrambled_a)
        file.write(str(scrambled_a) + '\n')
        file.write(str(scrambled_b) + '\n')
        #print(type(x))

    file.close()
    return filename

def parse_file(filename):
    print("opening " + filename)
    time.sleep(2)

    file = open(filename, "r")
    content = file.read()
    content_list = content.split('\n')
    file.close()

    #converted_list = list()

    read_a = 0
    read_b = 0
    read_tuple = tuple()
    amount_read = 0

    read_tuple_list = list()

    for i in content_list:
        if amount_read == 0:
            read_a = int(i)
            amount_read = amount_read + 1

        else:
            if amount_read == 1:
                read_b = int(i)
                amount_read = 0
                read_tuple = (read_a, read_b)
                read_tuple_list.append(read_tuple)

    #print(read_tuple_list)
    return read_tuple_list

def ask_input():
    tuple_list = list()

    for i in range(0, 7):
        print("note " + str(i) + ":")
        entered_a = int(input("a: "))
        entered_b = int(input("b: "))
        entered_tuple = (entered_a, entered_b)
        tuple_list.append(entered_tuple)

    if len(tuple_list) != 0:
        print(tuple_list)
        return tuple_list

    else:
        print("error!")

def val_gen():
    argc = len(sys.argv)
    argv = sys.argv
    res_list = list()
    shift_list = list()
    scale = list()
    index = 0

    if argc == 2:
        fn = argv[1]
        res_list = parse_file(argv[1])

    else:
        res_list = ask_input()

    for(i,j) in res_list:
        seed = random.randrange(1, 100)
        val = caesar(i, j, seed)
        suitable = req_check(val)

        if primes.check(val) or not suitable:
            val = val + 1

        shift_list.append(val)
    
    assert len(shift_list) > 0
    return shift_list

def approach_1():
    argc = len(sys.argv)
    argv = sys.argv
    res_list = list()
    shift_list = list()

    if argc == 2:
        fn = argv[1]
        res_list = parse_file(argv[1])


    else:
        res_list = ask_input()

    print("generating values")
    time.sleep(2)

    for (i,j) in res_list:
        seed = random.randrange(1, 100)
        val = caesar(i, j, seed)
        not_suitable = val % 2 != 0 and val % 3 != 0 and val % 5 != 0
        assert val > 0

        if primes.check(val) or not_suitable:
            val = val + 1

        shift_list.append(val)

    assert len(shift_list) > 0

    print("convert to notes")
    time.sleep(2)
    scale = get_note(shift_list)

    print("generating scale")
    time.sleep(2)
    make_scale(scale)

    scramble_list(shift_list)

def val_to_note(note_before, val):
    shift = 0

    min_sec = val % 2 == 0
    maj_sec = val % 3 == 0

    min_3rd = val % 5 == 0
    maj_3rd = val % 7 == 0

    fourth = val % 11 == 0
    üb_fourth = val % 13 == 0

    dim_5th = val % 17 == 0
    fifth = val % 19 == 0

    min_six = val % 23 == 0
    maj_six = val % 29 == 0

    min_sev = val % 31 == 0
    maj_sev = val % 37 == 0

    octave = val % 41 == 0

    min_nin = val % 43 == 0
    maj_nin = val % 47 == 0 

    if min_sec:
        shift = 1

    elif maj_sec:
        shift = 2

    elif min_3rd:
        shift = 3

    elif maj_3rd:
        shift = 4

    elif fourth:
        shift = 5

    elif üb_fourth:
        shift = 6

    elif dim_5th:
        shift = 7

    elif fifth:
        shift = 8

    elif min_six:
        shift = 9

    elif maj_six:
        shift = 10

    elif min_sev:
        shift = 11

    elif maj_sev:
        shift = 12

    elif octave:
        shift = 13

    elif min_nin:
        shift = 14

    elif maj_nin:
        shift = 15

    else:
        shift = None

    note_val = note_num(note_before)
    assert shift != 0 or shift != None
    shifted_note_val = note_val + shift
    new_note = num_note(shifted_note_val)

    return new_note

def num_note(num):
    match num:
        case 0:
            return "c"

        case 1:
            return "cs"

        case 2:
            return "d"

        case 3:
            return "ds"

        case 4:
            return "e"

        case 5:
            return "f"

        case 6:
            return "fs"

        case 7:
            return "g"

        case 8:
            return "gs"

        case 9:
            return "a"

        case 10:
            return "as"

        case 11:
            return "b"
        
def note_num(note):
    match note:
        case "c":
            return 0

        case "cs":
            return 1

        case "d":
            return 2

        case "ds":
            return 3

        case "e":
            return 4

        case "f":
            return 5

        case "fs":
            return 6

        case "g":
            return 7

        case "gs":
            return 8

        case "a":
            return 9

        case "as":
            return 10

        case "b":
            return 11

def main():
    approach_1()

def req_check(val):
    problems = [
        val % 2 == 0,
        val % 3 == 0,

        val % 5 == 0,
        val % 7 == 0,

        val % 11 == 0,
        val % 13 == 0,

        val % 17 == 0,
        val % 19 == 0,

        val % 23 == 0,
        val % 29 == 0,

        val % 31 == 0,
        val % 37 == 0,

        val % 41 == 0,

        val % 43 == 0,
        val % 47 == 0
    ]

    status = False

    for x in problems:
        status = status or x

    return status
 
if __name__ == "__main__":
    main()