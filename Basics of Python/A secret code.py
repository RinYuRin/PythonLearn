def translate(secret_code):
	translation = ""
	
	for letter in secret_code:
		if letter in "Aa":
			translation = translation + "0"
			
		elif letter in "Ee":
			translation = translation + "¶"
			
		elif letter in "Ii":
			translation = translation + "ī"
			
		elif letter in "Oo":
			translation = translation + "ø"
			
		elif letter in "Uu":
			translation = translation + "û"
			
		elif letter in "Bb":
			translation = translation + "1"
			
		elif letter in "Cc":
			translation = translation + "2"
			
		elif letter in "Dd":
			translation = translation + "3"
			
		elif letter in "Ff":
			translation = translation + "4"
		
		elif letter in "Gg":
			translation = translation + "5"
		
		elif letter in "Hh":
			translation = translation + "6"
			
		elif letter in "Jj":
			translation = translation + "7"
		
		elif letter in "Kk":
			translation = translation + "8"
			
		elif letter in "Ll":
			translation = translation + "9"
			
		elif letter in "Mm":
			translation = translation + "!"
		
		elif letter in "Nn":
			translation = translation + "@"
		
		elif letter in "Pp":
			translation = translation + "#"
			
		elif letter in "Qq":
			translation = translation + "$"
			
		elif letter in "Rr":
			translation = translation + "%"
			
		elif letter in "Ss":
			translation = translation + "^"
			
		elif letter in "Tt":
			translation = translation + "&"
			
		elif letter in "Vv":
			translation = translation + "*"
			
		elif letter in "Ww":
			translation = translation + "£"
			
		elif letter in "Xx":
			translation = translation + "¢"
			
		elif letter in "Yy":
			translation = translation + "¥"
			
		elif letter in "Zz":
			translation = translation + "∆"	
				
		else:
			translation = translation + letter
			
	return translation

print(translate(input()))