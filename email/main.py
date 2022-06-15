import smtplib

my_email = "hancai@outlook.com"
password = input("password is#")

with smtplib.SMTP("outlook.office365.com", 587) as connection:
    connection.ehlo()
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(from_addr=my_email, to_addrs="hancai@cisco.com", msg="Hello World!")
    connection.close()
