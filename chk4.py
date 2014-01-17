import csv
import sys

f = open(sys.argv[1], 'wt')
try:
    writer = csv.writer(f)
    writer.writerow( ('Title 1', 'Title 2') )
    for i in range(1500000):
        writer.writerow( (i+1, (i+100)*.123456789))
finally:
    f.close()

print open(sys.argv[1], 'rt').read()