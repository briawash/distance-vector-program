
"""
Brianca Washington
1001132562

"""

import time
import numpy
import tkinter as Tkinter
from tkinter import filedialog
import glob
####### sets up the node boxes#######
def listboxes_menu(p,l, Name,pos):
	label_widget = Tkinter.Label(p,text=Name)
	listbox_widget = Tkinter.Listbox(p)
	for entry in l:
		listbox_widget.insert(Tkinter.END, entry)
	label_widget.grid(row = 3, column = pos) 	
	listbox_widget.grid(row = 5, column = pos)
	return listbox_widget
def menu_callback():
	    print("I'm in the menu callback!")
##### to open the file
def submenu_callback(p):
	open_window=Tkinter.Tk()
	open_window.filename =filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt files","*.txt"),("all files","*.*")))
	fname=open_window.filename
	open_window.destroy()
	openfile(fname,p)
def buttons(p, name, clr,cmd,rw,col):
	button_widget = Tkinter.Button(p,fg=clr,
    	text=name, command=cmd )
	button_widget.grid(row = rw, column = col)
###### this is for opening a new file
def openfile(filename,p):
	try:
		data=open(filename,'r')
		a=[]
		b=[]
		a=data.read()
		for i in a:
			if(i.isdigit()== 1):
				b.append(int(i))
		
		

	except FileNotFoundError:
		print("Wrong file or file path")
		b=0

	startDV(b,p)
# this will change the cost and then call the start function
# reintialize the arrays
def changeCost(arr,a,b,cost,p):
	for i in range(0,len(arr)):
		if((i+1)%3==0):
			if(((arr[i-2]==a) and (arr[i-1]==b))or (arr[i-2]==b and arr[i-1]==a)):
				arr[i]=cost
				startDV(arr)
	arr.append(a)
	arr.append(b)
	arr.append(cost)
	startDV(arr,p)
### places array values into nodes#######
def place(arr, row):
	base = numpy.empty((7, 7))
	base.fill(999)
	base[0][1]=1
	base[1][0]=1
	base[2][0]=2
	base[0][2]=2
	base[0][3]=3
	base[3][0]=3
	base[0][4]=4
	base[4][0]=4
	base[5][0]=5
	base[0][5]=5
	base[0][6]=6
	base[6][0]=6
	for i in range(0,len(arr)):
		if((i+1)%3==0):
			if(arr[i-1]==row):
				base[row][arr[i-2]]=arr[i]
			elif(arr[i-2]==row):
				base[row][arr[i-1]]=arr[i]
	
	return base 
	##### intializes nodes and program######
def startDV(arr,p):
	a=textbox(p,"From Node", "green",6,1)
	b=textbox(p,"To Node", "green",6,3)
	cost=textbox(p,"Cost", "green",6,5)
	change_widget = Tkinter.Button(p,
	text="Change Cost", command=lambda:changeCost(arr,a.get(),b.get(),cost.get(),p))
	change_widget.grid(row = 6, column = 7)
	node1=place(arr,1)
	node2=place(arr,2)
	node3=place(arr,3)
	node4=place(arr,4)
	node5=place(arr,5)
	node6=place(arr,6)
	start=time.time()
	cntrller(1,node1,node2,node3,node4,node5,node6,p,start)

	####### main controller function######3
def cntrller(step,node1,node2,node3,node4,node5,node6,p,start):

	label_widget = Tkinter.Label(p,text="Step:"+str(step))
	label_widget.grid(row = 2, column = 8)
	listboxes_menu(p, node1, "Node 1",0)
	listboxes_menu(p, node2, "Node 2",1)
	listboxes_menu(p, node3, "Node 3",2)
	listboxes_menu(p, node4, "Node 4",3)
	listboxes_menu(p,node5, "Node 5",4)
	listboxes_menu(p,node6 , "Node 6",5)
	if(step ==1):
		start_widget = Tkinter.Button(p,
    	text="Start" ,command=lambda:OneStep(step,node1,node2,node3,node4,node5,node6,p,start))
		start_widget.grid(row = 7, column = 0)
	elif(step<=6):
		button_widget = Tkinter.Button(p,
    	text="Run One Step", command=lambda:OneStep(step,node1,node2,node3,node4,node5,node6,p,start))
		button_widget.grid(row = 7, column = 3)

		full_widget = Tkinter.Button(p,
    	text="Run to End", command=lambda:toEnd(step,node1,node2,node3,node4,node5,node6,p,start))
		full_widget.grid(row = 7, column = 5)
	else:
		stop=time.time()
		label_widget = Tkinter.Label(p,text="Step:6")
		l1_widget = Tkinter.Label(p,text="Time(ms):"+ str(stop-start))
		l1_widget.grid(row = 0, column = 3)
		l2_widget = Tkinter.Label(p,text="The system is in a stable state")
		l2_widget.grid(row = 0, column = 1)
########## for the to node##############
def toEnd(step,node1,node2,node3,node4,node5,node6,p,start):
	while(step!=6):
		node1=checkNode(1,node1,node2,node3,node4,node5,node6)
		node2=checkNode(2,node1,node2,node3,node4,node5,node6)
		node3=checkNode(3,node1,node2,node3,node4,node5,node6)
		node4=checkNode(4,node1,node2,node3,node4,node5,node6)
		node5=checkNode(5,node1,node2,node3,node4,node5,node6)
		node6=checkNode(6,node1,node2,node3,node4,node5,node6)
		node1=checkswap(node1,step)
		node2=checkswap(node2,step)
		node3=checkswap(node3,step)
		node4=checkswap(node4,step)
		node5=checkswap(node5,step)
		node6=checkswap(node6,step)
		step=step+1
	cntrller(7,node1,node2,node3,node4,node5,node6,p,start)
