import os
import csv

folder_name = os.path.join('C:', '\\Users', 'jmose', 'Downloads', 'UDEN201805DATA1-master', 'UDEN201805DATA1-master', 'Week3 - Python', 'Python HW', 'PyBank', 'raw_data')
csvpath1 = os.path.join(folder_name, 'budget_data_1.csv')
csvpath2 = os.path.join(folder_name, 'budget_data_2.csv')
report_path = os.path.join(folder_name, 'report.txt')

with open(csvpath1) as f_in:
	reader = csv.reader(f_in)
	next(reader) #Skip header row
	data = list(reader)

date_column = 0
revenue_column = 1
total_months = len(data)
total_revenue = sum([eval(rows[revenue_column]) for rows in data])
revenue_change = [eval(rows[revenue_column]) for rows in data]
monthly_differences = [eval(data[i+1][revenue_column])-eval(data[i][revenue_column]) for i in range(len(data)-1)]
average_revenue_change = sum(monthly_differences) / len(monthly_differences)
(max_change,max_i) = max((v,i) for i,v in enumerate(monthly_differences))
(min_change,min_i) = min((v,i) for i,v in enumerate(monthly_differences))

output_text = []
output_text.append("Financial Analysis")
output_text.append("----------------------------")
output_text.append("Total Months: {}".format(total_months))
output_text.append("Total Revenue: ${}".format(total_revenue))
output_text.append("Greatest Increase in Revenue: {} (${})".format(data[max_i+1][date_column],max_change))
output_text.append("Greatest Decrease in Revenue: {} (${})".format(data[min_i+1][date_column],min_change))

with open(report_path, "w+") as f_out:
	for line in output_text:
		print(line)
		f_out.write(line)
		f_out.write("\r\n")

