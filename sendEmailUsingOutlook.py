import smtplib

def sendMail(sUsername,sPass,rUsername,subject,body):    
    # sUsername corresponds to email of sender
    # spass corresponds to password of sender's email
    # rUsername corresponds to email of reciever
    # subject -> subject of mail
    # body -> body o mail


    smtp_server = "smtp-mail.outlook.com"
    
    smtp = smtplib.SMTP(smtp_server, 587)
    smtp.starttls()
    smtp.login(sUsername, sPass)

    message = f"""\
    Subject: {subject}

    {body}"""
    smtp.sendmail(sUsername, rUsername, message)
            
    smtp.quit()
    
