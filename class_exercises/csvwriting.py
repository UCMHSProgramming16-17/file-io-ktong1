#import module
import csv
import math

#create file
csvfile = open("trial2.csv", "w")

#create csvwriter
csvwriter = csv.writer(csvfile, delimiter = ",")

csvwriter.writerow(['a','b','theta in radians'])
#write infomation
for a in range(1, 100):
    for b in range(a, 100):
        theta = math.atan(b/a)
        csvwriter.writerow([a, b, theta])

#close file
csvfile.close()