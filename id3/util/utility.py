# All Rights Reserved.
# Copyright (C) 2014


__author__ = 'Vijay Shanker Dubey'
__project__ = 'metapy'
__Timestamp__ = '29-Jun-14 : 15:33'


########################################################################################################################
def to_string(data, encoding="ISO-8859-1"):
    """
    Bytes to String
    """
    return str(data.decode(encoding, errors='ignore'))


########################################################################################################################
def to_integer(bytes):
    """
    Decode bytes to integer
    """
    return int.from_bytes(bytes, byteorder='big')


########################################################################################################################
def parse_encoding(encode_byte):
    encoding = 'UTF-8'

    if encode_byte == 0:
        encoding = 'ISO-8859-1'
    elif encode_byte == 1:
        encoding = 'UTF-16'
    elif encode_byte == 2:
        encoding = 'UTF-16BE'
    elif encode_byte == 2:
        encoding = 'UTF-8'

    return encoding


