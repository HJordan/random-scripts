from PIL import Image
import urllib, cStringIO

# Set up some basic variables
max_rows = 11
max_cols = 21

plate_width = 850 
plate_height = 850

# Create the image to hold the plates together
final_image = Image.new('RGBA', [max_cols * plate_width, max_rows * plate_height], 'white')

# Itterate over the rows and columns
for row in xrange(1, max_rows+1) :
	for col in xrange(1, max_cols+1) :
		# Define and area where the plate fits in the final image
		current_plate_area = [ 	((col - 1) * plate_width) ,
								((row - 1) * plate_height) ,
								(col * plate_width) ,
								(row * plate_height) ]

		# Get the plate for the current row,col position
		current_plate = urllib.urlopen(
			'http://web.ccpgamescdn.com/eve_com/monument/plate_%s_%s.jpg' %(row, col))

		# There is a rectangle of missing plates where the rest of the monument sits
		# This means otherwise valid plates are missing, so we check if we got the image
		# before we try to stick it into the final image.
		if current_plate.getcode() == 200:
			# Loads the image and pastes it into the area defined above
			tmp = Image.open(cStringIO.StringIO(current_plate.read()))
			final_image.paste(tmp, current_plate_area)
			print ( 'plate %s , %s pasted' %(row, col))
		else:
			print ( 'plate %s , %s omitted' %(row, col))

#Now save it to disk. Pillow knows to save as png if it has the extension.
print ('Image compiled, saving...')
final_image.save('mounumentLarge.png')
print ('Saved!')
