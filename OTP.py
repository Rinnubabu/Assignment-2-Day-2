import random as ram
import string

length = 6
otp = ""
character = string.ascii_letters + string.digits
for i in range(length):
  otp = otp + ram.choice(character)


print("OTP: ", otp)