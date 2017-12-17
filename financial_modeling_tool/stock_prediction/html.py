fn = "content_for_inshorts.txt"

file = open(fn, "r")

of = open("daal.txt","w")

count = 0 
for line in file:

	print (line)

	if line is '\n':
		count = 0
		continue

	elif count == 0:
		line = '<h3>'+line+'</h3>'
		count = count + 1

	elif count == 1:
		line = '<p>'+line+'</p>'


	of.write(line)


