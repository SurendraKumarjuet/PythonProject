from Tkinter import *
from tkMessageBox import *
        
counter=0
num=0
x=0
cntr=0

def res():
    root=Tk()
    root.attributes('-fullscreen',True)
    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(root, text='\n\n\n\n\nYour score is',fg='black',font='Times 22').pack(side=TOP,anchor=CENTER)
    Label(root, text='\n'+str(num),fg='black',font='Times 24 bold').pack(side=TOP,anchor=CENTER)
    def counter(label):
        def count():
            global cntr
            cntr= cntr+1
            label.after(1000,count)

            if cntr==2:
                root.destroy()
            
        count()
    label=Label(root,fg='black',font='Arial 18 bold')
    label.pack(side=TOP,anchor=CENTER)
    counter(label)

def ques10():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==2):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
        
    def counter(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    x=x/60
            global t
            t=str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==10:
                root.destroy()
                res()
        count()
    label=Label(root,fg='light green',font='Arial 18 bold')
    label.pack(side=TOP,anchor=CENTER)
    counter(label)
    
    
    Label(root, text = '\n\nQ10. Which of the following results in a SyntaxError(Multiple answers possible) ?',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' "Once upon a time...",she said.',padx=20,variable=v,value=1,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' "He said,"Yes!""',padx=20,variable=v,value=2,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' "3\"',padx=20,variable=v,value=3,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' '"That's okey"'',padx=20,variable=v,value=4,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    
        
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            res()
    def r():
        
        root.destroy()
        res()
    s = Frame(root, height=30, bg='black')
    Button(s, text = 'EXIT',width=16,height=2,bg='black',fg='red',font='Times 10 bold', command = Quit,relief=GROOVE,cursor="hand2").pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'RESULT',width=16,height=2,bg='black',fg='light green',font='Times 10 bold', command = r,relief=GROOVE,cursor="hand2").pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)


def ques9():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==4):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
        root.destroy()
        ques10()
    
    def counter(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    x=x/60
            global t
            t=str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==10:
                root.destroy()
                res()
        count()
    label=Label(root,fg='light green',font='Arial 18 bold')
    label.pack(side=TOP,anchor=CENTER)
    counter(label)
    
    Label(root, text = '\n\nQ9. Given a function that does not return any value, What value is thrown by itby default when executed in shell.',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER) 
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' int',padx=20,variable=v,value=1,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' bool',padx=20,variable=v,value=2,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' void',padx=20,variable=v,value=3,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' None ',padx=20,variable=v,value=4,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)

    def Quit(event=None):
       
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            res()
    s = Frame(root, height=30, bg='black')
    Button(s, text = 'EXIT',width=16,height=2,bg='black',fg='red',font='Times 10 bold', command = Quit,relief=GROOVE,cursor="hand2").pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=2,bg='black',fg='light green',font='Times 10 bold', command = q2,relief=GROOVE,cursor="hand2").pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)


def ques8():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==2):
            global num
            num=num+2
        
        else:
            num
    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
        root.destroy()
        ques9()
    def counter(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    x=x/60
            global t
            t=str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==10 :
                root.destroy()
                res()
        count()
    label=Label(root,fg='light green',font='Arial 18 bold')
    label.pack(side=TOP,anchor=CENTER)
    counter(label)
    

    Label(root, text = '\n\nQ8. What is the average value of the code that is executed below ?',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER)
    Label(root, text = '       1. >>>grade1 = 80',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER)
    Label(root, text = '       2. >>>grade2 = 90',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER)
    Label(root, text = '       3. >>>average = (grade1 + grade2) / 2',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 85',padx=20,variable=v,value=1,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 85.0',padx=20,variable=v,value=2,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 95',padx=20,variable=v,value=3,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 95.0',padx=20,variable=v,value=4,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    
       
    def Quit(event=None):
       
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            res()
    s = Frame(root, height=30, bg='black')
    Button(s, text = 'EXIT',width=16,height=2,bg='black',fg='red',font='Times 10 bold', command = Quit,relief=GROOVE,cursor="hand2").pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=2,bg='black',fg='light green',font='Times 10 bold', command = q2,relief=GROOVE,cursor="hand2").pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)



def ques7():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==2):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
       
        root.destroy()
        ques8()

    def counter(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    x=x/60
            global t
            t=str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==10:
                root.destroy()
                res()
        count()
    label=Label(root,fg='light green',font='Arial 18 bold')
    label.pack(side=TOP,anchor=CENTER)
    counter(label)
    
    Label(root, text = '\n\nQ7. What is the output of print 0.1 + 0.2 == 0.3?',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' True',padx=20,variable=v,value=1,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' False',padx=20,variable=v,value=2,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Machine dependent',padx=20,variable=v,value=3,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Error',padx=20,variable=v,value=4,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    
        
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            res()
    s = Frame(root, height=30, bg='black')
    Button(s, text = 'EXIT',width=16,height=2,bg='black',fg='red',font='Times 10 bold', command = Quit,relief=GROOVE,cursor="hand2").pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=2,bg='black',fg='light green',font='Times 10 bold', command = q2,relief=GROOVE,cursor="hand2").pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)



