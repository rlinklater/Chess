# Function to take in a text file
# with coordinates in the format
# x.K(x, y) 			// For PlayerX King
# x.R(x, y)			// For PlayerX Rook
# y.K(x, y) 			// For PlayerY King

Debug = True

workfile = "testCase.txt"

# Helper Function
# Checks if provided coordinate 
# falls within a legal chessboard
# range: 8X8		
def validCoord(l):
	if ((int(l[4])	>= 1) and (int(l[4]) <= 8)) and ((int(l[6])	>= 1) and (int(l[6]) <= 8)):
		return True # Coordinate is valid
	else:
		print("Coordinate out of range(1-8)")
		return False # Coordinate is invalid
	

def FileRead(wf):
	Coordinates = []
	with open(wf, 'r') as f:
		if Debug:
			print("{} successfully opened".format(wf))
		
		# Loop to iterate through each line in the provided text file
		# Assumes lines in the form: p.cp(x,y)		where p is the character
		#		representing the player(x, y), cp is the character representing the
		#		chess piece(K for king, R for rook), and (x,y) are the coordinates 
		#		of the chess piece on the chess board(1-8).
		s = f.read()
		s2 = s.replace(',', ' ').split()
		for line in s2:
			if Debug:
				print(line)
			if line[0] == "x":
				# PlayerX piece coordinate
				if line[2].upper() == "K":
					# PlayerX - King Piece
					if validCoord(line):
						xK = (line[4], line[6]) # Creates tuple for PlayerX's King
						Coordinates.append(xK)
				elif line[2].upper() == "R":
					#		PlayerX - Rook Piece
					if validCoord(line):
						xR = (line[4], line[6])	#		Creates tuple for PlayerX's Rook
						Coordinates.append(xR)	
				else:
					# Print "Unrecognized piece character"
					pass	
			elif line[0] == "y":
				# PlayerY piece coordinate
				if line[2].upper() != "K":
					# Print "Unrecognized piece chacter"
					pass
				else:
					# PlayerY - King Piece
					if validCoord(line):
						yK = (line[4], line[6]) #	Creates tuple for PlayerY's King
						Coordinates.append(yK)
			else:
				# Print "Coordinate format unrecognized"
				pass


	# For Debugging purposes
	if Debug:
		if f.closed:
			print('File closed successfully')
		else:
			print('File was not closed successfully')
		print(Coordinates)
		
	return Coordinates


FileRead(workfile)	
# Tuple:		("x", "r", 1, 3)


