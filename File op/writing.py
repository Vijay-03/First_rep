# eminem = ["lose yourself", "not afraid", "beautiful", "venom"]
#
# with open("eminem.txt", 'w') as song_file:
#     for song in eminem:
#         print(song, file=song_file)

eminem = []
with open("eminem.txt", 'r') as song_file:
    for song in song_file:
        eminem.append(song.strip('\n'))

print(eminem)
for song in eminem:
    print(song)