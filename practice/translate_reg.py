# with...as 自动调用close()方法
with open('reg_addr.dat',encoding='gbk',errors='ignore') as f:
	addr = [line.strip() for line in f.readlines() if line.strip()]
	
with open('reg_data.dat',encoding='gbk',errors='ignore') as f:
	data = [line.strip() for line in f.readlines() if line.strip()]

reg_addr = []	
for c in addr:
	reg_addr.append('reg[0x' + c + ']')
   
print(reg_addr[:5])
 
reg_data = []
for c in data:
	reg_data.append(' = 0x' + c)
	
print(reg_data[:5]) 
	
output = []
with open('output.log', 'w') as f:
	for idx in range(2, len(reg_addr)):
		output.append(reg_addr[idx] + reg_data[idx])
		f.write(output[idx - 2])
		f.write('\n')
   
 















