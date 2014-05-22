def convert_word_to_num(street):
	num_dict = {"first":"1","second":"2","third":"3","fourth":"4","fifth":"5","sixth":"6","seventh":"7","eighth":"8","ninth":"9","tenth":"10","eleventh":"11","twelfth":"12","thirteenth":"13", "1st":"1","2nd":"2","3rd":"3","4th":"4","5th":"5","6th":"6","7th":"7","8th":"8","9th":"9","10th":"10","11th":"11","12th":"12","13th":"13"}
	for key in num_dict:
		if key in street:
			street = street.replace(key,num_dict[key])
	return street