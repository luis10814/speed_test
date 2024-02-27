import subprocess
import re
from datetime import datetime, timezone


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

print(srvr)
print(lat)
print(dwn)
print(up)
print(date)