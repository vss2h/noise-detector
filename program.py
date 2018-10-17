
#trying some simple python programming to check how well the email sending work

import datetime
import smtplib
from email.mime.text import MIMEText

def main():
	now= datetime.datetime.now()
	#now= datetime.datetime.now()
	max_temp= 120.0
	min_temp= 20.0
	curr_temp= 0.0
	myfile= open("pfile.txt", 'r')
	for line in myfile:
		curr_temp = float(line)
		if curr_temp <= min_temp:
			print ("")
		elif curr_temp > min_temp and curr_temp < max_temp:
			smtpUser= "youremail@gmail.com"
			smtpPass= "yourpassword"

			toAdd= ["recipientemail1@gmail.com","recipientemail2@gmail.com"]
			fromAdd= "youremail@gmail.com"
			body= MIMEText("It is beautiful outside. The temperature is " + str(curr_temp) + " on " + now.strftime('%a,%b %d,%Y %H:%M:%S %Z'))
			

			body["Subject:"]= "Weather station report"
			body["From:"]= fromAdd
			body ["To"]=", ".join(toAdd)
			#body= "It is beautiful outside. The temperature is " + str(curr_temp) + " on " + now.strftime('%a,%b %d,%Y %H:%M:%S %Z') 


			print ("mail sent")

			s= smtplib.SMTP('smtp.gmail.com',587) #makes  an instance variable s to connect to the server

			#setting up the encryption

			s.ehlo()
			s.starttls()
			s.ehlo()

			s.login(smtpUser, smtpPass) #logs in using user credentials
			s.sendmail(fromAdd, toAdd, body.as_string())
			s.quit()
		elif curr_temp >= max_temp:
			 #save into file
                        # savefile= open("weatherfile.txt", 'w')
                        # savefile.write(body)
			 
			 smtpUser= "youremail@gmail.com"
			 smtpPass= "yourpassword"

			 toAdd= ["recipientemail1@gmail.com","recipientemail2@gmail.com"]
			 fromAdd= "youremail@gmail.com"
			 body= MIMEText("WARNING !!! \n It is too hot outside. The temperature is " + str(curr_temp) + " on " + now.strftime('%a,%b %d,%Y %H:%M:%S %Z'))

			 body["From:"]= fromAdd
			 body["To:"]=", ". join(toAdd)
                  	 body["Subject:"]= "weather station report"
                 	 #body= "WARNING !!! \n It is too hot outside. The temperature is " + str(curr_temp) + " on " + now.strftime('%a,%b %d,%Y %H:%M:%S %Z') 
			 #save into file
                         #savefile= open("weatherfile.txt", 'w')
                         #savefile.write(body)
			 

                 	 print ("mail2 sent")

                 	 s= smtplib.SMTP('smtp.gmail.com',587) #makes  an instance variable s to connect to the server
	
        	          #setting up the encryption

                	 s.ehlo()
        	         s.starttls()
                	 s.ehlo()

              	   	 s.login(smtpUser, smtpPass) #logs in using user credentials
                	 s.sendmail(fromAdd, toAdd, body.as_string())
                	 s.quit()
	      		
		
		#	savefile= open("weatherfile.txt", 'w')
                #	savefile.write(body)
main()
