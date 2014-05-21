def if_cleaning(s):
	print s
	cleaninglist = []
	if "(SANITATION BROOM SYMBOL)" in s:
		s = s[s.index("(SANITATION BROOM SYMBOL)")+25:]
		s = s[:s.index("<")]
		if "TO" in s:
			s = s.replace("TO","-")
		print s
		
		start = s[0:s.index("-")]
		s = s[len(start):]
		print s
		end = s[s.index("-")+1:s.index(" ")+1]
		
		if ":" not in end:
			end = end[:-3]
		s = s[len(start)+len(end)+1:]
		print "time " + s
		time = s[:2]
		
		if "&" in s:
			day1len = s.index("&")
			day1 = s[2:day1len]
			day2 = s[day1len+1:]
		
		day1 = s[2:]
		day2 = ""
		
		cleaninglist.append(start.strip())
		cleaninglist.append(end.strip())
		cleaninglist.append(time.strip())
		cleaninglist.append(day1.strip())
		cleaninglist.append(day2.strip())
		
		print cleaninglist
		return cleaninglist 

