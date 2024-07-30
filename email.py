
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("630786shahidmalik@gmail.com", "##APP PASSWORD##")
server.sendmail(
    "630786shahidmalik@gmail.com",
    "shahidteamopine@gmail.com",
    "Subject: Password Reset\n\nThe reset password link is valid for 1 minute."
)
print("Mail sent")
