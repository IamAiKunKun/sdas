import os
import re

dir_lists = []


def search_dir(path, keyword):
    dir_names = os.listdir(path)
    for name in dir_names:
        sub_path = path + os.sep + name
        if keyword in name:
            # print(sub_path)
            dir_lists.append(sub_path)

        if os.path.isdir(sub_path):
            search_dir(sub_path, keyword)


if __name__ == '__main__':
    search_dir(os.getcwd(), '.git')
    for dirname in dir_lists:
        if ".wiki.git" in dirname:
            continue

        try:
            with open(dirname + '/config', 'r') as f2:
                filec = f2.read()

                match = re.findall(r'fullpath = (.*)', filec)

            if len(match) > 0:
                print(dirname + "   |   " + match[0])

        except:
            pass