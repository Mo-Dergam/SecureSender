#Passwortgenerator:
# Hier Importieren wir string Bibliothek um passwort zu erstellen.
import string
# Hier Imortieren random Bibliothek, die uns ermöglischt ein Passwort auf zufällige Weise 
# aus dem String-Bibliothek zu erstellen 
import random 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
Password1 = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
password11 = ''.join(random.choice(Password1) for _ in range(16))


# Hier estellen wir variablen und speichern wir unsere Email
#und das benötigte passwort um sie in der login-Funktion zu benutzen 
sender_email = "mn512693@gmail.com"
my_password = "Hier das Passwort"
# und hier eingabe von benutzer-Name und seine Email adresse 
Benutzer_name = input("geben Sie Ihr Vor un Nachname ein:")
receiver_email = input("Geben Sie Ihr Email_Adresse Ein:")
import time 
t= 5 
time.sleep(t)
# Hier verbinden wir mit gemail Server 
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()


#Hier logen wir in unsere Email-Adresse
server.login(sender_email, my_password)


# Hier erstellen wir unseren Email-begriff und Email-Text. 
Subject = "Ihr neues Passwort von Secur Mail Pass"
body = F"Lieber {Benutzer_name},\n\nwir freuen uns, Ihnen Ihr neues Passwort mitzuteilen. \n\nNeus Passwort: {password11} \n\nBitte verwenden Sie das Passwort, um eine Sichers Passwort für Ihr konto zu erstellen. \n\nMit Freundlichen Grüßen \nMohammad Alfayad Ersteller des Programms Secur Mail Pass"

# Erstellen eine MIMEMultipart-Nachricht
message = MIMEMultipart()

# Hier Rufen wir alle benötigten Variablen um das Email zu erstellen
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = Subject
message.attach(MIMEText(body))


server.sendmail(sender_email,
receiver_email,message.as_string())

print(password11, end = '')

server.quit





# def Password12():
#   i = int(input("aus wie stellig soll ihr passwort sein:"))
#   Z = input("Soll dein Passwort zahlen enthalten: (Ja/Nein)")
#   GB = input("Soll dein passwort großbuchtaben haben: (Ja/Nein)")
#   KB = input("Soll dein passwort Kleinbuchtaben haben: (Ja/Nein)")
#   S = input("soll dein passwort sonderzeichen haben: (Ja/Nein)")
#  # Ja, Nein, Nein, Nein
#   if Z.lower() == "ja" and GB.lower() == "nein" and KB.lower() == "nein" and S.lower() == "nein":
#     Password1 = string.digits
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Ja, Ja, Nein, Nein
#   elif Z.lower() == "ja" and GB.lower() == "ja" and KB.lower() == "nein" and S.lower() == "nein":
#     Password1 = string.digits + string.ascii_uppercase
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Ja, Ja, Ja, Nein
#   elif Z.lower() == "ja" and GB.lower() == "ja" and KB.lower() == "ja" and S.lower() == "nein":
#     Password1 = string.digits + string.ascii_uppercase + string.ascii_lowercase
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Ja, Ja, Ja, Ja
#   elif Z.lower() == "ja" and GB.lower() == "ja" and KB.lower() == "ja" and S.lower() == "ja":
#     Password1 = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Nein, Ja, Ja, Ja
#   elif Z.lower() == "nein" and GB.lower() == "ja" and KB.lower() == "ja" and S.lower() == "ja":
#     Password1 = string.ascii_uppercase + string.ascii_lowercase + string.punctuation
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Nein, Nein, Ja, Ja
#   elif Z.lower() == "nein" and GB.lower() == "nein" and KB.lower() == "ja" and S.lower() == "ja":
#     Password1 = string.ascii_lowercase + string.punctuation
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Nein, Nein, Nein, Ja
#   elif Z.lower() == "nein" and GB.lower() == "nein" and KB.lower() == "nein" and S.lower() == "ja":
#     Password1 = string.punctuation
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Ja, Ja, Nein, Ja
#   elif Z.lower() == "ja" and GB.lower() == "ja" and KB.lower() == "nein" and S.lower() == "ja":
#     Password1 = string.digits + string.ascii_uppercase + string.punctuation
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Ja, Nein, Ja, Ja
#   elif Z.lower() == "ja" and GB.lower() == "nein" and KB.lower() == "ja" and S.lower() == "ja":
#     Password1 = string.digits + string.ascii_lowercase + string.punctuation
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Ja, Nein, Nein, Ja
#   elif Z.lower() == "ja" and GB.lower() == "nein" and KB.lower() == "nein" and S.lower() == "ja":
#     Password1 = string.digits + string.punctuation
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Nein, Ja, Ja, Nein
#   elif Z.lower() == "nein" and GB.lower() == "ja" and KB.lower() == "ja" and S.lower() == "nein":
#     Password1 = string.ascii_uppercase + string.ascii_lowercase 
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Nein, Ja, Nein, Ja
#   elif Z.lower() == "nein" and GB.lower() == "ja" and KB.lower() == "nein" and S.lower() == "ja":
#     Password1 = string.ascii_uppercase + string.punctuation
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Nein, Ja, Nein, Nein
#   elif Z.lower() == "nein" and GB.lower() == "ja" and KB.lower() == "nein" and S.lower() == "nein":
#     Password1 =  string.ascii_uppercase
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
#  # Nein, Nein, Ja, Nein
#   elif Z.lower() == "nein" and GB.lower() == "nein" and KB.lower() == "ja" and S.lower() == "nein":
#     Password1 = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
#     password = ''.join(random.choice(Password1) for _ in range(i))
#     print(password, end = '')
# Password12()
