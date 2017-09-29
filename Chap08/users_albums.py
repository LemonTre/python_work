def make_album(singer, song):
	album = {'singer_name': singer, 'song_name': song}
	return album
	
while True:
	print("\nPlease input a song and it's holder: ")
	print("(Enter 'q' to quit in any time!)")
	
	singer = input("Enter the singer: ")
	if singer == 'q':
		break
	
	song = input("Enter the song: ")
	if song == 'q':
		break

	album = make_album(singer, song)
	print(album)