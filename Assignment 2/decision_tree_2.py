#-------------------------------------------------------------------------
# AUTHOR: Nathan Pham
# FILENAME: decision_tree_2.py
# SPECIFICATION: Using Decision Tree Classifier
# FOR: CS 4210- Assignment #2
# TIME SPENT: 10/1/2022
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
accuracyList = []

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []
    lowestAccuracy = 1

    #reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #transform the original categorical training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
    # so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    for row in dbTraining:
        temp = []
        for i in range(4):
            if row[i] == "Young" or row[i] == "Myope" or row[i] == "Yes" or row[i] == "Reduced":
                temp.append(1)
            elif row[i] == "Prepresbyopic" or row[i] == "Hypermetrope" or row[i] == "No" or row[i] == "Normal":
                temp.append(2)
            else:
                temp.append(3)
        X.append(temp)

    #transform the original categorical training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
    for row in dbTraining:
        if row[4] == "Yes":
            Y.append(1)
        else:
            Y.append(2)

    #loop your training and test tasks 10 times here
    for i in range (10):

       #fitting the decision tree to the data setting max_depth=3
       clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
       clf = clf.fit(X, Y)

       #read the test data and add this data to dbTest
       #--> add your Python code here
       dbTest = []
       with open("contact_lens_test.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            for column, row in enumerate(reader):
                if column > 0: 
                    dbTest.append(row)

    correct = 0
    incorrect = 0
    for data in dbTest:
           #transform the features of the test instances to numbers following the same strategy done during training,
           #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
           #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
        transformedData = []
        for j in range(5):
            if data[j] == "Young" or data[j] == "Myope" or data[j] == "Yes" or data[j] == "Reduced":
                transformedData.append(1)
            elif data[j] == "Prepresbyopic" or data[j] == "Hypermetrope" or data[j] == "No" or data[j] == "Normal":
                transformedData.append(2)
            else:
                transformedData.append(3)
        class_predicted = clf.predict([transformedData[:-1]])[0]

        #compare the prediction with the true label (located at data[4]) of the test instance to start calculating the accuracy.
        if transformedData[4] == class_predicted:
            correct += 1
        else:
            incorrect += 1

        #find the lowest accuracy of this model during the 10 runs (training and test set)
        accuracy = correct / (correct + incorrect)
        if lowestAccuracy > accuracy:
            lowestAccuracy = accuracy
    accuracyList.append(lowestAccuracy)

    #print the lowest accuracy of this model during the 10 runs (training and test set).
    #your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
print("final accuracy when training on contact_lens_training_1.csv:", accuracyList[0])
print("final accuracy when training on contact_lens_training_2.csv:", accuracyList[1])
print("final accuracy when training on contact_lens_training_3.csv:", accuracyList[2])




