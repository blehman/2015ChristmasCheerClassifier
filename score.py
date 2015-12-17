#!/usr/bin/env python
import fileinput
import struct
import sys

# read the labels from binary file
label_names = ["./private/test-labels.gz"]
g = fileinput.FileInput(label_names, openhook=fileinput.hook_compressed)
# grab the first chunk of data for header info
x = g.next()
head = []
for i in range(2):
    head.append(struct.unpack(">I", x[4*i:4*i+4])[0])
magic, n_labels = head
print "magic={}\nlabels={}".format(*head)
# start reading the lables
# unsigned binary ints - 1 byte each
labels = []
j = 8 # byte index on current chunk
while len(labels) < n_labels:
    try:
        val = struct.unpack("B", x[j])[0]
    except IndexError:
        # read a new chuck from file
        x = f.next()
        j = 0
        val = struct.unpack("B", x[j])[0]
    labels.append(val)
    j += 1

sub_file = sys.argv[1]
header = []
data = []
i_data_counts = {x:0 for x in range(10)}
with open(sub_file, "rb") as f:
    for x in f:
        if x.startswith("#"):
            continue
        if len(header) < 3:
            header.append(x.strip())
        else:
            i_data_counts[int(x)] += 1
            data.append(int(x))

total = 0
n_correct = 0
i_correct = {x:0 for x in range(10)}
for x,y in zip(data, labels):
    total += 1
    if x == y:
        n_correct += 1
        i_correct[x] += 1


print "#"*50
for x in header:
    print "#  {}".format(x)
print "#"*50
print "total sumbission size = {}".format(total)
print "total size check = {}".format(total == len(labels))
print "#"*50
print "SCORE = {} ({:.5%})".format(n_correct, float(n_correct)/total)
print "#"*50
for y in i_correct:
    print "    {}: pred = {:4},  actual = {:4} ({:.4%})".format(y, i_correct[y], i_data_counts[y], float(i_correct[y])/i_data_counts[y])
print "#"*50

#
import datetime
print
print
print '"' + '"\t"'.join([str(j) for j in [
          header[1]
        , header[0]
        , header[2]
        , float(n_correct)/total
        , ""
        , n_correct
        , float(n_correct)/total
        , len(labels) - n_correct
        , float(len(labels) - n_correct)/total
        , float(i_correct[0])/i_data_counts[0]
        , float(i_correct[1])/i_data_counts[1]
        , float(i_correct[2])/i_data_counts[2]
        , float(i_correct[3])/i_data_counts[3]
        , float(i_correct[4])/i_data_counts[4]
        , float(i_correct[5])/i_data_counts[5]
        , float(i_correct[6])/i_data_counts[6]
        , float(i_correct[7])/i_data_counts[7]
        , float(i_correct[8])/i_data_counts[8]
        , float(i_correct[9])/i_data_counts[9]
        , len(labels)
        , len(labels) == len(data)
        , datetime.datetime.now()
        ]]) + '"'

###
#print # key
#print "Dr Skippy"
#print datetime.datetime.now()
#print "Key"
#for x in labels:
#    print x
