#I want to print song name and artist name dictionary
def artist_song():
    while True:
        song_name = input("Song Name Please:  ")
        quit=input("Want to quit?(yes/no) ")
        if quit =='yes':
           break
        artist_name = input("Artist Name Please: ")
        quit=input("Want to quit?(yes/no) ")
        if quit=='yes':
            break
        details = {'song':song_name,'artist': artist_name}
        x = details.values()
        complete_details = print(x)
          
    return complete_details
    
artist_song()

