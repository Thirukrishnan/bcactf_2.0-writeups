cipher="VKRXOG_LW_KDYH_EHHQ_YLJHQHUH_LQVWHDG"
msg=" "
for shift in range(1,50):
	msg=" "
	for i in range(0,len(cipher)):
		org=ord(cipher[i])
		if(org >=97 and org<=122):
			if(org-shift>=97):
				mov=org-shift
				msg+=chr(mov)
			else:
				mov=26+org-shift
				msg+=chr(mov)
		elif(org>=65 and org<=90):
			if(org-shift>=65):
				mov=org-shift
				msg+=chr(mov)
			else:
				mov=26+org-shift
				msg+=chr(mov)
		else:
			msg+=cipher[i]
	print(msg+"\n")

