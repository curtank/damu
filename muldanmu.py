from danmufm.fitdanmu import main
from multiprocessing import Pool
import time
def whileapp(url):
	while True:
		main(url)
		time.sleep(1200)
		pass
	
	pass
urls=["http://www.douyu.com/sunyalong",
		"http://www.douyu.com/156277",
		"http://www.douyu.com/633019",
		"http://www.douyu.com/ShinyRuo"
		"http://www.douyu.com/3484"]
pool=Pool()
pool.map(whileapp,urls)
#main(url)
print("finish")