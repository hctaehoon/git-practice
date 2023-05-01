#TEST python env 
def print_hello():
    animals = ['dog','cat','hamster','tiger'] # in one line
    names = [
	'John',
	'Jane',
	'Gil-Dong',
	'Dong-eun',
	'Tae-Hoon',
] # W/ trailing comma
    foods=[
	'spagetti',
	'Pizza',
	'bibimbob'] # w/o trailing comma
    for name in names:
      print(name)	
if __name__ == '__main__':
    print_hello()
