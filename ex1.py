#!/usr/bin/python

import pandas as pd


filename = "stats.csv"
name = ['Emp#','YearsOfExp','SalaryinRs.']
data = pd.read_csv(filename,names=name)
trim_data = data.iloc[1:]
trim_data[['Emp#','YearsOfExp','SalaryinRs.']]= trim_data[['Emp#','YearsOfExp','SalaryinRs.']].apply(pd.to_numeric)   
print("Mean of Years of Experience : ",trim_data["YearsOfExp"].mean())
print("Median of Years of Experience : ",trim_data["YearsOfExp"].median())
print("Mode of Years of Experience : ",trim_data["YearsOfExp"].mode()[0])
print("Mean of Salary : ",trim_data["SalaryinRs."].mean())
print("Median of Salary : ",trim_data["SalaryinRs."].median())
print("Mode of Salary : ",trim_data["SalaryinRs."].mode()[0])