## computes one step for ALLLLL nodes ##########
def OneStep(step,node1,node2,node3,node4,node5,node6,p,start):

	node1=checkNode(1,node1,node2,node3,node4,node5,node6)
	node2=checkNode(2,node1,node2,node3,node4,node5,node6)
	node3=checkNode(3,node1,node2,node3,node4,node5,node6)
	node4=checkNode(4,node1,node2,node3,node4,node5,node6)
	node5=checkNode(5,node1,node2,node3,node4,node5,node6)
	node6=checkNode(6,node1,node2,node3,node4,node5,node6)
	node1=checkswap(node1,step)
	node2=checkswap(node2,step)
	node3=checkswap(node3,step)
	node4=checkswap(node4,step)
	node5=checkswap(node5,step)
	node6=checkswap(node6,step)
	## now check the values
	step=step+1
	cntrller(step,node1,node2,node3,node4,node5,node6,p,start)
	
#### check the recipocral values
def checkswap(arr, size):
	for j in range(0,size):
		for i in range(0,size):
			if(arr[i+1][j+1]>arr[j+1][i+1]):
				arr[i+1][j+1]=arr[j+1][i+1]
			elif(arr[i+1][j+1]<arr[j+1][i+1]):
				arr[j+1][i+1]=arr[i+1][j+1]
			elif(i+1==j+1):
				arr[j+1][i+1]=0

	return arr
###### will update the nodes to be nodes with last node#######
def checkNode(check,node1,node2,node3,node4,node5,node6):
	done=node1
	for j in range(0,6):
		for i in range(0,6):
			if(check==1):
				node1[j+1][i+1]=min(node1[j+1][i+1],node1[j+1][1]+node1[1][i+1],node1[j+1][2]+node2[2][i+1],node1[j+1][3]+node3[3][i+1],node1[j+1][4]+node4[4][i+1],node1[j+1][5]+node5[5][i+1],node1[j+1][6]+node6[6][i+1])
				done=node1
			if(check==2):
				node2[j+1][i+1]=min(node2[j+1][i+1],node2[j+1][1]+node1[1][i+1],node2[j+1][2]+node2[2][i+1],node2[j+1][3]+node3[3][i+1],node2[j+1][4]+node4[4][i+1],node2[j+1][5]+node5[5][i+1],node2[j+1][6]+node6[6][i+1])
				done=node2
			if(check==3):
				node3[j+1][i+1]=min(node3[j+1][i+1],node3[j+1][1]+node1[1][i+1],node3[j+1][2]+node2[2][i+1],node3[j+1][3]+node3[3][i+1],node3[j+1][4]+node4[4][i+1],node3[j+1][5]+node5[5][i+1],node3[j+1][6]+node6[6][i+1])
				done=node3
			if(check==4):
				node4[j+1][i+1]=min(node4[j+1][i+1],node4[j+1][1]+node1[1][i+1],node4[j+1][2]+node2[2][i+1],node4[j+1][3]+node3[3][i+1],node4[j+1][4]+node4[4][i+1],node4[j+1][5]+node5[5][i+1],node4[j+1][6]+node6[6][i+1])
				done=node4
			if(check==5):
				node5[j+1][i+1]=min(node5[j+1][i+1],node5[j+1][1]+node1[1][i+1],node5[j+1][2]+node2[2][i+1],node5[j+1][3]+node3[3][i+1],node5[j+1][4]+node4[4][i+1],node5[j+1][5]+node5[5][i+1],node5[j+1][6]+node6[6][i+1])
				done=node5
			if(check==6):
				node6[j+1][i+1]=min(node6[j+1][i+1],node6[j+1][1]+node6[1][i+1],node6[j+1][2]+node2[2][i+1],node6[j+1][3]+node3[3][i+1],node6[j+1][4]+node4[4][i+1],node6[j+1][5]+node5[5][i+1],node6[j+1][6]+node6[6][i+1])
				done=node6
	return done
############if for change cost function#########
def textbox(p,name,clr,rw,col): 
	label_widget = Tkinter.Label(p,text=name)
	entry_widget = Tkinter.Entry(p)
	entry_widget.insert(0,name)
	label_widget.grid(row = rw, column = col-1)
	entry_widget.grid(row = rw, column = col)
	return entry_widget	
## this function is for the menu open function#####3
def menu_boxes(p, name):
	menu_widget = Tkinter.Menu(p)
	submenu_widget = Tkinter.Menu(menu_widget, tearoff=False)
	submenu_widget.add_command(label="Open",
	                           command=lambda:submenu_callback(p))
	submenu_widget.add_command(label="Quit",
	                           command=p.destroy)
	menu_widget.add_cascade(label="File", menu=submenu_widget)
	p.config(menu=menu_widget)	
######## this function initializes the program UI#########
def controller():
	p= Tkinter.Tk()
	p.title("Distance Vector Program")
	listbox_entries = [""]
	node1=listboxes_menu(p, listbox_entries, "Node 1",0)
	node2=listboxes_menu(p, listbox_entries, "Node 2",1)
	node3=listboxes_menu(p, listbox_entries, "Node 3",2)
	node4=listboxes_menu(p, listbox_entries, "Node 4",3)
	node5=listboxes_menu(p, listbox_entries, "Node 5",4)
	node6=listboxes_menu(p, listbox_entries, "Node 6",5)
	menu_boxes(p,"File")
	Tkinter.mainloop()
	
	
    ###################  main  ###################
if __name__ == "__main__" :
	controller()