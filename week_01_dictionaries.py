favourite_albums = [
    {
        "artist": "Smashing Pumpkins",
        "album": "Siamese Dream",
        "year": "1993"
    },
    {
        "artist": "The Racontuers",
        "album": "Broken Boy Soldiers",
        "year": "2006"
    },
    {
        "artist": "The Black Keys",
        "album": "El Camino",
        "year": "2011"
    }
]

def find_album_year(album_name):
    for album in favourite_albums:
        if album["album"] == album_name:
            return album["year"]

print(find_album_year("El Camino"))
