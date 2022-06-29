from tkinter import *
from tkinter import ttk
from os.path import exists #No bitches?

def delete():
    txFilas.delete('1.0', END)
    txColumnas.delete('1.0', END)
    txDeterminante.delete('1.0', END)
    tx0x0.delete('1.0', END)
    tx0x1.delete('1.0', END)
    tx0x2.delete('1.0', END)
    tx0x3.delete('1.0', END)
    tx1x0.delete('1.0', END)
    tx1x1.delete('1.0', END)
    tx1x2.delete('1.0', END)
    tx1x3.delete('1.0', END)
    tx2x0.delete('1.0', END)
    tx2x1.delete('1.0', END)
    tx2x2.delete('1.0', END)
    tx2x3.delete('1.0', END)
    tx3x0.delete('1.0', END)
    tx3x1.delete('1.0', END)
    tx3x2.delete('1.0', END)
    tx3x3.delete('1.0', END)

def readFile():
    txFilas.delete('1.0', END)
    txColumnas.delete('1.0', END)
    txDeterminante.delete('1.0', END)
    tx0x0.delete('1.0', END)
    tx0x1.delete('1.0', END)
    tx0x2.delete('1.0', END)
    tx0x3.delete('1.0', END)
    tx1x0.delete('1.0', END)
    tx1x1.delete('1.0', END)
    tx1x2.delete('1.0', END)
    tx1x3.delete('1.0', END)
    tx2x0.delete('1.0', END)
    tx2x1.delete('1.0', END)
    tx2x2.delete('1.0', END)
    tx2x3.delete('1.0', END)
    tx3x0.delete('1.0', END)
    tx3x1.delete('1.0', END)
    tx3x2.delete('1.0', END)
    tx3x3.delete('1.0', END)
    #Value's deletion.
    if((exists(txArchivo.get())) == False):
        txDeterminante.insert('1.0', 'Error: ANE.')
        return
    fname = open(txArchivo.get(), 'r')
    txFilas.insert('1.0', fname.readline().rstrip())
    txColumnas.insert('1.0', fname.readline().rstrip())
    #--------------------------------------------------
    global filas
    global columnas
    filas = int(txFilas.get('1.0'))
    columnas = int(txColumnas.get('1.0'))
    if((filas < 2) | (columnas < 2) | (filas > 4) | (columnas > 4)):
        txDeterminante.insert('1.0', 'Error: DI.')
        return
    if(filas != columnas):
        txDeterminante.insert('1.0', 'Error: MNC.')
    if((filas >= 2) & (columnas >= 2)):
        line0 = fname.readline().rstrip().rsplit('\t')
        line1 = fname.readline().rstrip().rsplit('\t')
        tx0x0.insert('1.0', line0[0])
        tx0x1.insert('1.0', line0[1])
        tx1x0.insert('1.0', line1[0])
        tx1x1.insert('1.0', line1[1])

    if((filas >= 3) & (columnas >= 3)):
        line2 = fname.readline().rstrip().rsplit('\t')
        tx0x2.insert('1.0', line0[2])
        tx1x2.insert('1.0', line1[2])
        #New
        tx2x0.insert('1.0',line2[0])
        tx2x1.insert('1.0',line2[1])
        tx2x2.insert('1.0', line2[2])
        
    if((filas == 4) & (columnas == 4)):
        line3 = fname.readline().rstrip().rsplit('\t')
        tx0x3.insert('1.0', line0[3])
        tx1x3.insert('1.0', line1[3])
        tx2x3.insert('1.0', line2[3])
        #New
        tx3x0.insert('1.0', line3[0])
        tx3x1.insert('1.0', line3[1])
        tx3x2.insert('1.0', line3[2])
        tx3x3.insert('1.0', line3[3])
    #--------------------------------------------------

def callDet():
    if((filas == 2) & (columnas == 2)):
        txDeterminante.delete('1.0', END)
        det2x2()
    if((filas == 3) & (columnas == 3)):
        txDeterminante.delete('1.0', END)
        det3x3()
    if((filas == 4) & (columnas == 4)):
        txDeterminante.delete('1.0', END)
        det4x4()

def det2x2():
    global d2
    d2 = (float(tx0x0.get('1.0')) * float(tx1x1.get('1.0'))) - (float(tx1x0.get('1.0')) * float(tx0x1.get('1.0')))
    if(filas == 2):
        txDeterminante.insert('1.0', d2)

def det3x3():
    global d3
    d3 = ((float(tx0x0.get('1.0')) * float(tx1x1.get('1.0')) * float(tx2x2.get('1.0')))+(float(tx0x1.get('1.0')) * float(tx1x2.get('1.0')) * float(tx2x0.get('1.0')))+(float(tx0x2.get('1.0')) * float(tx2x1.get('1.0')) * float(tx1x0.get('1.0')))) - ((float(tx0x0.get('1.0')) * float(tx1x2.get('1.0')) * float(tx2x1.get('1.0'))) + (float(tx0x1.get('1.0')) * float(tx2x2.get('1.0')) * float(tx1x0.get('1.0'))) + (float(tx0x2.get('1.0')) * float(tx1x1.get('1.0')) * float(tx2x1.get('1.0'))))
    if(filas == 3):
        txDeterminante.insert('1.0', d3)

