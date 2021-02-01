from tkinter import*
from tkinter import ttk
import random
from src.quicksort import quick_sort
from src.insertionsort import insertion_sort
from src.bubbleSort import bubble_sort
from src.selectionsort import selection_sort
from src.mergesort import merge_sort

def main():
    root = Tk()
    root.title('Sorting Algorithm Visualisation')
    root.maxsize(1800,1200)
    root.config(bg='black')

    #variables
    selected_alg = StringVar()
    data = []

    def drawData(data,colorArray):
        canvas.delete("all")
        c_height = 650
        c_width = 1200
        x_width = c_width / (len(data) + 1)
        offset = 30
        spacing = 5
        normalizedData = [i / max(data) for i in data]

        for i,height in enumerate(normalizedData):
            #top left
            x0 = i * x_width + offset + spacing
            y0 = c_height - height * 600
            #bottom right
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            canvas.create_rectangle(x0,y0,x1,y1, fill=colorArray[i])
            canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
        root.update_idletasks()

    def Generate():
        global data
        minVal = int(minEntry.get())
        maxVal = int(maxEntry.get())
        size = int(sizeEntry.get())

        data = []

        for _ in range(size):
            data.append(random.randrange(minVal,maxVal+1))
        drawData(data,['red' for x in range(len(data))]) #

    def StartAlgorithm():
        global data
        if not data: return


        if algMenu.get() == 'Bubble Sort':
            bubble_sort(data,drawData,speedScale.get())

        elif algMenu.get() == 'Selection Sort':
            selection_sort(data,drawData,speedScale.get())

        elif algMenu.get() == 'Insertion Sort':
            insertion_sort(data,drawData,speedScale.get())

        elif algMenu.get() == 'Quick Sort':
            quick_sort(data,0,len(data)-1,drawData,speedScale.get())

        elif algMenu.get() == 'Merge Sort':
            merge_sort(data, drawData, speedScale.get())

        drawData(data,['green' for x in range(len(data))])

    #frame / base layout
    UI_frame = Frame(root, width=1200, height=400, bg='grey')
    UI_frame.grid(row=0, column=0, padx=10, pady=5)

    canvas = Canvas(root, width=1200, height=650, bg='white')
    canvas.grid(row = 1, column = 0, padx=0,pady=0)

    #User interface area
    #Row[0]
    Label(UI_frame, text='Algorithm : ', bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
    algMenu = ttk.Combobox(UI_frame,textvariable=selected_alg, values=['Quick Sort','Bubble Sort','Merge Sort','Selection Sort','Insertion Sort'])
    algMenu.grid(row=0, column=1, padx=0, pady=5)
    algMenu.current(0)

    speedScale = Scale(UI_frame, from_= 0.01, to=10.0, length=200,digits=4, resolution=0.2,orient=HORIZONTAL, label="Select speed [s]")
    speedScale.grid(row=0, column=2, padx = 5, pady = 5)
    Button(UI_frame, text='Start', command=StartAlgorithm, bg='red').grid(row=0, column=3,padx=5, pady=5)

    #Row[1]
    sizeEntry = Scale(UI_frame, from_= 3, to=100, resolution=1,orient=HORIZONTAL, label="Data Size")
    sizeEntry.grid(row = 1, column=0, padx=5, pady=5)

    minEntry = Scale(UI_frame, from_= 0, to=20, resolution=1,orient=HORIZONTAL, label="Min Value")
    minEntry.grid(row = 1, column=1, padx=5, pady=5)

    maxEntry = Scale(UI_frame, from_= 3, to=100, resolution=1,orient=HORIZONTAL, label="Max Value")
    maxEntry.grid(row = 1, column=2, padx=5, pady=5)

    Button(UI_frame, text='Generate', command=Generate, bg='yellow').grid(row=1, column=3,padx=5, pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()