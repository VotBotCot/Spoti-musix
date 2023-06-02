from os import system

print("Install lib.")
system('sudo pip3 install spotdl')
system("pip install spotipy")
system('clear')

id = input("Client ID: ")
secret = input("Client Secret: ")

system('clear')
print('Configuration...')
with open('config', 'w') as f:
    f.write(id + "\n" + secret)
    
print("Finish!")
