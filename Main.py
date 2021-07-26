import phonenumbers
from phonenumbers import carrier

# getting phone number
ph_no = input('Enter phone number with Country Code: ')
a = phonenumbers.parse(ph_no)

# Print Details
service = carrier.name_to_number(a, 'en')
print(service)
