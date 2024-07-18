import smtplib


email = "amiralipeymanispacelove@gmail.com"

password = "piij ajpc ehvf yhqh"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="piliconwalys@gmail.com", msg="Subject:fuck you")

    