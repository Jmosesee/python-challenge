import os
import csv

file1 = 'budget_data_1.csv'
file2 = 'budget_data_2.csv'
folder_name = os.path.join('C:', '\\Users', 'jmose', 'Downloads', 'UDEN201805DATA1-master', 'UDEN201805DATA1-master', 'Week3 - Python', 'Python HW', 'PyBank', 'raw_data')
report_path = os.path.join(folder_name, 'report.txt')

date_column = 0
revenue_column = 1
month_column = 0
year_column = 1

def read_revenue_data(filename):
	csvpath = os.path.join(folder_name, filename)
	with open(csvpath) as f_in:
		reader = csv.reader(f_in)
		next(reader) #Skip header row
		return [[x[date_column],eval(x[revenue_column])] for x in reader] #Inline Cleaning)

def analyze_and_output_revenue_data(revenue_data, filename):
	total_months = len(revenue_data)
	total_revenue = sum([rows[revenue_column] for rows in revenue_data])
	revenue_change = [rows[revenue_column] for rows in revenue_data]
	monthly_differences = [revenue_data[i+1][revenue_column]-revenue_data[i][revenue_column] for i in range(len(revenue_data)-1)]
	average_revenue_change = sum(monthly_differences) / len(monthly_differences)
	(max_change,max_i) = max((v,i) for i,v in enumerate(monthly_differences))
	(min_change,min_i) = min((v,i) for i,v in enumerate(monthly_differences))

	output_text = []
	output_text.append("Financial Analysis for {}".format(filename))
	output_text.append("----------------------------")
	output_text.append("Total Months: {}".format(total_months))
	output_text.append("Total Revenue: ${}".format(total_revenue))
	output_text.append("Average Revenue Change: ${}".format(average_revenue_change))
	output_text.append("Greatest Increase in Revenue: {} (${})".format(revenue_data[max_i+1][date_column],max_change))
	output_text.append("Greatest Decrease in Revenue: {} (${})".format(revenue_data[min_i+1][date_column],min_change))

	with open(report_path, "w+") as f_out:
		for line in output_text:
			print(line)
			f_out.write(line)
			f_out.write("\r\n")

#It turns out that merging the two datasets is actually not required, but since had already started on it, here it is as a bonus:
def scrub_dates(revenue_data):
	separator = '-'
	dates = [row[date_column].split(separator) for row in revenue_data]
	scrubbed_dates = [separator.join(date) if len(date[year_column]) <= 3 else separator.join([date[month_column], date[year_column][2:]]) for date in dates]
	return [list(row) for row in zip(scrubbed_dates, [row[revenue_column] for row in revenue_data])]

#merge list2 into list1 and return list1
def merge_lists(list1, list2):
	list1_keys = [row1[date_column] for row1 in list1]
	for row2 in list2:
		if row2[date_column] in list1_keys:
			list1[list1_keys.index(row2[date_column])][revenue_column] += row2[revenue_column]
		else:
			list1.append(row2)
			list1_keys.append(row2[date_column])
	return list1

analyze_and_output_revenue_data(read_revenue_data(file1), file1)
print("")
print("")
analyze_and_output_revenue_data(read_revenue_data(file2), file2)

merged = merge_lists(scrub_dates(read_revenue_data(file2)), scrub_dates(read_revenue_data(file1)))

print("")
print("")
print("As a bonus, I also combined the two files to yield the following combined revenue:")
for row in merged:
	print (row)
print("")
print("")

analyze_and_output_revenue_data(merged, "combined")

