#!/usr/bin/env python3
'''
Protkoll generierung für Azubi-meeting
'''
from argparse import ArgumentParser
from datetime import datetime
import sys
bool_verbose = False
def verbose(vnachricht):
    ''' Verbose
        '''
    print(f"[debug] \t {vnachricht}")

def ausbilderthemen():
    ''' Ausbilderthemen werden in schleife hinzugefügt
        - wenn der Input leer ist, wird die Eingabe beendet'''
    print("__AusbilderTHEMEN__\n")
    ergebnis = '''\nThemen:'''
    print("Füge Themen hinzu, wenn das feld leer ist, endet die Aufnahme von Themen")
    thema = "42"
    if bool_verbose:
        verbose(f"thema: {thema}")
    while thema != "":
        thema = input(">> ")
        if thema != "":
            ergebnis += f"\n   * {thema}"
    if bool_verbose:
        verbose("Alle Ausbilderthemen hinzugefügt")
    return ergebnis

def xtime(toolortech:str):
    ''' XTIME nimtt die Tool oder Techtime und macht einen Tabelleneintrag daraus'''
    print(f"__{toolortech}__\n")
    tt_thema = input("Thema\n>> ")
    tt_darbieter = input("Darbieter\n>> ")
    if bool_verbose:
        verbose(f"tooltech -> {toolortech} Thema wurde hinzugefügt")
    return f"|{toolortech}:|{tt_darbieter}|{tt_thema}|"



def main():
    ''' Main Funktion
        - Argument Parser werden hinzugefügt
        - wenn nichts angegeeben wird, wird das Programm geschlossen'''
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
    parser.add_argument("-v", "--verbose",
                        help="Verbose für Debug",
                        action="store_true")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    endergebnis = f'''# {datetime.now().date().isoformat()}'''
    if args.verbose:
        # damit wird die Globale Var genommen
        global bool_verbose
        bool_verbose = True
        # erst ab hier tun verbose argumente
        if len(sys.argv) == 2:
            if bool_verbose:
                verbose("Keine weiteren Argumente, Programm wird beendet")
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
