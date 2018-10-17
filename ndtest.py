import usb
import time
import datetime 
import MySQLdb 
import smtplib 
from email.mime.text import MIMEText


streams="Vanessa's Sound level meter:i"
tokens="<tokencode>"
now= datetime.datetime.now()

# connect to smtp server
smtpUser= "youremail@gmail.com"
smtpPass= "yourpasswd"
toAdd= ["recipientemail1@gmail.com", "recipientemail1@gmail.com"]
fromAdd= "youremail@gmail.com"

#find the device
dev= usb.core.find(idVendor=0x16c0,idProduct=0x5dc)

#If the device is found
assert dev is not None

print (dev)

print (hex(dev.idVendor)+','+hex(dev.idProduct))


#connecting to the database
db= MySQLdb.connect("localhost", "monitor", "password", "database")
cur= db.cursor()

while True:
	time .sleep(1)
	ret= dev.ctrl_transfer(0xC0,4,0,0,200)
	dB= (ret[0]+((ret[1]&3)*256))*0.1+30
	try:
		if ( dB >= 70):
			print (dB)
			msg="{'dB':'"+str(dB)+"'}" 
			body= MIMEText("Noise level at " + str(dB) + " on " + now.strftime('%a,%b %d,%Y %H:%M:%S %Z'))
			body["Subject:"]= "Sound meter report"
			body["From:"]= fromAdd
			body ["To"]=", ".join(toAdd)
			s= smtplib.SMTP('smtp.gmail.com',587) #makes  an instance variable s to connect to the server

                         #setting up the encryption
			s.ehlo()
			s.starttls()
			s.ehlo()
			s.login(smtpUser, smtpPass) #logs in using user credentials
			s.sendmail(fromAdd, toAdd, body.as_string())
			s.quit()

			db.query("INSERT INTO ndtable (Date, Time, noise_level) VALUES(curdate(), curtime(), {0})".format(dB))
			db.commit()
			print ("Data committed")
		else:
			None
	except MySQLdb.Error as err: 
		print ("Error:", err)
		db.rollback()
cur.close()
db.close()	