def ques6():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==3):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
        
        root.destroy()
        ques7()
    def counter(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    x=x/60
            global t
            t=str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==10 :
                root.destroy()
                res()
        count()
    label=Label(root,fg='light green',font='Arial 18 bold')
    label.pack(side=TOP,anchor=CENTER)
    counter(label)
    

    Label(root, text = '\n\nQ6. Which of the following is not a complex number?  ',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' k = 2 + 3j',padx=20,variable=v,value=1,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' k = complex(2, 3)',padx=20,variable=v,value=2,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' k = 2 + 3l',padx=20,variable=v,value=3,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text='  k = 2 + 3J',padx=20,variable=v,value=4,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    
       
    def Quit(event=None):
     
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            res()
    s = Frame(root, height=30, bg='black')
    Button(s, text = 'EXIT',width=16,height=2,bg='black',fg='red',font='Times 10 bold', command = Quit,relief=GROOVE,cursor="hand2").pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=2,bg='black',fg='light green',font='Times 10 bold', command = q2,relief=GROOVE,cursor="hand2").pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)



def ques5():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==3):
            global num
            num=num+2
           
        else:
            num
    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
        
        root.destroy()
        ques6()

    def counter(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    x=x/60
            global t
            t=str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==10:
                root.destroy()
                res()
        count()
    label=Label(root,fg='light green',font='Arial 18 bold')
    label.pack(side=TOP,anchor=CENTER)
    counter(label)
    
    Label(root, text = '\n\nQ5. What is the type of inf?',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Boolean',padx=20,variable=v,value=1,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text='  Integer',padx=20,variable=v,value=2,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Float',padx=20,variable=v,value=3,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Complex',padx=20,variable=v,value=4,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    
        
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            res()
    s = Frame(root, height=30, bg='black')
    Button(s, text = 'EXIT',width=16,height=2,bg='black',fg='red',font='Times 10 bold', command = Quit,relief=GROOVE,cursor="hand2").pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=2,bg='black',fg='light green',font='Times 10 bold', command = q2,relief=GROOVE,cursor="hand2").pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)



def ques4():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==1):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
        
        root.destroy()
        ques5()
    def counter(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    x=x/60
            global t
            t=str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==10:
                root.destroy()
                res()
        count()
    label=Label(root,fg='light green',font='Arial 18 bold')
    label.pack(side=TOP,anchor=CENTER)
    counter(label)
    
    Label(root, text = '\n\nQ4. What does ~4 evaluate to? ',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' -5',padx=20,variable=v,value=1,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' -4',padx=20,variable=v,value=2,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' -3',padx=20,variable=v,value=3,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' +3',padx=20,variable=v,value=4,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    
       
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            res()
    s = Frame(root, height=30, bg='black')
    Button(s, text = 'EXIT',width=16,height=2,bg='black',fg='red',font='Times 10 bold', command = Quit,relief=GROOVE,cursor="hand2").pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=2,bg='black',fg='light green',font='Times 10 bold', command = q2,relief=GROOVE,cursor="hand2").pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)


def ques3():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==1):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
       
        root.destroy()
        ques4()

    def counter(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    x=x/60
            global t
            t=str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==10:
                root.destroy()
                res()
        count()
    label=Label(root,fg='light green',font='Arial 18 bold')
    label.pack(side=TOP,anchor=CENTER)
    counter(label)
    
    Label(root, text = '\n\nQ3. What does ~~~~~~5 evaluate to? ',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text='  +5',padx=20,variable=v,value=1,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' -11',padx=20,variable=v,value=2,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' +11',padx=20,variable=v,value=3,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' -5',padx=20,variable=v,value=4,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    
        
    def Quit(event=None):
       
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            res()
    s = Frame(root, height=30, bg='black')
    Button(s, text = 'EXIT',width=16,height=2,bg='black',fg='red',font='Times 10 bold', command = Quit,relief=GROOVE,cursor="hand2").pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=2,bg='black',fg='light green',font='Times 10 bold', command = q2,relief=GROOVE,cursor="hand2").pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)
    

