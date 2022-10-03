#-------------------------------------------------------------------------
# AUTHOR: Nathan Pham
# FILENAME: knn.py
# SPECIFICATION: Using KNN Classifier
# FOR: CS 4210- Assignment #2
# TIME SPENT: 10/1/2022
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

correct = 0
incorrect = 0


#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):

    #add the training features to the 2D array X and remove the instance that will be used for testing in this iteration.
    #For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid warning messages
    
    #transform the original training classes to numbers and add them to the vector Y. Do not forget to remove the instance that will be used for testing in this iteration.
    #For instance, Y = [1, 2, ,...]. Convert values to float to avoid warning messages

    #--> add your Python code here
    # X =
    X = []
    for j, row in enumerate(db):
        if i != j:
            temp = []
            for n in row[:-1]:
                temp.append(int(n))
            X.append(temp)
    # Y =
    Y = []
    for j, row in enumerate(db):
        if i != j:
            if row[-1] == "+":
                Y.append(1)
            else:
                Y.append(2)
    #testSample =
    testSample = [int(instance[0]), int(instance[1])]

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    class_predicted = clf.predict([testSample])[0]

    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    test = 0
    if instance[2] == "+":
        test = 1
    else:
        test = 2
    if class_predicted == test:
        correct += 1
    else:
        incorrect += 1
#print the error rate
#--> add your Python code here
errorRate = incorrect / (correct + incorrect)
print(errorRate)





