# list containing dictionaries
favourite_albums = [
    {
        "artist": "Smashing Pumpkins",
        "album": "Siamese Dream",
        "year": "1993"
    },
    {
        "artist": "The Raconteurs",
        "album": "Broken Boy Soldiers",
        "year": "2006"
    },
    {
        "artist": "The Black Keys",
        "album": "El Camino",
        "year": "2011"
    }
]

# function that uses dictionary
def find_album_year(album_name):
    for album in favourite_albums:
        if album["album"] == album_name:
            return album["year"]

# call function
print(find_album_year("El Camino"))