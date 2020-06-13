from PIL import Image, ImageDraw
import sys
import random
'''
Set some arbitrary rules and draw the patterns.
'''

counter = 0

d = {"left": None, "left-up": None, "up": None, "right-up": None, 
		"right": None} # String art for pixel surrounding

# Rules string art
rules = [({"left": '-', "left-up": '-', "up": '*', "right-up": '-', "right": '-'}, 'rule_one'),
		 ({"left": '-', "left-up": '-', 'up': '-', "right-up": '*', "right": '-'}, 'rule_two'), 
		 ({"left": '-', "left-up": '*', "up": '-', "right-up": '-', "right": '-'}, 'rule_three')]



width = int(sys.argv[1])
height = int(sys.argv[2])
name = str(sys.argv[3])

# String map generation
def textmap(color, n):
	global d
	if color == (0, 0, 0):
		d[list(d.keys())[n]] = '-'
	else:
		d[list(d.keys())[n]] = '*'

# Comparing rules and adding pixels
def rule_compare(current_textmap, coords, imagepil):
	for x in range(len(rules)):
		if d == rules[x][0]:
			if rules[x][1] == 'rule_one':
				imagepil.putpixel(coords, (0, 0, 255))
				imagepil.putpixel((coords[0]+1, coords[1]), (0, 0, 255))
				imagepil.putpixel((coords[0]-1, coords[1]), (0, 0, 255))
			if rules[x][1] == 'rule_two' or rules[x][1] == 'rule_three':
				imagepil.putpixel(coords, (0, 0, 255))


coord_manip = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0)]# Coordinate 'manipulators' used to check area around pixels
img = Image.new("RGB", (width, height), (0,0,0))
drw = ImageDraw.Draw(img)
img.putpixel((random.randrange(width), 0), (0, 0, 255))# Randomly placed first integer

# Iterating to each pixel
for y in range(1, height):
	for x in range(width-1):
		counter += 1
		d = {"left": None, "left-up": None, "up": None, "right-up": None, "right": None}		
		if x!=0 and x!=width and img.getpixel((x,y)) == (0, 0, 0):
			for n in range(len(coord_manip)):# Checking 5 pixels around pixel
				textmap(img.getpixel((x+coord_manip[n][0], y+coord_manip[n][1])), n)# Get color using manipulation list to create string map
				rule_compare(d, (x, y), img)# Compare rules
		

		
		print("Pixels Scanned: " + str(counter), end="\r"), # Pixel counter


img.save("E:/PythonScripts/General/SimpleCA/%s.png" % name)
