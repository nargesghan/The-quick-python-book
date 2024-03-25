temperatures=[]
with open('D:\CS internship\step 2\Chapter5\lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

max_temp = max(temperatures)
min_temp = min(temperatures)
mean_temp = sum(temperatures)/len(temperatures)
# we'll need to sort to get the median temp
temperatures.sort()
median_temp = temperatures[len(temperatures)//2]
print("max = {}".format(max_temp))
print("min = {}".format(min_temp))
print("mean = {}".format(mean_temp))
print("median = {}".format(median_temp))
max = 28.2
min = 0.8
mean = 14.848309178743966
median = 14.7
