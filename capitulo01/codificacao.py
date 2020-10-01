
input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
input_str = input_bytes.decode('utf-16')
print(input_str)

out_str = 'We copy you down, Eagle.\n'
out_bytes = out_str.encode('utf-8')

with open('eagle.txt', 'wb') as f:
	f.write(out_bytes)
