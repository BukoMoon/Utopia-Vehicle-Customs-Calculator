# Utopia-Vehicle-Customs-Calculator

This was a programming assignment for University.


Task:

Utopia Customs Authority has employed you to develop an application to help their customers calculate the customs for imported vehicles.  The customs value for an imported vehicle is calculated based on the vehicle's market price and engine capacity, according to the following rules:

- Category A (Engine capacity up to 1600 cc): 25% of the vehicle's market price.
- Category B (Engine capacity more than 1600 cc and up to 2000 cc): 50% of the vehicle's market price.
- Category C (Engine capacity more than 2000 cc): 75% of the vehicle's market price.

A depreciation discount can be applied based on the year the vehicle was manufactured. For each previous year, a depreciation discount of 1% of the market price is applied. For example, a vehicle manufactured in 2021 gets no discount. A vehicle manufactured in 2020 gets 1% discount. A vehicle manufactured in 2019 gets 2% discount, and so on. The maximum allowed depreciation discount is 10%.

You are required to design and write an interactive program that prompts the user for the vehicle's market price, engine capacity and manufacture year; and displays the initial customs amount, depreciation discount, and final customs amount. The program should allow the user to calculate the customs again and should continue until the user decides to quit.

Review the sample run below to clearly understand all requirements.

```
Utopia Vehicle Customs Calculator
---------------------------------

Enter the market price: 20000
Enter the engine capacity: 1500
Enter the manufacture year: 2018

Initial customs amount (category A): $5,000
Depreciation discount (3 years): $600
Final customs amount: $4,400


Calculate for another vehicle (y/n)? y

Enter the market price: 35000
Enter the engine capacity: 2000
Enter the manufacture year: 2015

Initial customs amount (category B): $17,500
Depreciation discount (6 years): $2,100
Final customs amount: $15,400


Calculate for another vehicle (y/n)? y

Enter the market price: 21500
Enter the engine capacity: 3600
Enter the manufacture year: 2009

Initial customs amount (category C): $16,125
Depreciation discount (10+ years): $2,150
Final customs amount: $13,975


Calculate for another vehicle (y/n)? n

Have a nice day!
```

**Task 1 (3 marks)**

Draw a flowchart that presents the steps of the algorithm required to perform the task specified. It is recommended to use Draw.io to draw your flowchart.

**Task 2 (12 marks)**

Implement your algorithm in Python. Comment on your code as necessary to explain it clearly. 

**Task 3 (5 marks)**

Select at least three sets of test data that will demonstrate the normal operation of your program; that is, test data that will demonstrate what happens when a valid input is entered. Select two sets of test data that will demonstrate the abnormal operation of your program; that is, test data that will demonstrate what happens when an invalid input is entered.

Set it out in a tabular form as follows: test data type, test data, the reason it was selected, the output expected due to using the test data, and finally a screenshot of the output actually observed when the test data is used. It is important that the output listings (i.e., screenshots) are not edited in any way.