def ques2():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==4):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q1():
        
        root.destroy()
        ques3()

    def counter(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    x=x/60
            global t
            t=str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==10:
                root.destroy()
                res()
        count()
    label=Label(root,fg='light green',font='Arial 18 bold')
    label.pack(side=TOP,anchor=CENTER)
    counter(label)
    
    
    Label(root, text = '\n\nQ2. Which of the following is incorrect?',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' x = 0b101',padx=20,variable=v,value=1,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' x = 0x4f5',padx=20,variable=v,value=2,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' x = 19023',padx=20,variable=v,value=3,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' x = 03964',padx=20,variable=v,value=4,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    
        
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            res()
    s = Frame(root, height=30, bg='black')
    Button(s, text = 'EXIT',width=16,height=2,bg='black',fg='red',font='Times 10 bold', command = Quit,relief=GROOVE,cursor="hand2").pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=2,bg='black',fg='light green',font='Times 10 bold', command = q1,relief=GROOVE,cursor="hand2").pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)



def ques1():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==1):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    
    def counter(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    x=x/60
            global t
            t=str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==10:
                root.destroy()
                res()
        count()
    label=Label(root,fg='light green',font='Arial 18 bold')
    label.pack(side=TOP,anchor=CENTER)
    counter(label)
    def q1():
        
        root.destroy()
        ques2()
   
    Label(root, text = '\n\nQ1. What is the result of cmp(3, 1)?',fg='black',font='Times 19').pack(side=TOP,anchor=CENTER)
    Radiobutton(root,text=' 1',padx=20,variable=v,value=1,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 0',padx=20,variable=v,value=2,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' True',padx=20,variable=v,value=3,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' False ',padx=20,variable=v,value=4,font='Times 16',command=m,relief=GROOVE,cursor="hand2").pack(side=TOP,anchor=CENTER)

        
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            res()

    s = Frame(root, height=24, bg='black')
    Button(s, text = 'EXIT',width=16,height=2,bg='black',fg='red',font='Times 10 bold', command = Quit,relief=GROOVE,cursor="hand2").pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=2,bg='black',fg='light green',font='Times 10 bold', command = q1,relief=GROOVE,cursor="hand2").pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)
    
    
def page3():
    root=Tk()
    root.attributes('-fullscreen',True)

    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(root, text=' Please read the instructions carefully',fg='black',font='Times 25 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='>>> This test contains 10 questions.',fg='black',font='Times 18 ').pack(side=TOP,anchor=CENTER)
    Label(root, text='>>> The test is of 20 marks.',fg='black',font='Times 18 ').pack(side=TOP,anchor=CENTER)
    Label(root, text='>>> All questions are multiple choice and are compulsory.',fg='black',font='Times 18 ').pack(side=TOP,anchor=CENTER)
    Label(root, text='>>> You can only attempt in sequential order.',fg='black',font='Times 18 ').pack(side=TOP,anchor=CENTER)
    Label(root, text='>>> Test is time bound. You have 5 mins for completing the test. ',fg='black',font='Times 18 ').pack(side=TOP,anchor=CENTER)
    Label(root, text='>>> The marks alloted per question will be 2.',fg='black',font='Times 18 ').pack(side=TOP,anchor=CENTER)
    Label(root, text='>>> Once you opt for a question you can go to another question without completing.',fg='black',font='Times 18 ').pack(side=TOP,anchor=CENTER)
    Label(root, text='>>> Your score will be displayed once you complete all the questions or when you quit the test.  ',fg='black',font='Times 18 ').pack(side=TOP,anchor=CENTER)
    Label(root,text='Click START to Continue' ,fg='red',font='Times 13').pack(side=TOP,pady=70)
    def next3():
        root.destroy()
        ques1()
    def Quit(event=None):
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()

    s = Frame(root, height=30, bg='black')
    Button(s, text = 'EXIT',width=16,height=2,bg='black',fg='red',font='Times 10 bold', command = Quit,relief=GROOVE,cursor="hand2").pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'START',width=16,height=2,bg='black',fg='light green',font='Times 10 bold', command = next3,relief=GROOVE,cursor="hand2" ).pack(side=RIGHT,expand=NO,anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)


