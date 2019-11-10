from datetime import datetime
Guide='''
        How to use my StopWatch
        start-To start the Timer
        stop-To stop the Timer
        quit-To quit.
        '''
print(Guide)
started=False
command=''
while True:
    command=input("> ").lower()
    if command=='start':
        if started:
            print("Timer is already started!")
        else:
            started=True
            start_time=datetime.now()
            print("Timer is Running...")
    elif command=='stop':
        if not started:
            print("Timer is already Stopped!")
        else:
            started=False
            end_time=datetime.now()
            print("Timer Stopped!")
            print('Duration: ',(end_time - start_time))
    elif command=='quit':
        break
    else:
        print("Sorry, didn't understand that.")
        print(Guide)