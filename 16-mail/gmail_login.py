import smtplib
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
smtpobj.ehlo()
smtpobj.starttls()
smtpobj.ehlo()
smtpobj.login('@gmail.com', '')
