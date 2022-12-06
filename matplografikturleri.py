from dis import show_code
import matplotlib.pyplot as plt 
"""
yil = [2011,2012,2013,2014,2015]

player1 = [8,12,18,20,25]
player2 = [7,11,17,24,28]
player3 = [9,13,15,22,29]

#Stack Plot

plt.plot([] , [] , color = "y" , label = "player1")
plt.plot([] , [] , color = "r" , label = "player1")
plt.plot([] , [] , color = "b" , label = "player1")

plt.stackplot(yil,player1 , player2 , player3 ,colors=["y","r","b"])
plt.title("Yıllara gore atilan goller")
plt.xlabel("Yil")
plt.ylabel("Gol sayisi")
plt.legend()

plt.show()"""
"""
goals_types = 'Penaltı' , 'Kaleye Atilan Sut' ,'Serbest Vurus'

goals = [12,35,7]
colors = ['y' , 'r' ,'b']

plt.pie(goals , labels=goals_types , colors=colors , shadow = True , explode = (0.05,0.05,0.05))
plt.show()"""
"""
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label = "BMW" , width= .5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label = "AUDİ ", width = .5)

plt.legend()
plt.xlabel("Gun")
plt.ylabel("Mesafe(km)")
plt.title("Arac")

plt.show()"""

yaslar = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115]
yas_grupları = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar , yas_grupları , histtype = "bar" ,rwidth=0.8 )
plt.xlabel("Yas Grupları")
plt.ylabel("Kisi Sayisi")
plt.title("Histogram Gra")

plt.show()