from Tkinter import *
import random

#risuet kvadrat s cifroi v centre
def fishka(a,b,c,d,g):
        w.create_rectangle(a, b, c, d, fill="gray")
        w.create_text(c-xh/2,d-yw/2,text=g)

#sozdaem izobrazenie togo sto na ekrane dolzno otobrazat sostojanie pamjati a
def showbox():
        for i in range(0,4):
                for n in range(0,4):
                        if a[i][n]==0 :
                                pass
                        else :
                              fishka(i*xh,n*yw,i*xh+xh,n*yw+yw,a[i][n])

#pravilno peremewivaet fishki v korobke
def mix(x):
        r = random.Random()
        for x in range (0,x):
                tmp=r.randint(-1,1)
                tmz=r.randint(-1,1)
                for i in range(0,4):
                        for n in range(0,4):
                                if a[i][n]==0 :
                                        if tmz==-1 :
                                                if n+tmp<4 and n+tmp>=0:
                                                        a[i][n]=a[i][n+tmp]
                                                        a[i][n+tmp]=0
                                                
                                        if tmz==1 :
                                                if i+tmp<4 and i+tmp>=0:
                                                        a[i][n]=a[i+tmp][n]
                                                        a[i+tmp][n]=0


#funkcija katoroja nahodit gde u nas teper 0 ili pustaja kletka po koordinate x
def findzerox(a):
        for x in range (0,4):
                for y in range(0,4):
                        if a[x][y]==0:
                                return x

#funkcija katoroja nahodit gde u nas teper 0 ili pustaja kletka po koordinate y
def findzeroy(a):
        for x in range (0,4):
                for y in range(0,4):
                        if a[x][y]==0:
                                return y
        

#nazatie knopki miwi    
def b1(event):
     #opredeljaem koordinati kletki!
     x=event.x
     y=event.y
     xz=findzerox(a)
     yz=findzeroy(a)
     #peremewaem toka esli klik na rastojanii +-1 na toi ze osi x ili y
     if x//xh==xz+1 and yz==y//yw :
             a[xz][yz]=a[x//xh][y//yw]
             a[x//xh][y//yw]=0
     if x//xh==xz-1 and yz==y//yw :
             a[xz][yz]=a[x//xh][y//yw]
             a[x//xh][y//yw]=0
     if y//yw==yz+1 and xz==x//xh :
             a[xz][yz]=a[x//xh][y//yw]
             a[x//xh][y//yw]=0
     if y//yw==yz-1 and xz==x//xh :
             a[xz] [yz]=a[x//xh][y//yw]
             a[x//xh][y//yw]=0
     ##udaljaem i pererisivivaem ekran!
     w.delete(ALL)
     showbox()
     w.update()
     
##zadaem razmer kletki
xh=96
yw=96
#sozdaem nacalnoe sostojanie pamjati 1->15,0
a = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12],[13,14,15,0]]
root=Tk()
##root.geometry('385x385')
w=Canvas(root,width=385,height=385,bg="white")
##zapuskaet okno poverh drugih
root.call('wm', 'attributes', '.', '-topmost', '1')
#peremewivaem sostojanie pamjati ( dolzno izmentisja soderzimoe ekrana
mix(79)
#pokazivaem
showbox()
#obrabativaem kliki moiuse izmenjaem sostojanie  pamjati i avtomatom ekrana
root.bind('<Button-1>',b1)
w.pack()
mainloop()


