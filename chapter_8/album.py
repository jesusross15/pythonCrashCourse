
def make_album(artist, title, songs=None):
    """Build a dictionary containing information about an album."""
    album = {'artist': artist.title(), 'title': title.title()}
    if songs:
        album['songs'] = songs
    return album

album_1 = make_album('kanye west', 'my beatiful dark twisted fantasy', songs=13)
print(album_1)

album_1 = make_album('frank ocean', 'blonde')
print(album_1)

album_1 = make_album('gunna', 'drip season 4')
print(album_1)
