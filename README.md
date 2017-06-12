# SignalSearch
Classwork

**Brief Project Description**
Protein query to match known signal sequences to target membranes

Location of Signal Search Input Page:
http://bfx.eng.jhu.edu/klauer2/final/searchinput.html

Example Queries:
>all_signals
DSWGILFSHPYTPLYLLNTPGYRHVDDSDEDLLGKISKHWTGIKGRKRKILKKRHIRKRPVRRRRRGLKRTKKQKTKRRKKRKPAAK
RVKLDRPRRKSKKKKSQCPSDSEEDEGYKGLYKNLYEGLSRRRFLMGCGCSSHPEAETENFVKEELQEDLSKLSKISRLSQLKDEL

>gi|176866369|ref|NP_076994.2| KDEL motif-containing protein 1 isoform 1 precursor [Homo sapiens]
MFGTLLLYCFFLATVPALAETGGERQLSPEKSEIWGPGLKADVVLPARYFYIQAVDTSGNKFTSSPGEKV
FQVKVSAPEEQFTRVGVQVLDRKDGSFIVRYRMYASYKNLKVEIKFQGQHVAKSPYILKGPVYHENCDCP
LQDSAAWLREMNCPETIAQIQRDLAHFPAVDPEKIAVEIPKRFGQRQSLCHYTLKDNKVYIKTHGEHVGF
RIFMDAILLSLTRKVKMPDVELFVNLGDWPLEKKKSNSNIHPIFSWCGSTDSKDIVMPTYDLTDSVLETM
GRVSLDMMSVQANTGPPWESKNSTAVWRGRDSRKERLELVKLSRKHPELIDAAFTNFFFFKHDENLYGPI
VKHISFFDFFKHKYQINIDGTVAAYRLPYLLVGDSVVLKQDSIYYEHFYNELQPWKHYIPVKSNLSDLLE
KLKWAKDHDEEAKKIAKAGQEFARNNLMGDDIFCYYFKLFQEYANLQVSEPQIREGMKRVEPQTEDDLFP
CTCHRKKTKDEL

Usage:
Using Signal Search only requires entering protein sequence either in Fasta format
or as a amino acid sequence.  If Fasta format is used the name will appear, 
otherwise protein name with be "n/a".

Requirements:
JQuery plugin Datasorter - https://mottie.github.io/tablesorter/docs/

JQuery 1.9+ for full use of Datasorter

js/sorter.js

css/style.css - modified version of tablesorter.com/themes/blue/style.css

searchinput.html

signalsearchFasta.cgi

templates/display.html

database information: klauer2

table: signal

columns: name, example, location, reference


Database Information:

Database Information was obtained from http://genome.unmc.edu/LocSigDB/cgi-bin/search.cgi?signal=all 

King BR, Guda C. ngLOC: an n-gram-based Bayesian method for estimating the subcellular proteomes of eukaryotes. 
Genome biology. 2007;8(5):R68. [PubMed]
