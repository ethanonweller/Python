import smtplib, ssl, socket, urllib.request

env:
    PASSWORD: ${{ <AFXiJwe86hY6DhJ> }}
port = 465 # for ssl
smtp_server = "smtp.gmail.com"
sender_email = "test.python.0530@gmail.com"
receiver_email = "test.python.0530@gmail.com"
password = PASSWORD

host_name = socket.gethostname()
priv_ip = socket.gethostbyname(host_name)
# to get public address w/ standard library you can request through browser
pub_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

message = """\
Subject: info

This message is sent from host_info.py. \n""" + "Host Name: ", \
host_name + " Private IP: \n" + priv_ip + "\n Public IP: " + pub_ip

# Creates a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
