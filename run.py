import login
import main

class MeetZone:
    def __init__(self):
        f = open('isLog.txt',"r")
        to_read = f.read(1024).split(',')
        if to_read[0] == 'logged in':
            main.main_loop(to_read[1])
        else:
            login.login()

if __name__=='__main__':
    my_app = MeetZone()
