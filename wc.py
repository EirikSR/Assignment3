import sys
import os


def split(word):
    return [c for c in word]


def get_file_info(name, type_):
    with open(name + "." + type_, "r") as f:
        line = f.readline()
        line_cnt = 1
        word_cnt = 0
        char_cnt = 0
        while line:
            # print("--" + line + "--")
            line = f.readline()
            line_strip = line.strip()
            string_length = len(line_strip.split())
            # print(string_length)
            char_length = len(split(line))
            line_cnt += 1
            word_cnt += string_length
            char_cnt += char_length

    print([line_cnt, word_cnt, char_cnt, name + "." + type_])


file_name = sys.argv[1]

if split(file_name)[0] == "*":
    file_lst = os.listdir("C:/Users/Eirik/In3110/Assignment3/Assignment3/")

    try:
        c = split(file_name)[1]
        if c == ".":

            type_target = file_name.split(".")[1]

            if split(file_)[0] != ".":  # Avoids files such as .gitignore
                name, type_ = file_.split(".")
                if type_ == type_target:
                    get_file_info(name, type_)

        else:
            print("Error, no file format found after *")
    except:
        for file_ in file_lst:
            if split(file_)[0] != ".":  # Avoids files such as .gitignore
                name, type_ = file_.split(".")
                get_file_info(name, type_)

# get_file_info("b", "py")
# ret = get_file_info("*.txt")
# print(ret)
