import re

def song_decoder(song):
    decoded_song = re.sub('WUB', ' ', song)

    return ' '.join(decoded_song.split())

print(song_decoder("AWUBBWUBC"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
print(song_decoder("WUBAWUBBWUBCWUB"))