def page2():
    root=Tk()
    root.attributes('-fullscreen',True)
    def Quit1(event=None):
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            page1()
    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=3,width=10,font='Times 15')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text=" Welcome to Quiz.  Fill the form to continue.",bg='black',fg='light green',width=80,height=1,font='Times 25')
    toolbar1.pack(side=TOP,anchor=CENTER)
    shortcutbar1.pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    shortcutbar2 = Frame(root)
    e1 = Entry(shortcutbar2)
    toolbar2 = Label(shortcutbar2, text="Enrollment No: ",width=45,height=1,font='Times 15', relief='groove').pack(side=TOP,anchor=CENTER)
    e1.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar2.pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    shortcutbar3 = Frame(root)
    e2 = Entry(shortcutbar3)
    toolbar2 = Label(shortcutbar3, text="Full Name: ",width=45,height=1,font='Times 15', relief='groove').pack(side=TOP,anchor=CENTER)
    e2.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar3.pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    shortcutbar4 = Frame(root)
    e4 = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="Branch: ",width=45,height=1,font='Times 15', relief='groove').pack(side=TOP,anchor=CENTER)
    e4.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(side=TOP,anchor=CENTER)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    
    shortcutbar4 = Frame(root)
    e5 = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="Batch: ",width=45,height=1,font='Times 15', relief='groove').pack(side=TOP,anchor=CENTER)
    e5.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(side=TOP,anchor=CENTER)
    def next2():

            root.destroy()
            page3()

    def Quit(event=None):
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
    def info():
            if(str(e1.get())=='' or str(e2.get())=='' or str(e4.get())=='' or str(e5.get())==''):
                s=showerror(title="Error",message='Fill the entries.')
            else:
                Label(root,text='Click NOTICE to Continue' ,fg='red',font='AdobeHeitiStdR 14').pack(side=TOP,pady=100)
                s = Frame(root, height=30, bg='black')
                Button(s, text = 'NOTICE',width=16,height=1,bg='black',fg='white',font='Times 10 bold',relief=GROOVE, command = next2,cursor="hand2" ).pack(side=RIGHT,expand=NO,anchor=SE )
                s.pack(side=BOTTOM,expand=NO, fill=X)
    def submit(event=None):
        if askokcancel("SUBMIT", "Are you sure you want to Submit?"):
            info()
            
            
    
           
    Button(root, text = 'SUBMIT',width=16,height=2,bg='black',fg='light green',font='Times 10 bold', command = submit,cursor="hand2" ).pack(side=TOP,expand=NO, anchor=CENTER)


    
def aboutus():
    root=Tk()
    root.attributes('-fullscreen',True)

    shortcutbar = Frame(root, height=30, bg='black')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=4,width=20,font='Times 35')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text='\n\n Project is designed by:',fg='black',font='Times 18').pack(side=TOP,anchor=CENTER)
    Label(root, text='Surendra Kumar (151426)',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='Branch - CSE(B7)',fg='black',font='Times 16 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='Email: rudrakshprasad1k97@gmail.com',fg='black',font='Times 16 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='\n Guided by:',fg='black',font='Times 18').pack(side=TOP,anchor=CENTER)
    Label(root, text='Dr. Mahesh Kumar',fg='black',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
    def sbmt():
        root.destroy()
        page2()
    s = Frame(root, height=30, bg='black')
    Button(s, text='EXIT',width=16,height=2,bg='black',fg='red',font='Times 12 bold',command=root.destroy,relief=GROOVE,cursor="hand2").pack(side=BOTTOM, anchor=CENTER)
    Button(s, text='SIGN UP',width=16,height=2,bg='black',fg='light green',font='Times 12 bold',command=sbmt,relief=GROOVE,cursor="hand2").pack(side=BOTTOM, anchor=CENTER)
    s.pack(side=BOTTOM,expand=NO, fill=X)



global page1
def page1():
    root =Tk()
    root.attributes('-fullscreen',True)
    shortcutbar1 = Frame(root, height=1000, bg='black')
  
    Label(shortcutbar1, text='\n\n\n\nWelcome to Quiz Test\n\n',bg='black',fg='white',font='Times 35').pack(side=TOP,anchor=CENTER)
    Label(shortcutbar1, text='SUDO\n\n\n\n',bg='black',fg='white',font='Times 25').pack(side=TOP,anchor=CENTER)
    
    def abt():
        root.destroy()
        aboutus()
    def sbmt():
        root.destroy()
        page2()
    def Quit(event=None):
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
    Button(shortcutbar1, text='SIGN UP',width=30,height=1,bg='black',fg='light green',font='Times 12 bold',command=sbmt,relief=GROOVE,cursor="hand2").pack()
    shortcutbar1.pack(expand=NO, fill=X)
    shortcutbar3 = Frame(root, height=60, bg='black')
    shortcutbar3.pack(expand=NO, fill=X)
    shortcutbar2 = Frame(root, height=768, bg='black')    


    Button(shortcutbar1, text='EXIT',width=30,height=1,bg='black',fg='red',font='Times 12 bold',command=Quit,relief=GROOVE,cursor="hand2").pack(side=BOTTOM, anchor=CENTER)
    Button(shortcutbar1, text='INFO',width=30,height=1,bg='black',fg='white',font='Times 12 bold',command=abt,relief=GROOVE,cursor="hand2").pack(side=BOTTOM, anchor=CENTER)

    shortcutbar2.pack(side=BOTTOM,expand=NO, fill=BOTH)
    root.mainloop()
page1()
