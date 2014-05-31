def convert_word_to_num(street):
	num_dict = {"FIRST":"1","SECOND":"2","THIRD":"3","FOURTH":"4","FIFTH":"5","SIXTH":"6","SEVENTH":"7","EIGHT":"8","NINTH":"9","TENTH":"10","ELEVENTH":"11","TWELFTH":"12","THIRTEENTH":"13", "1ST":"1","2ND":"2","3RD":"3","4TH":"4","5TH":"5","6TH":"6","7TH":"7","8TH":"8","9TH":"9","10TH":"10","11TH":"11","12TH":"12","13TH":"13"}
	for key in num_dict:
		if key in street:
			street = street.replace(key,num_dict[key])
	return street