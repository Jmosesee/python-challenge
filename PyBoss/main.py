import os
import csv
from us_state_abbrev import us_state_abbrev

input_file1 = 'employee_data1.csv'
input_file2 = 'employee_data2.csv'
output_file1 = 'reformatted_employee_data1.csv'
output_file2 = 'reformatted_employee_data2.csv'

folder_name = os.path.join('C:', '\\Users', 'jmose', 'Downloads', 'UDEN201805DATA1-master', 'UDEN201805DATA1-master', 'Week3 - Python', 'Python HW', 'PyBoss', 'raw_data')

def read_employee_data(filename):
	csvpath = os.path.join(folder_name, filename)
	with open(csvpath) as f_in:
		reader = csv.reader(f_in)
		next(reader) #Skip header row
		return list(reader)

def reformat_employee_data(data):
	formatted_employee_data = []
	for employee in data:
		emp_id = employee[0]
		first_name = employee[1].split(' ')[0]
		last_name = employee[1].split(' ')[1]
		DOB_year = employee[2].split('-')[0]
		DOB_month = employee[2].split('-')[1]
		DOB_day = employee[2].split('-')[2]
		SSN = employee[3]
		redactedSSN = ''.join('*' if i in[0,1,2,4,5] else v for i,v in enumerate(SSN))
		state_abbrev = us_state_abbrev[employee[4]]
		formatted_employee_data.append([emp_id,
			first_name,
			last_name,
			"{}/{}/{}".format(DOB_month,DOB_day,DOB_year),
			redactedSSN,
			state_abbrev])

	return formatted_employee_data

def write_employee_data(data, filename):
		outputpath = os.path.join(folder_name, filename)
		with open(outputpath, "w+") as f_out:
			f_out.write("Emp ID,First Name,Last Name,DOB,SSN,State")
			f_out.write("\r\n")
			for line in data:
				#print(','.join(line))
				f_out.write(','.join(line))
				f_out.write("\r\n")


write_employee_data(reformat_employee_data(read_employee_data(input_file1)),output_file1) 
write_employee_data(reformat_employee_data(read_employee_data(input_file2)),output_file2)
