#!/usr/local/bin/python3
# Kim Lauer (klauer2)
# Final Project
# Due 5/7/16

# Content Type Header to allow printing in HTML
print("Content-type: text/html\n\n")

import mysql.connector
import cgi
import cgitb; cgitb.enable()
import jinja2
import re

signal = []
protein_name = 'n/a'
signal_found = False

# stores results from database search
class Results(object):
    def _init_(signal, name=None, example=None, location=None, reference=None):
        signal.name = name
        signal.example = example
        signal.location = location
        signal.reference = reference

# called if their was a signal matching pattern
def found_signal(str):
    signal.append(str)
    return True

# path to template, creates environment & name of template to use
templateLoader = jinja2.FileSystemLoader( searchpath="./templates" )
env = jinja2.Environment(loader=templateLoader)
template = env.get_template('display.html')

# obtained entered data from initial form page
form = cgi.FieldStorage()
if form.getvalue('signal_search'):
    protein_seq = form.getvalue('signal_search')
else:
    protein_seq = "Error"

# removed whitespace from entered data
protein_seq = protein_seq.lstrip()

# if a fasta sequence was entered
if protein_seq.startswith(">"):
    pro = re.search(r'>(.*)([\r|\n])', protein_seq)
    protein_name = pro.group(1).rstrip()
    if protein_name == "":
        protein_name = "n/a"

# took out all other whitespace
protein_seq = protein_seq.rstrip().upper()

# Nucleus Signals
if re.search(r'GKISKHWTGI', protein_seq):
    signal_found = found_signal('%GKISKHWTGI%')
if re.search(r'KGRKR', protein_seq):
    signal_found = found_signal('%KGRKR%')
if re.search(r'KILKKRHI', protein_seq):
    signal_found = found_signal('%KILKKRHI%')
if re.search(r'RKRPVRRR', protein_seq):
    signal_found = found_signal('%RKRPVRRR%')
if re.search(r'RRGLKR', protein_seq):
    signal_found = found_signal('%RRGLKR%')
if re.search(r'TKKQKT', protein_seq):
    signal_found = found_signal('%TKKQKT%')
if re.search(r'KRK', protein_seq):
    signal_found = found_signal('%KRK%')
if re.search(r'KKRR', protein_seq):
    signal_found = found_signal('%KKRR%')
if re.search(r'PAAKRVKLD', protein_seq):
    signal_found = found_signal('%PAAKRVKLD%')
if re.search(r'KHRKHPG', protein_seq):
    signal_found = found_signal('%KHRKHPG%')
if re.search(r'PQPKKKP', protein_seq):
    signal_found = found_signal('%PQPKKKP%')
if re.search(r'RPRRK', protein_seq):
    signal_found = found_signal('%RPRRK%')

# Mitochondria Signals
if re.search(r'SKK', protein_seq):
    signal_found = found_signal('%SKK%')
if re.search(r'KKSQ', protein_seq):
    signal_found = found_signal('%KKSQ%')

# Endoplasmic Reticulum Signals
if re.search(r'.*KDEL$', protein_seq):
    signal_found = found_signal('%KDEL%')
if re.search(r'KEEL', protein_seq):
    signal_found = found_signal('%KEEL%')
if re.search(r'QEDL', protein_seq):
    signal_found = found_signal('%QEDL%')

# Golgi Apparatus Signals
if re.search(r'CPSDSEEDEG', protein_seq):
    signal_found = found_signal('%CPSDSEEDEG%')
if re.search(r'YKGL', protein_seq):
    signal_found = found_signal('%YKGL%')
if re.search(r'YAGL', protein_seq):
   signal_found = found_signal('%YAGL%')
if re.search(r'YKNL', protein_seq):
   signal_found = found_signal('%YKNL%')
if re.search(r'YEGL', protein_seq):
   signal_found = found_signal('%YEGL%')

# Plasma Membrane/Peroxisome/Lysosome Signals
if re.search(r'DSWGILFSHP', protein_seq):
    signal_found = found_signal('%DSWGILFSHP%')
if re.search(r'YTPL', protein_seq):
    signal_found = found_signal('%YTPL%')
if re.search(r'YLLNT', protein_seq):
    signal_found = found_signal('%YLLNT%')
if re.search(r'PGYRHV', protein_seq):
    signal_found = found_signal('%PGYRHV%')
if re.search(r'DDSDEDLL', protein_seq):
    signal_found = found_signal('%DDSDEDLL%')
if re.search(r'SRRRFL', protein_seq):
    signal_found = found_signal('%SRRRFL%')
if re.search(r'MGCGCSSHPE', protein_seq):
    signal_found = found_signal('%MGCGCSSHPE%')
if re.search(r'AETENFV', protein_seq):
    signal_found = found_signal('%AETENFV%')
if re.search(r'SKL', protein_seq):
    signal_found = found_signal('%SKL%')
if re.search(r'SKI', protein_seq):
   signal_found = found_signal('%SKI%')
if re.search(r'SRL', protein_seq):
   signal_found = found_signal('%SRL%')
if re.search(r'SQL', protein_seq):
   signal_found = found_signal('%SQL%')

# If no signal found, no attempt to connect to database
if signal_found == False:
    nosignal = 'No Signal Found'

# list to store signals found
signal_info = []

# if signal found connect to database
if signal_found == True:
   
    try:
        conn = mysql.connector.connect(user='klauer2', password='t3tra', host='localhost', database='klauer2')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ACCESS_DENIED_ERROR. Check user name and password")
        else:
            print(err)
    else:
        curs=conn.cursor()
# MySql Query
    for signals in signal:

        sel = ("SELECT name, example, location, reference ")
        fr = ("FROM signal ")
        where = ("WHERE name LIKE %s")
        qry = sel + fr + where

        curs.execute(qry,(signals,))

        for (name, example, location, reference) in curs:
            n = name
            e = example
            l = location
            r = reference
            x = Results()
            x.name = n
            x.example = e
            x.location = l
            x.reference = r
            signal_info.append(x)

# sent data to results page
    print(template.render(match='yes', protein_name=protein_name, signal=signal_info))

    curs.close()

# if no hits
else:
    print(template.render(match='No Match', protein_name=protein_name, signal=signal_info))
