import json
filename='./156277/1488700134gift.json'
fileo=open(filename)
for line in fileo:
	jsonformat=json.loads(line)
	if '澜' in jsonformat["origncontent"]:
		print (jsonformat)
		pass