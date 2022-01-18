import phonenumbers
import time

from phonenumbers import timezone, geocoder, carrier
number = input("Enter Your NO. with + __:")
phone = phonenumbers.parse(number)
# time = timezone.time_zone_for_number
car = carrier.name_for_number(phone,"en")
reg = geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)