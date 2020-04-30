import send2trash

bacon_file = open('bacon.txt', 'a')
bacon_file.write('Bacon is not a vegitable.')

bacon_file.close()
send2trash.send2trash('bacon.txt')
