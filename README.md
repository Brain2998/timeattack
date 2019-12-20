# TimeAttack
Time-based attack on passwords (https://en.wikipedia.org/wiki/Timing_attack)

Usage:\
python timing.py login_url username\
Example:\
python timing.py http://example.com/login admin

Headers and body of POST request should be edited for particular case. Default:\
Headers:\
'Content-Type': 'application/x-www-form-urlencoded'\
Body:\
username=%username&password=%password&submit=submit
