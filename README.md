# pcapSort
Sorts pcap files by first 18/32 symbols and creates output file named <b>OUTPUT.TXT</b>

<b>How to use:</b>

python3 parser.py [INPUT FILE] [SORT METHOD]

<b>1st:</b> sorts pcap K12 by first 18 symbols 

<b>2st:</b> sorts pcap K12 by second 18 symbols

<b>3st:</b> sorts pcap K12 by first 32 symbols

<b>Example:</b>

┌─[root@Windy34]─[/home/Windy34/Documents]

└──╼ #python3 parser.py k12.txt 2

Sorted ranges are:

 |00|1e|10|1f|00|00| |4c|54|99|45|e5|d5| |00|1e|10|1f|00|00| 
 
 |00|1e|10|1f|00|00| |00|1e|10|1f|00|00| |4c|54|99|45|e5|d5| 
 
 |4c|54|99|45|e5|d5| |4c|54|99|45|e5|d5| |4c|54|99|45|e5|d5| 
 
 |00|1e|10|1f|00|00| |4c|54|99|45|e5|d5| |00|1e|10|1f|00|00|
 
File was sorted by second 18 symbols

