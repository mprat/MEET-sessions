import io
import sys

if len(sys.argv) != 2:
	print "type the name of the notebook as the command-line argument"
else:
	notebook = sys.argv[1]
	path = notebook[:-6] + '.slides.html'
	flag = u'@media print{*{text-shadow:none !important;color:#000 !important'
	 
	with io.open(path, 'r') as in_file:
		data = in_file.readlines()
		for i, line in enumerate(data):
			if line[:64] == flag:
				data[i] = data[i].replace('color:#000 !important;', '')
	 
	with io.open(path, 'w') as out_file:
		out_file.writelines(data)
	 
	print "You can now print your slides"
