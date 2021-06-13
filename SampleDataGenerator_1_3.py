import random
import mysql.connector
import os,binascii
import string

#Database connection
mydb = mysql.connector.connect(
  host="<database hostname>",
  user="username",
  password="password",
  database="database name"
)

mycursor = mydb.cursor()

query = "CREATE TABLE IF NOT EXISTS router_details(`Sapid` varchar(18) DEFAULT NULL,`Hostname` varchar(14) DEFAULT NULL,`Loopback` varchar(15) DEFAULT NULL, `MACaddress` varchar(17) DEFAULT NULL, `isActive` boolean NOT NULL DEFAULT 1, PRIMARY KEY (`Sapid`))"
mycursor.execute(query)

    # Random record generation
n = int(input('How many number of record to be created? '))
Sapid, Hostname, Loopback, MACaddress = ([] for _ in range(4))
for _ in range(n):
    macdata = str(binascii.b2a_hex(os.urandom(6))).split("'")[1]
    macdata = ':'.join(macdata[i:i+2] for i in range(0, len(macdata), 2))
    print ('Generated mac', macdata)

    hostdata = 'host_'+''.join(random.choices(string.ascii_letters + string.digits, k=9))
    print ('Generated host', hostdata)

    ipdata=str(random.randint(0, 255))
    for _ in range(3):
      ipdata += '.'
      ipdata += str(random.randint(0, 255))
    print ('Generated ip', ipdata)

    sapiddata = str(binascii.b2a_hex(os.urandom(9))).split("'")[1]
    print ('Generated sapid', sapiddata)
    Sapid.append(sapiddata)
    Hostname.append(hostdata)
    Loopback.append(ipdata)
    MACaddress.append(macdata)

# Insert generated data into connected Database
for x in range(len(Sapid)):
  # print(f'Sapid({Sapid[x]}) \tHostname({Hostname[x]}) \tLoopback({Loopback[x]}) \tMACaddress({MACaddress[x]})')
  sql = f"INSERT INTO router_details (Sapid, Hostname, Loopback, MACaddress) VALUES ('{Sapid[x]}', '{Hostname[x]}', '{Loopback[x]}', '{MACaddress[x]}')"
  mycursor.execute(sql)

mydb.commit()
sql = f"SELECT * FROM router_details"
mycursor.execute(sql)
results = mycursor.fetchall()
print(results)
mycursor.close()
mydb.close()