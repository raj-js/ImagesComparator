import sys
from comparator import Comparator

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        print('incorrect args')
        sys.exit(0)

    comparator = Comparator()
    degree = comparator.compare(sys.argv[1], sys.argv[2])
    sys.stdout.write(str(degree))
    sys.exit(0)