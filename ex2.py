#!/usr/bin/python

import pandas as pd


filename = "stats.csv"
name = ['Emp#','YearsOfExp','SalaryinRs.']
data = pd.read_csv(filename,names=name)
trim_data = data.iloc[1:]
trim_data[['Emp#','YearsOfExp','SalaryinRs.']]= trim_data[['Emp#','YearsOfExp','SalaryinRs.']].apply(pd.to_numeric)   

print("Standard Deviation of Years of Experience : ",trim_data["YearsOfExp"].std())
print("Variance of Years of Experience : ",trim_data["YearsOfExp"].var())
print("Standard Deviation of Salary : ",trim_data["SalaryinRs."].std())
print("Variance of Salary : ",trim_data["SalaryinRs."].var())
