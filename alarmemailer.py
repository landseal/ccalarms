# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

msg = MIMEText('uhoh')

# me == the sender's email address
# you == the recipient's email address
me = 'sealandjoshua@gmail.com'
you = 'joshua.sealand@motivps.com'
msg['Subject'] = 'clipper creek alarm'
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()
