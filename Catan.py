import CatanDefs
import os
import cmd

# Main Program
if __name__ == '__main__':
	os.system('cls')
	print 'Welcome to Catan!'
	print ''
	CatanDefs.hexName(CatanDefs.location)
	CatanDefs.explore().cmdloop()
	print 'Fare Thee Well!'
