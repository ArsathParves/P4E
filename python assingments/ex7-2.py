# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475(eg)
# Count these lines and extract the floating point values from each of the lines and compute the average of those
# values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count=0
sum=0.0
average=0.0

fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find('0')
    num=line[pos:pos+6]
    fnum=float(num)
    count=count+1
    sum=sum+fnum
    average=sum/count
    print(fnum)
#print('Total lines:',count)
#print('Total sum:',sum)
print('Average spam confidence:',average)
