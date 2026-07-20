#time to Time wishing good time
time=int(input ("enter the time:"))

if time<0 or time>25:
    print ("invalid ")
elif time<=5:
    print ("good morning 🌄")
elif time<=12:
    print ("good afternoon 🌞")
elif time<=17:
    print (" good evening 🌆")
else :
    print (" good night 🌃")
