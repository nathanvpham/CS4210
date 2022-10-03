#-------------------------------------------------------------------------
# AUTHOR: Nathan Pham
# FILENAME: naive_bayes.py
# SPECIFICATION: Using Naive Bayes Classifier
# FOR: CS 4210- Assignment #2
# TIME SPENT: 10/1/2022
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
import csv
from sklearn.naive_bayes import GaussianNB

#reading the training data in a csv file
weatherTraining = []
with open('weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: # skipping the header
            weatherTraining.append(row)

#transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, so X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
#--> add your Python code here
X = []
for row in weatherTraining:
    temp = []
    for i in range(1, 5):
        if row[i] == "Sunny" or row[i] == "Hot" or row[i] == "High" or row[i] == "Weak":
            temp.append(1)
        elif row[i] == "Overcast" or row[i] == "Mild" or row[i] == "Normal" or row[i] == "String":
            temp.append(2)
        else:
            temp.append(3)
    X.append(temp)

#transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> add your Python code here
Y = []
for row in weatherTraining:
    if row[-1] == "Yes":
        Y.append(1)
    else:
        Y.append(2)

#fitting the naive bayes to the data
clf = GaussianNB()
clf.fit(X, Y)

#reading the test data in a csv file
#--> add your Python code here
weatherTest = []
with open('weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: # skipping the header
            weatherTest.append(row)
X_test = []
for row in weatherTest:
    temp = []
    for i in range(1, 5):
        if row[i] == "Sunny" or row[i] == "Hot" or row[i] == "High" or row[i] == "Weak":
            temp.append(1)
        elif row[i] == "Overcast" or row[i] == "Mild" or row[i] == "Normal" or row[i] == "String":
            temp.append(2)
        else:
            temp.append(3)
    X_test.append(temp)            
#printing the header os the solution
print ("Day".ljust(15) + "Outlook".ljust(15) + "Temperature".ljust(15) + "Humidity".ljust(15) + "Wind".ljust(15) + "PlayTennis".ljust(15) + "Confidence".ljust(15))

#use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
predictions = clf.predict(X_test)
for i, row in enumerate(X_test):
    confidence = clf.predict_proba([row])[0]
    # Yes == 1
    if confidence[0] >= 0.75 and predictions[i] == 1:
        print(weatherTest[i][0].ljust(15) + weatherTest[i][1].ljust(15) + weatherTest[i][2].ljust(15) + weatherTest[i][3].ljust(15) + weatherTest[i][4].ljust(15) + "Yes".ljust(15) + str(confidence[0]).ljust(15))


