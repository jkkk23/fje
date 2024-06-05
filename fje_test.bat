@echo off
cd fje
python fje.py -f data.json -s tree -i poker-face
python fje.py -f data.json -s tree -i star
python fje.py -f data.json -s rectangle -i poker-face
python fje.py -f data.json -s rectangle -i star
pause
@echo on