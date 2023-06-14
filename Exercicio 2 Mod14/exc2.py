import sys
import lib

meses = sys.argv[1:]

for mes in meses:
    lib.gera_graficos(mes)
