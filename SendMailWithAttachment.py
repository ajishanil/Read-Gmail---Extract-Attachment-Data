#Sending mail with attachments from your Gmail account

# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import shutil
import os
import datetime


def sendOutputMail(fromAddress,toAddress,body,appPass,InputImageFolder,OutputImageFolder,emailOutputFolder):
    shutil.make_archive(os.path.join(emailOutputFolder,'inputs'), 'zip', InputImageFolder)
    shutil.make_archive(os.path.join(emailOutputFolder,'outputs'), 'zip', OutputImageFolder)

    # instance of MIMEMultipart
    msg = MIMEMultipart()
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Subject'] = "Python Execution Completed - "+str(datetime.date.today())
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    inputfile=os.path.join(emailOutputFolder,'inputs.zip')
    outputfile=os.path.join(emailOutputFolder,'outputs.zip')

    attachment1 = open(inputfile, "rb")
    attachment2=open(outputfile,'rb')

    # instance of MIMEBase and named as

    p1 = MIMEBase('application', 'octet-stream')
    p2 = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p1.set_payload((attachment1).read())
    p2.set_payload((attachment2).read())

    # encode into base64
    encoders.encode_base64(p1)
    encoders.encode_base64(p2)

    p1.add_header('Content-Disposition', "attachment; filename= %s" % 'input.zip')
    p2.add_header('Content-Disposition', "attachment; filename= %s" % 'output.zip')

    # attach the instance 'p' to instance 'msg'
    msg.attach(p1)
    msg.attach(p2)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromAddress, appPass)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromAddress, toAddress, text)

    # terminating the session
    s.quit()
