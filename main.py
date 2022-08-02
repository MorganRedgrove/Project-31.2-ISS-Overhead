import requests
import smtplib
import time
from datetime import datetime



def overhead():
    if iss_latitude in range(MY_LAT-5,MY_LAT+5) and iss_longitude in range(MY_LONG-5,MY_LONG+5):
        return True
    else:
        pass


MY_LAT = round(-35) # Your latitude
MY_LONG = round(-65) # Your longitude


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()


iss_latitude = round(float(data["iss_position"]["latitude"]))
iss_longitude = round(float(data["iss_position"]["longitude"]))
print(iss_latitude)
print(iss_longitude)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
h_sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
h_sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


now = datetime.now()
h_now = now.hour

print(h_sunset)
print(h_sunrise)
print(h_now)


status = ""
if h_now > h_sunset or h_now < h_sunrise:
    status = "night"
else:
    status = "day"


print(status)

loop = 1
while loop == 1:
    if overhead() and status == "night":
        print("sending")
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user="", password="")
        connection.sendmail(from_addr="",
                            to_addrs="",
                            msg="Subject:Look Up!\n\nThe ISS is currently overhead.")
        connection.close()

        time.sleep(60)






#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



