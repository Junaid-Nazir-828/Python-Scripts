import smtplib

def mail(sUsername,sPass,rUsername,subject,body):    
        
    smtp_server = "smtp-mail.outlook.com"
    

    smtp = smtplib.SMTP(smtp_server, 587)
    smtp.starttls()
    smtp.login(sUsername, sPass)

    message = f"""\
    Subject: {subject}

    {body}"""
    smtp.sendmail(sUsername, rUsername, message)
            

    smtp.quit()
    