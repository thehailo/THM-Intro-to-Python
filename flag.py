# The flag is encoded five times each with base16, base32, and base64.
# https://tryhackme.com/room/introtopython
import base64

# Define functions to decode base16, base32, and base64.
def b16d(encoded):
	decoded = base64.b16decode(encoded)
	return decoded
def b32d(encoded):
	decoded = base64.b32decode(encoded)
	return decoded
def b64d(encoded):
	decoded = base64.b64decode(encoded)
	return decoded

# Load encoded file.
flagfile = input("Please enter the name of the flag file: ")
encodedflag = open(flagfile, "rb").read()

# Run through five rounds of base16 decoding.
for i in range(5):
	encodedflag = b16d(encodedflag)
# Run through five rounds of base32 decoding.
for i in range(5):
	encodedflag = b32d(encodedflag)
# Run through five rounds of base64 decoding.
for i in range(5):
	if i != 4:
		encodedflag = b64d(encodedflag)
	else:
		encodedflag = b64d(encodedflag)
		print("The flag is:",encodedflag)