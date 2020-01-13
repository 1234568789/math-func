#A collection of my math functions
import math


def __radians__(degrees):
	radians = degrees*(180/math.pi)
	return radians
	#convert degrees to radians
def __degrees__(radians):
	degrees = radians*(math.pi/180)
	return degrees
	#convert radians to degrees
def sqrt(sqval):
	sqrt_val = (sqval)**0.5
	return sqrt_val
	#square root
def fibbonacci(nterms):
	# Program to display the Fibonacci sequence up to n-th term
	# first two terms
	n1, n2 = 0, 1
	count = 0

	# check if the number of terms is valid
	if nterms <= 0:
		print("Please enter a positive integer")
	elif nterms == 1:
		print("Fibonacci sequence upto",nterms,":")
		return n1
	else:
		while count < nterms:
			nth = n1 + n2
			# update values
		n1 = n2
		n2 = nth
		count += 1
		return nth
def den2hex(den_no):
	_hex_ = hex(den_no)
	return _hex_
	#denary to hexadecimal conversion
def hex2den(hex_no):
	hexden = int(hex_no, 16)
	return hexden
	#hexadecimal to denary conversion
def den2bin(den_no):
	binden = bin(den_no)
	return binden
	#denary to binary conversion
def bin2den(bin_no):
	denbin = int(bin_no, 2)
	return denbin
	#binary to denary conversion
def __hpyth__(side_a, side_b):
	_pythval_ = sqrt((side_a**2)+(side_b**2))
	return _pythval_
	#pythagoras' theorem for the hypotenuse
def  __AOPyth__(side_oth, side_hy):
	pythval = sqrt((side_hy**2)-(side_oth**2))
	return pythval
	#pythagoras' theorem for sides other than the hypotenuse
def _in_(number_to_be_indexed, index):
	indexed_no = number_to_be_indexed**index
	return indexed_no
def circarea(radius):
	Area = (float(radius)**2)*math.pi
	return Area
def _diameter_(raidus_):
	diameter_ = raidus_*2
	return diameter_
def _raidus_(diameter):
	raidius = diameter/2
	return raidius
def _circumference_(radius):
	circum = 2*math.pi*radius
	return circum
def triarea(base, perp_height):
	TriArea = (base * perp_height)/2
	return TriArea
def tribase(area, perp_height):
	Base = 2*(area/perp_height)
	return Base
def triheightperp(area, base):
	heightperp = 2*(area/base)
	return heightperp
def __sumofintangles__(n):
	sumofintangles = (n - 2)*180
	return sumofintangles
def __exteriorangles__(n):
	exteriorangles = 360/n
	return exteriorangles
def sin(degrees):
	sine_val = math.sin(__radians__(degrees))
	return sine_val
def cos(degrees):
	cosine_val = math.cos(__radians__(degrees))
	return cosine_val
def tan(degrees):
	tangent_val = math.tan(__radians__(degrees))
	return tangent_val
def __arcsin__(opposite, hypotenuse):
	arcsine = math.arcsine(opposite/hypotenuse)
	return arcsine
def __arccos__(adjacent, hypotenuse):
	arccosine = math.arccosine(adjacent/hypotenuse)
	return arccosine
def __arctan__(opposite, adjacent):
	arctan = math.arctan(opposite/adjacent)
	return arctan
