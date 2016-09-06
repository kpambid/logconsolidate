import datetime

def print_lines(input, output):
	now = datetime.datetime.now()
	date = now.strftime('%-d' + '-' + '%b' + '-' + '%Y')

    # Opens input and output file
	with open(input, 'r') as file, open(output, 'w') as fileo:

		lines = file.read().splitlines()
		
		# Search the current date in every line
		for line in lines:
			found = line.find(date)
			if found > 0:
				fileo.write(line + "\n")

		fileo.close()	
		file.close()

file = raw_input("Enter file name:")
fileo = raw_input("Enter output file:")
print_lines(file,fileo)
