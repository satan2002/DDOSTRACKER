import os, time, subprocess, sys, time, datetime, requests, json
from datetime import datetime
os.system("clear")
print("Logs have Started")
print("H4X00R")
alert_pps = int(sys.argv[1])
interface = str(sys.argv[2])
URL = "https://discord.com/api/webhooks/"
def getpps():
    o = subprocess.getoutput(f"grep {interface}: /proc/net/dev | cut -d :  -f2 "+"| awk '{ print $2 }'")
    time.sleep(1)
    t = subprocess.getoutput(f"grep {interface}: /proc/net/dev | cut -d :  -f2 "+"| awk '{ print $2 }'")
    pps = int(str(int(o) - int(t)).replace("-", ""))
    return(pps)
def attackdetected(pps):
    now = datetime.now()
    current_time = now.strftime("%d-%m-%Y--%H:%M:%S")
    pps = getpps()
    os.system(f"tcpdump -n -s0 -c {alert_pps} -w /root/TCPDUMP/capture.{current_time}.pcap")
    print(f"\n\nAttack Started at {current_time}\nPPS : {pps}\nDump name : capture.{current_time}.pcap")
    payload = {
          "embeds": [
        {
          "title": "DDoS Attack",
          "description": "DDoS attack had been Detected.",
          "url": "https://github.com/satan2002",
          "color": 16056320,
          "fields": [
            {
              "name": "Server:",
              "value": "``H4X00R``",
              "inline": True
            },
            {
              "name": "Dump Name",
              "value": f"``capture.{current_time}.pcap``",
              "inline": True
            },
            {
              "name": "PPS:",
              "value": f"``{pps}``",
              "inline": True
            }
          ],
          "author": {
            "name": "H4X00R",
            "url": "https://github.com/satan2002",
            "icon_url": "https://i.pinimg.com/originals/0c/ec/c2/0cecc275f0ad539388a9ab8de1a5e49c.png"
          },
          "footer": {
            "text": "Our system has sucessfully captured an attack.",
            "icon_url": "https://i.pinimg.com/originals/0c/ec/c2/0cecc275f0ad539388a9ab8de1a5e49c.png"
          },
          "thumbnail": {
            "url": "https://i.pinimg.com/originals/0c/ec/c2/0cecc275f0ad539388a9ab8de1a5e49c.png"
          }
        }
      ]
    }
    header_data = {'content-type': 'application/json'}
    requests.post(URL, json.dumps(payload), headers=header_data)
    while pps > alert_pps:
        pps = getpps()
        time.sleep(1)
while True:
    pps = getpps()
    if pps > alert_pps:
        attackdetected(pps)