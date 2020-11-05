# {firstname}_{lastname}_cg1_ex{#}.zip
import os
import re
import shutil


def do(firstName, lastName, path):
    directory_contents = os.listdir(path)
    for item in directory_contents:
        if os.path.isdir(item) and re.match("^(cg)\d+_{1}(exercise)_{1}\d{2}", item):
            try:
                currentPath = "src/"
                outputFilename = firstName + "_" + lastName + "_cg1_ex" + item.split("_")[-1]
                shutil.make_archive(outputFilename, 'zip', path + "/" + item + "/skeleton", currentPath)
            except:
                print("An exception occurred")


if __name__ == '__main__':
    do(firstName="Max", lastName="Mustermann", path="../../WebstormProjects/CG1")
