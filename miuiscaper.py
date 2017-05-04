
##############################################
##### http://en.miui.com/thread-96987-1-1.html
##### http://en.miui.com/thread-96987-217-1.html

##############################################

#### STEPS
# 1. take input of page numbers from where to where
# 2. find out how to use bs for finding content
# 3. Write into a html file
####


from bs4 import BeautifulSoup
import urllib
import re
import sys


def main(args):

	start_page_no = int(args[0])
	end_page_no = int(args[1])

	file = open("test.html","w")
	file.write("<html><head></head><link rel='stylesheet' type='text/css' href='miuitemplate.css'><body><center><table border='1' style='width:80%'><tbody>")
	for i in range(start_page_no,end_page_no+1):
		current_link = urllib.urlopen('http://en.miui.com/thread-246333-'+str(i)+'-1.html').read()
		soup = BeautifulSoup(current_link,"html.parser")

		post_content = soup.findAll("td",{"class":"t_f"})
		post_metadata = soup.findAll("em",{"id":re.compile("authorposton*")})
		
		print "done for page "+str(i)

		

		# print "length on a page : "+str(len(post_content))
		# print str(post_metadata)

		for j in range(0,len(post_content)):
			# #main logic
			# print "***********************************"
			# print "j="+str(j)
			# print "post_content = "+str(post_content[j])
			# print "***********************************"
			words_list = str(post_content[j]).split()
			# print words_list
			if len(words_list) < 30:
				continue

			file.write("<tr><td>")
			file.write(str(post_content[j]))
			file.write("</td><td id='info'>")
			file.write(str(post_metadata[j]))
			file.write("</td></tr>")
		

	file.write("</body></html>")
	file.close()
if(len(sys.argv)>1):
    main(sys.argv[1:])
