import tkinter as tk
#import sys
#import os


#if os.environ.get('DISPLAY','') == '':
 #   print('no display found. Using :0.0')
  #  os.environ.__setitem__('DISPLAY', ':0.0')

venster=tk.Tk()
tekst=tk.Label(venster, text="Demo")
tekst.pack()

venster.mainloop()
