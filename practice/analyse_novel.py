# with...as 自动调用close()方法
with open('Cambridge_China_History_UTF-8.txt',encoding='utf-8',errors='ignore') as f:
	cont = [line.strip() for line in f.readlines() if line.strip()]
	
#for c in cont[10:50]:
#	print(c)
   
names = ['毛','周','邓','朱','费']   
   
def find_main_characters(num = 3):
	novel = ''.join(cont)
	count = []
	for name in names:
		count.append([name, novel.count(name)])
		count.sort(key = lambda v : v[1], reverse=True)
			
	return count[:num]       
	
print(find_main_characters())















