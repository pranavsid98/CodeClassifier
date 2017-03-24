import os
import logging

mapping_global = {
	'ZeroDivisionError' : 'Ouch, try checking denominator on line: ',
	'NameError': 'Maybe you didnt define the variable you are tying to access on line ',
	'TypeError': "I think you're mixing up your data types on line ",
	'SyntaxError': 'Check your syntax on line ',
}


w_space = "".ljust(4)
LOG_FNAME = 'logging_example.out'

script = open("hello.py","r")
script_lines = script.readlines()
if not(script_lines[0].startswith("import logging")):
	script_lines.insert(0,"try:\n")
	script_lines.insert(0,"logging.basicConfig(filename=LOG_FNAME, level=logging.DEBUG)\n")
	script_lines.insert(0,"LOG_FNAME = 'logging_example.out'\n")
	script_lines.insert(0,"import logging\n")
	for i in range(len(script_lines)):
		if i > 3:
			script_lines[i] = w_space + script_lines[i]

	script_lines.append("except SyntaxError:\n")
	script_lines.append("    logging.exception('Got syntax error')\n")
	script_lines.append("except:\n")
	script_lines.append("    logging.exception('Got exception')\n")
	script.close()
	script2 = open("hello.py","w")
	script2.truncate()
	script2.writelines(script_lines)
	script2.close()

os.system("cp /dev/null /tmp/logging_example.out")
os.system("python hello.py")

result = open(LOG_FNAME, "r")
lines = result.readlines()
for i in range(len(lines)):
	if lines[i].startswith("Traceback (most"):
		line_num = (lines[i+1].split(" ")[5])
		line_error = lines[i+3].split(":")[0]
		print mapping_global[line_error] + line_num + '\n'
