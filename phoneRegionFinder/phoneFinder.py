import phonenumbers

u1='+15307425637'
u2='+905307425637'

from phonenumbers import geocoder
number=phonenumbers.parse(u1)
print(geocoder.description_for_number(number,'tr'))


from phonenumbers import carrier
number=phonenumbers.parse(u2)
print(carrier.name_for_number(number,'tr'))

from phonenumbers import timezone
number=phonenumbers.parse(u1)
print(timezone.time_zones_for_number(number,))