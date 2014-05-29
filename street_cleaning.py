def if_cleaning(s):
	cleaninglist = []
	originalline = s

	if "(SANITATION BROOM SYMBOL)" in s:
		s = s[s.index("(SANITATION BROOM SYMBOL)")+25:]

		if "TO" in s:
			s = s.replace("TO","-")
		if "=" in s:
			s = s.replace("=","-")
		if "--" in s:
			s = s.replace("--","-")
		if "NOON" in s:
			s = s.replace("NOON","12PM")
		if "MIDNIGHT" in s:
			s = s.replace("MIDNIGHT","12AM")
		if "8AM 11AM" in s:
			s = s.replace("8AM 11AM", "8AM - 11AM")

		if "MONDAY-FRIDAY" in s:
			day = "Monday - Friday"

		elif "TUES & FRI" in s:
			day = "Tuesday & Friday"
		
		elif "TUES & F RI" in s:
			day = "Tuesday & Friday"
		
		elif "TUES THURS SAT" in s:
			day = "Tuesday, Thursday & Saturday"
		
		elif "EXCEPT SUN" in s:
			day = "Monday - Saturday"
		
		elif "MON TUES THURS FRI" in s:
			day = "Monday, Tuesday, Thursday & Friday"
		
		elif "MON & THURS" in s:
			day = "Monday & Thursday"
		
		elif "MON WED FRI" in s:
			day = "Monday, Wednesday & Friday"
		
		elif "MON&THURS" in s:
			day = "Monday & Thursday"
		
		elif "MON &THURS" in s:
			day = "Monday & Thursday"

		elif "MONDAY THURSDAY" in s:
			day = "Monday & Thursday"

		elif "TUES& THURS" in s:
			day = "Tuesday & Thursday"
		
		elif "TUESDAY THURSDAY" in s:
			day = "Tuesday & Thursday"

		elif "TUESDAY FRIDAY" in s:
			day = "Tuesday & Friday"

		elif " WED " in s:
			day = "Wednesday"
		
		elif " WEDNESDAY " in s:
			day = "Wednesday"

		elif " WENESDAY " in s:
			day = "Wednesday"
		
		elif " SAT " in s:
			day = "Saturday"
	
		elif " SATURDAY " in s:
			day = "Saturday"

		elif " THURS " in s:
			day = "Thursday"

		elif " THURSDAY " in s:
			day = "Thursday"

		elif " MON" in s:
			day = "Monday"

		elif " FRI" in s:
			day = "Friday"

		elif " FRIDAY " in s:
			day = "Friday"

		elif " TUES" in s:
			day = "Tuesday"

		elif " SUN " in s:
			day = "Sunday"

		elif " SUNDAY " in s:
			day = "Sunday"
		else:
			day = "Everyday"

		start = s[:s.index("-")]
		s = s[len(start)+1:]
		
		start = start.strip()
		if "AM" in start:
			start = start[:-2]
		elif "PM" in start:
			start = start[:-2]
		
		end = s[:s.index("M")-1]
		s = s[len(end):]
		
		time = s[:2]
		s = s[len(time):]
				
		cleaninglist.append(start.strip())
		cleaninglist.append(end.strip())
		cleaninglist.append(time.strip())
		cleaninglist.append(day.strip())

		return cleaninglist 