#import module
import csv

#create file
csvfile = open("trial2.csv", "w")

#create csvwriter
csvwriter = csv.writer(csvfile, delimiter = ",")

#write infomation 10 x
for x in range(100):
    csvwriter.writerow(['1','2', '3', '4'])
    
# write more info
csvwriter.writerow(['a', 'b', 'c', 'd'])

#close file
csvfile.close()