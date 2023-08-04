# PF-Recoil-Converter
A simple python script to convert old PF recoil stats to the new mean/vairance

Doesnt account for speed, damper and recoveries yet, simply converts the raw recoil numbers to the new system.

To call the script open the containg folder in a terminal and use the folling command
.\recoil.exe [arg]

arguments:
info - Gives info about the script
convert - Converts recoil, code is much easier to digest and follow
oneliners - This does the same as convert but the code has been condensed down by 1 line for every 2
hello - hi

If you wish to run the source code script:

pip install "typer[all]"
pip install pyperclip

Python Main.py convert
give the input requested

Thanks @yeha. for the help :3
