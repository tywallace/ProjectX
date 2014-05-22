def if_cleaning(s):
	cleaninglist = []
	if "(SANITATION BROOM SYMBOL)" in s:
		s = s[s.index("(SANITATION BROOM SYMBOL)")+25:]
		# s = s[:s.index("<")]
		if "TO" in s:
			s = s.replace("TO","-")
		if "=" in s:
			s = s.replace("=","-")
		if "NOON" in s:
			s = s.replace("NOON","12PM")
		if "MIDNIGHT" in s:
			s = s.replace("MIDNIGHT","12AM")

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
		
		if "TUES & FRI" in s:
			day = "Tuesday & Friday"
		if "TUES & F RI" in s:
			day = "Tuesday & Friday"
		elif " SAT " in s:
			day = "Saturday"
		elif "EXCEPT SUN" in s:
			day = "Except Sunday"
		elif "MON TUES THURS FRI":
			day = "Monday, Tuesday, Thursday & Friday"
		elif "MON & THURS":
			day = "Monday & Thursday"
		elif " WED ":
			day = "Wednesday"
		elif " WEDNESDAY ":
			day = "Wednesday"

		
		cleaninglist.append(start.strip())
		cleaninglist.append(end.strip())
		cleaninglist.append(time.strip())
		cleaninglist.append(day.strip())
		
		return cleaninglist 

