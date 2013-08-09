
import requests
import xml.etree.cElementTree as et


def readData():
	f = open("/Users/pranavr/Desktop/MIT/MEng/vizmaps_proj/public/mass data.txt")
	out = open("/Users/pranavr/Desktop/MIT/MEng/vizmaps_proj/public/SomervilleData.txt", 'w')
 	lines = f.readlines()

 	count = 0

 	for line in lines:
 		if line[0] == '+':
 			line = line.split(",")
 			lat = float(line[0][1:len(line[0])])
 			lng = float(line[1])
 			pop = line[2]


 			url = 'http://api.geonames.org/findNearbyPostalCodes?lat='+str(lat)+'&lng='+str(lng)+'&maxRows=1&username=pranav'
			xml = requests.get(url)
			content = None
			if (xml.status_code == 200):
				#print xml.content
				content =  xml.content
			else:
				print "RequestError: " + xml.status_code


			parse = et.XML(content)

			#print content
			place = parse.find("code").find("adminName2").text


			if place =="Somerville":	
				out.write('{lat:'+str(lat)+', lng:'+str(lng)+', count:'+ str(pop)+ '},')
			else:
				print("not Somerville " + place + ".........." + str(count) + " out of about " + str(len(lines)))
			count+=1





readData()