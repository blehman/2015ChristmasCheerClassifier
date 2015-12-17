2nd Annual Christmas Cheer Classifer
2015 Dec 16
drskippy@twitter.com
------------------------------------------------------------------

Objective:
----------
Correctly identify handwritten images of numbers from 
  the test set.

Two image files contain 28x28 pixel, 1-byte grey-scale images. One labels 
  file contains the labels for the training data. Data Set:
    9912422  train-images.gz
    28881    train-labels.gz
    1648877  test-images.gz

The utility images.py illustrates how to read the binary file format (and
  displays the images as simple text art).

Teams:
------
  1-3 people per team
  At least 1 DDIS team member per team
  Name your team and keep the same name for the competition

Duration:
---------
  2015 Dec 16 Now
  2015 Dec 30 at 1 pm MT

Submissions:    
------------
  If you don't submit a lebel file, you can't win!
  You can submit as many test-labels files as you wish and at any time you
    wish.
  Your entry will be scored as quickly as I can get to it. I will email
    your results to you and add them to the leader board.
  The format of a submission is a text file (do not binary pack your submissions
    in the format of the train-labels.gz file.
  The format should have the
    header and body as shown below. Comment lines are optional.

Example Submission File
-----------------------

        ####### submission file
        # comment
        # comment
        <team name, make this consistent across all submissions. This will appear in the leader board.>
        <timestamp of sumbission in format 2015-12-xxT00:00:00>
        <submission name-anything you want. This will appear in the leader board.>
        # data is 1 integer per row. there should be 10000 of them.
        3
        2
        6
        1
        0
        <...>

(Also, see included "random.submission" file.)

Example Output
--------------

score.py output from key.submission:

##################################################
#  Dr Skippy
#  2015-12-16 11:00:14.039316
#  Key
##################################################
total sumbission size = 10000
total size check = True
##################################################
SCORE = 10000 (100.00000%)
##################################################
    0: pred =  980,  actual =  980 (100.0000%)
    1: pred = 1135,  actual = 1135 (100.0000%)
    2: pred = 1032,  actual = 1032 (100.0000%)
    3: pred = 1010,  actual = 1010 (100.0000%)
    4: pred =  982,  actual =  982 (100.0000%)
    5: pred =  892,  actual =  892 (100.0000%)
    6: pred =  958,  actual =  958 (100.0000%)
    7: pred = 1028,  actual = 1028 (100.0000%)
    8: pred =  974,  actual =  974 (100.0000%)
    9: pred = 1009,  actual = 1009 (100.0000%)
##################################################

"2015-12-16 11:00:14.039316"	"Dr Skippy"	"Key"	"1.0"	""	"10000"	"1.0"	"0"	"0.0"	"1.0"	"1.0"	"1.0"	"1.0"	"1.0"	"1.0"	"1.0"	"1.0"	"1.0"	"1.0"	"10000"	"True"	"2015-12-16 11:03:51.897223"
<eof>

What's fair game?
-----------------

This data set is available from a web site. Please do not download the key
  file from that web site.
In general, you should be assembling a solution from "data science-y"
  components rather than adapting an existing end-to-end OCR solution
  to this particular data set.
Prepared to explain in detail the methods and techniques employed
  without booing or fruits being thrown.
Don't build machine learning alogrithms from scratch (unless you invent
  something brand new.)
Your own Twitter-funded EC2 instance.

