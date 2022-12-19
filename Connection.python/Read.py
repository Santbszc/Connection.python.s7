import time 

while True: 
    f = open('dashBoard.txt', 'r')
    print(f.read())
    f.close()
    time.sleep(1)