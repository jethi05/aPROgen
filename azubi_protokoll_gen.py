#!/usr/bin/env python3
'''
Protkoll generierung für Azubi-meeting
'''
from argparse import ArgumentParser
from datetime import datetime
import sys

def verbose(vnachricht):
    print(bool_verbose)
    if bool_verbose:
        print(f"[debug] \t {vnachricht}")

def ausbilderthemen():
    print("__AusbilderTHEMEN__\n")
    Ergebnis = '''\nThemen:''' 
    print("Füge Themen hinzu, wenn das feld leer ist, endet die Aufnahme von Themen")
    thema = "x"
    while thema != "":
        thema = input(">> ")
        if thema != "":     
            Ergebnis += f"\n   * {thema}"
    return Ergebnis
    
def xtime(toolortech:str):
    print(f"__{toolortech}__\n")
    tt_thema = input("Thema\n>> ")
    tt_darbieter = input("Darbieter\n>> ")
    return f"|{toolortech}:|{tt_darbieter}|{tt_thema}|"



def main():
    parser = ArgumentParser(prog = "Azubi Protokoll gen",
                            description = "Für unser Azubi Wiki wird hier der Eintrag generiert",
                            epilog = "möge argparse mit euch sein")
    parser.add_argument("-a", "--ausbilderthemen",
                        help="Hier können Themen aus dem Azubi-meeting hingeschrieben werden",
                        action="store_true")
    parser.add_argument("-t", "--tooltime",
                        help="Fügt ToolTime Thema && Namen hinzu",
                        action="store_true")
    parser.add_argument("-T", "--techtime",
                        help="Fügt TechTime Thema && Namen hinzu",
                        action="store_true")
    #parser.add_argument("-v", "--verbose",
    #                   action="store_true")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    endergebnis = f'''# {datetime.now().date().isoformat()}'''
    if args.ausbilderthemen:
        endergebnis += f"\n{ausbilderthemen()}"
    if args.tooltime:
        endergebnis += f"\n{xtime('TOOLtime')}"
    if args.techtime:
        endergebnis += f"\n{xtime('TECHtime')}"
    print("---------------------") 
    print(endergebnis)
    print("---------------------") 

if __name__ == "__main__":
    main()


















