from getpass import getuser
from decoders import fromgzip, frombase64, xor
import sys


def file_load(path):
    with open(path, mode="rb") as file:
        bfile = file.read()
    return fromgzip(frombase64(xor(bfile)))


def main(path):
    string = file_load(path)
    i = string.rfind("<k>GJA_002</k><s>") + 17
    j = 1
    while string[i + j] != "<":
        j += 1
    print("Password:", string[i: i + j])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        save_path = sys.argv[1]
    else:
        save_path = f"C:\\Users\\{getuser()}\\AppData\\Local\\GeometryDash\\CCGameManager.dat"
    main(save_path)
    input()
