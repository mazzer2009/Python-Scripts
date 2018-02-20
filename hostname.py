#!/usr/bin/python
import mysql.connector
import sys
def db_query(mac):	

	cnx = mysql.connector.connect(user='***', password='***', host='fogserver.dacom', database='fog')
	cursor=cnx.cursor()
	mac =(mac,)
	
	
	query=("select hostname from hosts inner join hostMAC on (hmID=hostID) where hostMAC.hmMAC=%s")
	
	
	cursor.execute(query,mac)
	for hostname in cursor:
		#print("{}".format(hostname))
		return hostname[0]


#############################################################################33
if(len(sys.argv)!=2):
	print("Usage: hostname.py [MAC]")
	exit(0)

mac = sys.argv[1]
host=db_query(mac)
if(host==None):
	print("MAC not found in database")
else:
	print(host)