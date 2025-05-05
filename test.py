from pyhamtools.locator import latlong_to_locator
from pyhamtools.locator import locator_to_latlong

print("51.12492, 16.94183")
print(latlong_to_locator(51.124913194444446, 16.94184027777778,10))
print(latlong_to_locator(51.12492, 16.94183,10))

print("JO81LC39AX")
print(locator_to_latlong("JO81LC39AX"))

b="MN45GU30AN"
print(b)
print(locator_to_latlong(b))
print(latlong_to_locator(45.83568,68.52518,10))
