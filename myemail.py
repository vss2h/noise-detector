import smtplib

smtpUser= "youremail@gmail.com"
smtpPass= "yourpassword"

toAdd= "youremail@gmail.com"
fromAdd= ["recipientemail1@gmail.com", "recipientemail1@gmail.com"]

subj= "This is a test"
header= "To: " + toAdd + '\n' +'From: ' + fromAdd +'\n' + 'Subject: ' + subj
body= "This is a message send from Vanessa's Raspberry Pi"


print header + '\n' + body

s= smtplib.SMTP('smtp.gmail.com',587) #makes  an instance variable s to connect to the server

#setting up the encryption

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass) #logs in using user credentials
s.sendmail(fromAdd, toAdd, header + '\n\n' + body)
s.quit()
