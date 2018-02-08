import hashlib, binascii
import base64
import os
import sys

password = raw_input(b"Please Enter Your Password: ")
iterations = 2**len(password)
print "Iterations: " + str(iterations)

directory = "/dev/disk/by-id/"

for file in os.listdir(directory):
    filename = file.upper()
    if filename.startswith("SCSI") and "-PART" not in filename:
        wwid = filename.replace("SCSI-3", "").upper()
        dk = hashlib.pbkdf2_hmac('sha512', wwid, password, iterations) 
	print(wwid + "\t" + base64.b64encode(dk))
        continue
    else:
        continue
