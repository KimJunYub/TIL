from matplotlib import pyplot as plt
import matplotlib.ticker as mticker


testFile = open('stdout.txt','r',encoding='UTF8')
# print(readFile)

cnt = 0
time=[]
temp=[]
hum=[]
fig, axes = plt.subplots(4,1)
p = 0
grCnt = 0

while 1 :
    readFile = testFile.readline()

    if 'End' == readFile.strip() or 'Readerror' == readFile.strip() :
        break

    splstr = readFile.split(sep='|')
    time.append(splstr[0].strip('Time='))
    temp.append(float(splstr[1].strip('Temperature=').strip('C')))
    hum.append(float(splstr[2].strip('Humidity=').strip('\n').strip('\%')))

    grCnt+=1
    cnt+=1

    if grCnt == 360 :
        # print('split')
        # yticks_loc = axes[p].get_yticks().tolist()

        axes[p].set_title(time[0]+'~'+time[-1])
        axes[p].plot(time, temp, label='Temperature')
        axes[p].plot(time, hum, label='Humidity')
        axes[p].legend(loc='lower right')
        # axes[p].yaxis.set_major_locator(mticker.FixedLocator(yticks_loc))
        axes[p].set_xticklabels(axes[p].get_xticklabels(), rotation=85)
        # axes[p].axes([time[0],time[-1],20,50])

        p+=1
        grCnt = 0

        time.clear()
        temp.clear()
        hum.clear()

plt.tight_layout()
plt.show()