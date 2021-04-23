# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bitcoin import *
my_private_key = random_key()
print("Private Key: %s\n" % my_private_key)
my_public_key = privtopub(my_private_key)
print("Public Key: %s\n" % my_public_key)
my_bitcoin_address = pubtoaddr(my_public_key)
print("Bitcoin Address: %s\n" % my_bitcoin_address)