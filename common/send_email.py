# coding = utf-8 
'''
Created on 29 May 2016

@author: jophy.cui
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import time


def send_email(HOST,PORT,mail_username,mail_password,to_addrs,folder):
    
    #list all report and try to get the latest report  
    lists=os.listdir(folder)
    print lists
    lists.sort(key=lambda fn: os.path.getmtime(folder+fn) if not os.path.isdir(folder+"\\"+fn) else 0)
    print ("The latest report is "+lists[-1])
    lastest_report = os.path.join(folder,lists[-1])


    #send email out
    from_addr = mail_username
    # Create SMTP Object
    smtp = smtplib.SMTP()
    print 'connecting ...'
    # show the debug log
#    smtp.set_debuglevel(1)

    # connect to smtp server
    try:
        print smtp.connect(HOST,PORT)
    except:
        print 'CONNECT ERROR ****'
    # gmail uses ssl
    smtp.starttls()
    # login with username & password
    try:
        print 'login successfully'
        smtp.login(mail_username,mail_password)
    except:
        print 'LOGIN ERROR ****'
        
    # fill content with MIMEText's object 

    msg = MIMEMultipart() 
    msg['From'] = from_addr
    msg['To'] = to_addrs
    msg['Subject']='smoke test report'
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
  
    #open report and read it for preview mode.  
    f = open(lastest_report,'rb')
    mail_body =f.read()
    f.close()
    part = MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg.attach(part)
    
    # add attachment
    part = MIMEApplication(open(lastest_report,'rb').read()) 
    part.add_header('Content-Disposition', 'attachment', filename= lists[-1]) 
    msg.attach(part) 
     
    #send email out
    smtp.sendmail(from_addr,to_addrs,msg.as_string())
    
    smtp.quit()
