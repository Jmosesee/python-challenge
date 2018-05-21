import os
import csv

folder_name = os.path.join('C:', '\\Users', 'jmose', 'Downloads', 'UDEN201805DATA1-master', 'UDEN201805DATA1-master', 'Week3 - Python', 'Python HW', 'PyPoll', 'raw_data')
csvpath1 = os.path.join(folder_name, 'election_data_1.csv')
csvpath2 = os.path.join(folder_name, 'election_data_2.csv')
report_path = os.path.join(folder_name, 'report.txt')

with open(csvpath1) as f_in:
	reader = csv.reader(f_in)
	next(reader) #Skip header row
	data = list(reader)

voter_id_column = 0
county_column = 1
candidate_column = 2
vote_list = [row[candidate_column] for row in data]
total_votes = len(vote_list)
candidate_list = list(set([row[candidate_column] for row in data]))
vote_count = [vote_list.count(candidate) for candidate in candidate_list]
vote_percentage = [c/sum(vote_count) for c in vote_count]
(max_votes, max_i) = max((v,i) for i,v in enumerate(vote_count))
winner = candidate_list[max_i]

output_text = []
output_text.append("Election Results")
output_text.append("----------------------------")
output_text.append("Total Votes: {}".format(total_votes))
output_text.append("----------------------------")
for i,v in enumerate(candidate_list):
	output_text.append("{}: {}% ({})".format(candidate_list[i], vote_percentage[i], vote_count[i]))
output_text.append("----------------------------")
output_text.append("Winner: {}".format(winner))

with open(report_path, "w+") as f_out:
	for line in output_text:
		print(line)
		f_out.write(line)
		f_out.write("\r\n")

