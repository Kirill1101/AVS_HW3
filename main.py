import sys
import time

from extender import *

start_time = time.time()
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("incorrect command line!\n"
              "  Waited:\n"
              "     command -f infile outfile01 outfile02\n"
              "  Or:\n"
              "     command -n number outfile01 outfile02\n")
        exit(1)

    print('==> Start')

    container = Container()

    if sys.argv[1] == "-f":
        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
        ifile = open(sys.argv[2])
        str = ifile.read()
        ifile.close()
        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        strArray = str.replace("\n", " ").split(" ")
        ReadStrArray(container, strArray)
    elif sys.argv[1] == "-n":
        size = int(sys.argv[2])
        if (size < 1) or (size > 10000):
            print("Incorrect number\n")
            exit(2)
        InRnd(container, size)

    ofile = open(sys.argv[3], 'w')
    container.Write(ofile)
    ofile.close()

    ofile = open(sys.argv[4], 'w')
    ofile.write("Average: {}\n".format(container.Shift()))
    container.Write(ofile)
    ofile.close()

    print('==> Finish')
    print("Program execution time in milliseconds:", (time.time() - start_time) * 1000)
