import urllib
import re
import numbers_dict
import datetime

def get_info(xml):
	location_obj = re.search(r"<location>(.*?)</location>", xml)
	if location_obj:
		location = location_obj.group(1)
	else:
		location = ""

	weather_obj = re.search(r"<weather>(.*?)</weather>", xml)
	if weather_obj:
		weather = weather_obj.group(1)
	else:
		weather = ""

	temp_obj = re.search(r"<temp_f>(.*?)</temp_f>", xml)
	if temp_obj:
		temp = temp_obj.group(1)
	else:
		temp = ""

	return(location, weather, temp)

def getChars(temp):
	ascii_chars = []
	temp = temp.split()[0]

	for char in temp:
		if char == ".":
			ref = "dot"
		elif char == " ":
			ref = "space"
		elif char == "-":
			ref = "minus"
		else:
			ref = char
		ascii_chars.append(numbers_dict.numbers()[ref])
	return ascii_chars

def combineAscii(ascii_chars):
	final_str = ""
	line_count = len(ascii_chars[0].split('\n'))

	for x in range(line_count):
		line = ""
		for char in ascii_chars:
			lines = char.split('\n')				
			line += lines[x]
		final_str += line + "\n"
	return final_str

def main(url):
	xml = urllib.urlopen(url).read()

	(location, weather, temp) = get_info(xml)
	ascii_chars = getChars(temp)
	temp_ascii = combineAscii(ascii_chars)
	print "\n{}\n{}\n{}\n{}\n".format(
		datetime.datetime.now(), location, weather, temp_ascii)

if __name__ == '__main__':
	main('http://w1.weather.gov/xml/current_obs/KMSN.xml')