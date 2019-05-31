data = []
count = 0
with open('reviews.txt' , 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data))
print('资料读取完毕，一共有:', len(data), '条信息')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('信息平均长度为:' , sum_len/len(data))

new = []
for d in data:
	if len(d) > 150:
		new.append(d)
print('大于150字符长度的留言有' , len(new) , '条')