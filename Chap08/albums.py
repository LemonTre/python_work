def make_album(name, album_name, song_number = ''):
	album = {'singer_name': name, 'album_name': album_name}
	
	if song_number:
		album['song_number'] = song_number
	
	return album
	
album_1 = make_album('Liu Huan', 'Dahe')
print(album_1)

album_2 = make_album('Han Hong', 'Tianshang')
print(album_2)

album_3 = make_album('Lenka', 'Trouble is a friend', song_number = 1000)
print(album_3)
