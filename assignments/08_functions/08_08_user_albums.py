def make_album(artist_name, album_title, tracks=None):
    album = {'artist': artist_name, 'title': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    print("\nEnter 'q' at any time to quit.")
    artist = input("Enter the artist's name: ")
    if artist.lower() == 'q':
        break
    title = input("Enter the album title: ")
    if title.lower() == 'q':
        break
    tracks_input = input("Enter the number of tracks (or leave blank): ")
    if tracks_input.lower() == 'q':
        break
    if tracks_input:
        tracks = int(tracks_input)
    else:
        tracks = None

    album_info = make_album(artist, title, tracks)
    print(f"\nAlbum info: {album_info}")