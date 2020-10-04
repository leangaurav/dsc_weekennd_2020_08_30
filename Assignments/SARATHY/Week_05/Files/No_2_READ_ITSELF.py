import sys
print(sys.argv)
with open(sys.argv[0],'r') as f:
	print(f.read())


