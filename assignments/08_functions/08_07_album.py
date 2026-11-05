def make_album(artist_name, album_title, tracks=None):
    album = {'artist': artist_name, 'title': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

print(make_album("Tyler the Creator", "IGOR", 12))
print(make_album("Christtt", "Social Justice Whatever"))
print(make_album("Insane Clown Posse", "The Great Milenko", 16))