def det4x4():
    global d4
    d4 = ((float(tx0x0.get('1.0')) * float(tx1x1.get('1.0')) * float(tx2x2.get('1.0')) * float(tx3x3.get('1.0'))) + (float(tx0x2.get('1.0')) * float(tx1x3.get('1.0')) * float(tx2x0.get('1.0')) * float(tx3x1.get('1.0'))) + (float(tx3x0.get('1.0')) * float(tx2x1.get('1.0')) * float(tx1x2.get('1.0')) * float(tx0x3.get('1.0'))) + (float(tx3x2.get('1.0')) * float(tx2x3.get('1.0')) * float(tx1x0.get('1.0')) * float(tx0x1.get('1.0')))) - ((float(tx0x1.get('1.0')) * float(tx1x2.get('1.0')) * float(tx2x3.get('1.0')) * float(tx3x0.get('1.0'))) + (float(tx0x3.get('1.0')) * float(tx1x0.get('1.0')) * float(tx2x1.get('1.0')) * float(tx3x2.get('1.0'))) + (float(tx3x1.get('1.0')) * float(tx2x2.get('1.0')) * float(tx1x3.get('1.0')) * float(tx0x0.get('1.0'))) + (float(tx3x3.get('1.0')) * float(tx2x0.get('1.0')) * float(tx1x1.get('1.0')) * float(tx0x2.get('1.0'))))
    if(filas == 4):
        txDeterminante.insert('1.0', d4)
    
#------------------------------------------------------------------------
def createWindow():
    global root, txArchivo, txFilas, txColumnas, txDeterminante, txLeyenda
    global tx0x0, tx0x1, tx0x2, tx0x3
    global tx1x0, tx1x1, tx1x2, tx1x3
    global tx2x0, tx2x1, tx2x2, tx2x3
    global tx3x0, tx3x1, tx3x2, tx3x3

    root = Tk()
    root.geometry('600x400+300+300')
    #root.configure(bg = '')
    root.title("Cálculo de Determinantes")
    root.iconbitmap('icon.ico')

    #--------------------------------------------------------
    btnReadFile = Button(root, text = 'Leer Archivo', command = readFile)
    btnReadFile.place(x = 500, y = 5)
    btnCalcDet = Button(root, text = 'Calcular Determinante', command = callDet)
    btnCalcDet.place(x = 20, y = 350)
    btnDelete = Button(root, text = 'Borrar', command = delete)
    btnDelete.place(x = 175, y = 350)
    #--------------------------------------------------------
    lArchivo = Label(root, text = 'Archivo:')
    lArchivo.place(x = 20, y = 10)
    lMatriz = Label(root, text = 'Matriz')
    lMatriz.place(x = 20, y = 40)
    lFilas = Label(root, text = 'Filas')
    lFilas.place(x = 425, y = 50)
    lColumnas = Label(root, text = 'Columnas')
    lColumnas.place(x = 505, y = 50)
    lDeterminante = Label(root, text = 'Determinante:')
    lDeterminante.place(x = 375, y = 300)
    txLeyenda = Label(root, text = 'Leyenda:\n-DI: Dimensiones Incompatibles.\n-MNC: Matriz No Cuadrada.\n-ANE: Archivo No Existente.', justify = LEFT)
    txLeyenda.place(x = 20, y =200)
    #--------------------------------------------------------
    txArchivo = Entry(root, width = 64)
    txArchivo.place(x = 75, y = 10)
    txFilas = Text(root, width = 3, height = 1)
    txFilas.place(x = 425, y = 75)
    txColumnas = Text(root, width = 6, height = 1)
    txColumnas.place(x = 508, y = 75)
    txDeterminante = Text(root, width = 12, height = 1)
    txDeterminante.place(x = 460, y = 300)

    tx0x0 = Text(root, width = 5, height = 1) #Fila 1
    tx0x0.place(x = 22, y = 75)
    tx0x1 = Text(root, width = 5, height = 1)
    tx0x1.place(x = 82, y = 75)
    tx0x2 = Text(root, width = 5, height = 1)
    tx0x2.place(x = 142, y = 75)
    tx0x3 = Text(root, width = 5, height = 1)
    tx0x3.place(x = 202, y = 75)

    tx1x0 = Text(root, width = 5, height = 1) #Fila 2
    tx1x0.place(x = 22, y = 105)
    tx1x1 = Text(root, width = 5, height = 1)
    tx1x1.place(x = 82, y = 105)
    tx1x2 = Text(root, width = 5, height = 1)
    tx1x2.place(x = 142, y = 105)
    tx1x3 = Text(root, width = 5, height = 1)
    tx1x3.place(x = 202, y = 105)

    tx2x0 = Text(root, width = 5, height = 1) #Fila 3
    tx2x0.place(x = 22, y = 135)
    tx2x1 = Text(root, width = 5, height = 1)
    tx2x1.place(x = 82, y = 135)
    tx2x2 = Text(root, width = 5, height = 1)
    tx2x2.place(x = 142, y = 135)
    tx2x3 = Text(root, width = 5, height = 1)
    tx2x3.place(x = 202, y = 135)

    tx3x0 = Text(root, width = 5, height = 1) #Fila 3
    tx3x0.place(x = 22, y = 165)
    tx3x1 = Text(root, width = 5, height = 1)
    tx3x1.place(x = 82, y = 165)
    tx3x2 = Text(root, width = 5, height = 1)
    tx3x2.place(x = 142, y = 165)
    tx3x3 = Text(root, width = 5, height = 1)
    tx3x3.place(x = 202, y = 165)

    txArchivo.focus()
#-----------------------------------------------------------------------
createWindow()
root.mainloop()