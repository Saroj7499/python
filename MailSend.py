#step1: Import SMTP pacakage
#step2:Create an Object
#Step3:Login (username and password)
#step4: Start session and send mail
#step5:close session

import smtplib
s = smtplib.SMTP("smtp.gmail.com",587) #port no.smtp 587
s.starttls()#for secured transcation of mail
s.login("m***********@gmail.com","************")
text = "Hey Saroj is here..."
s.sendmail("m**********@gmail.com","s*********@gmail.com",msg=text)
print("Mail sent sucessfully .. check your inbox")
s.quit()