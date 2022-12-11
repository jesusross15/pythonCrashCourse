
def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album = {'artist': artist.title(), 'title': title.title()}
    if tracks:
        album['number of tracks'] = tracks
    return album

while True:
    print("\nWhat's your favorite album? (Please include the album artist and name!)")
    print("enter 'q' at any time to quit")

    artist_name = input("Artist Name: ")
    if artist_name == 'q':
        break

    album_name = input("Album Name: ")
    if album_name == 'q':
        break

    user_input = make_album(artist_name, album_name)
    print(f"\n{user_input}? what a great choice!")