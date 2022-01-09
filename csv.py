#reading the csv file
text = open("Employeedata.csv", "r")
#join() method combines all contents of Employeedata.csv and 
#form as a string
text = ' '. join([i for i in text])
#search and replace contents
text = text.replace("helpinghands.cm", "handsinhands.org")
#output .csv is the outputfile opened to write mode
x = open("output.csv", "w")
#all the replaced text is written in the output.csv file
x.writelines(text)
x.close