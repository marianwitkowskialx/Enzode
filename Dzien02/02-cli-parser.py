
# Parsowanie linii poleceń skryptu
import sys
from argparse import ArgumentParser

#print(sys.argv)
parser = ArgumentParser()
parser.add_argument("-n", "--name", required=True, help="nazwa pliku", metavar="FILENAME")
parser.add_argument("-d", type=int, default=5, help="liczba sekund", metavar="SECONDS")
parser.add_argument("-f", "--folder", nargs="+", default=".", type=str)
parser.add_argument("-v", "--verbose", action="store_true", help="więcej detali")
args = parser.parse_args()
print(args.folder)

