# with...as 自动调用close()方法
with open('err_log.txt',encoding='gbk',errors='ignore') as f:
	cont = [line.strip() for line in f.readlines() if line.strip()]
	
for c in cont:
	if c.find("input file path") != -1 or \
		 c.find("error count") != -1:
		print(c)
   
   
   
   
 















