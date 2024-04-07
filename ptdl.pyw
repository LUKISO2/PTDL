import tkinter as tk
import urllib.parse
import webbrowser
import requests
import re

helpDict = {}
rex = re.compile(r'\{.?file.?\:.?\"(?P<link>.*?)\".?,.*label.?\:.?\'(?P<res>.*?)\'')
colorBg = '#262626'
colorFg = '#FFFFFF'
colorBox = '#36454F'
colorButtons = '#B4A0E5'
colorButtonsFg = '#000000'

def download(url):
    if 'http' not in url:
        url = 'https://' + url
    
    if 'https://prehrajto.cz' not in url and 'https://prehraj.to' not in url:
        return ['None']
    
    r = requests.get(url)
    return rex.findall(r.text)

window = tk.Tk()
window.title('PTDL')
window.geometry('450x200')
window.minsize(450, 200)
window['bg'] = colorBg

chosenVar = tk.StringVar()
inpute = tk.StringVar()
statusVar = tk.StringVar()
searchVar = tk.StringVar()

statusVar.set('Waiting for input...')
chosenVar.set('None')

topFrame = tk.Frame(window, bg=colorBg)
topFrame.pack(anchor='center', pady=(10, 0))

labelOpen = tk.Label(topFrame, text='Hledat na Prehraj.to:', bg=colorBg, fg=colorFg)
labelOpen.grid(row=0, column=0)

entrySearch = tk.Entry(topFrame, textvariable=searchVar, bg=colorBox, fg=colorFg, width=35)
entrySearch.grid(row=0, column=1, padx=15)

def openPrehrajT():
    openPrehraj()

openButton = tk.Button(topFrame, text='Search', command=openPrehrajT, bg=colorButtons, fg=colorButtonsFg)
openButton.grid(row=0, column=2, sticky=tk.W)

labelDownload = tk.Label(topFrame, text='Prehraj.to link filmu: ', bg=colorBg, fg=colorFg)
labelDownload.grid(row=1, column=0, sticky=tk.E)

inputEntry = tk.Entry(topFrame, textvariable=inpute, bg=colorBox, fg=colorFg, width=35)
inputEntry.grid(row=1, column=1, padx=15, pady=15)

def editMenuT():
    editMenu()

submitButton = tk.Button(topFrame, text='Query', command=editMenuT, bg=colorButtons, fg=colorButtonsFg)
submitButton.grid(row=1, column=2, sticky=tk.W)

labelResolution = tk.Label(topFrame, text='Resolution: ', bg=colorBg, fg=colorFg)
labelResolution.grid(row=2, column=0, sticky=tk.E)

options = tk.OptionMenu(topFrame, chosenVar, 'None')
options['highlightbackground'] = colorBg
options['activebackground'] = '#9e9e9e'
options['bg'] = '#4e4e4e'
options['fg'] = colorFg
options.grid(row=2, column=1)

def editMenu():
    options['menu'].delete(0, 'end')
    found = download(inpute.get())
    
    if found == ['None']:
        statusVar.set('Invalid link!')
        chosenVar.set('None')
        options['menu'].add_command(label='None', command=lambda: chosenVar.set('None'))
        return

    for i in found:
        url = i[0]
        resolutoin = i[1]
        helpDict[resolutoin] = url
        options['menu'].add_command(label=resolutoin, command=lambda resolutoin=resolutoin: chosenVar.set(resolutoin))
        chosenVar.set(resolutoin)

    if len(found) == 0:
        chosenVar.set('None')
        options['menu'].add_command(label='None', command=lambda: chosenVar.set('None'))
        statusVar.set('No possibilities found!')
    else:
        statusVar.set('Found ' + str(len(found)) + ' possibilities!')

def openWeb():
    if chosenVar.get() != 'None' and chosenVar.get() != '':
        webbrowser.open(helpDict[chosenVar.get()], new=2, autoraise=True)
        statusVar.set('Done! Opening in browser...\nPlease select three dots in the bottom right corner and click "Download"!')
        return True
    return False

def openPrehraj():
    webbrowser.open(f'https://prehraj.to/hledej/{urllib.parse.quote(searchVar.get())}', new=2, autoraise=True)
    statusVar.set('Opening in browser...\nPlease search for a movie and copy the link to it!')

downloadButton = tk.Button(topFrame, text='Download', command=openWeb, bg=colorButtons, fg=colorButtonsFg)
downloadButton.grid(row=2, column=2, sticky=tk.W)

outputLabel = tk.Label(topFrame, textvariable=statusVar, bg=colorBg, fg=colorFg)
outputLabel.grid(row=3, column=0, columnspan=3, pady=(15, 0))

window.mainloop()