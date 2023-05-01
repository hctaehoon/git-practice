#TEST python env 
def print_hello():
    animals = ['dog','cat','hamster'] # in one line
    names = [
	'John',
	'Jane',
	'Gil-Dong'
] # W/o trailing comma
    foods=[
	'spagetti',
	'Pizza'] # w/ trailing comma
    for name in names:
      print(name)	
if __name__ == '__main__':
    print_hello()
