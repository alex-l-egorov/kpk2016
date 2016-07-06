import turtle


#x=input()
#x='1234567890'

"""
Словарь, описывающий последовательность точек для рисования
каждой цифры
        0--1
        |  |
        2--3
        |  |
        4--5
"""
path={
    '0':(5,4,0,1),
    '1':(5,1,2,1),
    '2':(0,1,3,4,5),
    '3':(0,1,2,3,4),
    '4':(5,3,2,0),
    '5':(0,2,3,5,4),
    '6':(2,3,5,4,2),
    '7':(0,1,2,4),
    '8':(0,2,3,5,4,2,3,1),
    '9':(0,2,3,1,3,4)
}


def write(t,d,size=40):
    """
    Рисует черепашкой t цифру d размером size в текущей 
    позиции Черепашки.
    После рисования перо поднято.
    """
    def gen_matr():
        """
        Генерирует координаты 6 точек, необходимых для рисования цифры
        """
        m=[(0,0)]*6
        x,y=map(int,t.position())
        m[0]=(x-size,y)
        m[1]=(x,y)
        m[2]=(x-size,y-size)
        m[3]=(x,y-size)
        m[4]=(x-size,y-2*size)
        m[5]=(x,y-2*size)
        return m
    
    
    
    m=gen_matr()
    t.pd()
    for k in path[d]:
        t.goto(m[k])
    t.pu()
    t.goto(m[1])    
    
    



t=turtle.Turtle()
t.pu()
t.bk(300)
t.pd()
s=30
x=turtle.textinput('Draw Digit','Enter number:')

if not x.isdigit():
    raise (ValueError("Bad Input"))
for c in x:
    write(t,c,s)
    t.fd(1.2*s)
    
turtle.done()    


    


