import subprocess
import re
from datetime import datetime, timezone
import psycopg2
from read_config import get_database_config

database_config = get_database_config("../config/config.txt")
connect_string = 'dbname={} user={} host={} password={}'.format(database_config['database'],
                                                                database_config['username'],
                                                                database_config['hostname'],
                                                                database_config['password'])


#run and store speed test results
proc = subprocess.Popen(["speedtest"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
#print("program output:", out)
str_out = str(out)
#print(str_out)
#find the numbers in the wall of text that is the output
srvr = re.search('Server: (.+?) \(id:', str_out)
srvr = srvr.group(1)
lat = re.search('Latency:    (.+?) ms', str_out)
lat = lat.group(1)
dwn = re.search('Download:   (.+?) Mbps', str_out)
dwn = dwn.group(1)
up = re.search('Upload:   (.+?) Mbps', str_out)
up = up.group(1)
date = datetime.now(timezone.utc)


#query = "INSERT INTO public.speed_tests VALUES(%s, %s, %s, %s, %s)", (str(date), srvr, lat, dwn, up)
try:
    conn = psycopg2.connect(connect_string)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO public.speed_tests VALUES(%s, %s, %s, %s, %s)", (date, srvr, lat, dwn, up))
    conn.commit()

except (Exception) as error:
    print(error)