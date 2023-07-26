from ctypes import alignment
import webbrowser
import tkinter as tk
from tkinter import *
import os
from conn import *
from variables_for_queries import *
fields = 'Song Name', 'Album Name', 'Artist Name'
temp_song = ''
temp_album = ''
temp_artist = ''
dtd= ''
dcn= ''
dvn= ''

def get_venue_details():


    if temp_song!='':   
		#print(venue_details_query_bySong)
        cursor.execute(venue_details_query_bySong)
        list_of_venue_details_bySong = cursor.fetchall()

        for i in range(len(list_of_venue_details_bySong)):
            display_tour_date = list_of_venue_details_bySong[i][0]
            display_country_name = list_of_venue_details_bySong[i][1]
            display_venue_name = list_of_venue_details_bySong[i][2]
            # global dtd
            dtd=display_tour_date
            dcn=display_country_name
            dvn=display_venue_name
            print(display_tour_date,display_country_name,display_venue_name)
			#print(list_of_venue_details_bySong)
            print(list_of_venue_details_bySong)
            return list_of_venue_details_bySong
    elif temp_album!='':

		#print(venue_details_query_byAlbum)
        cursor.execute(venue_details_query_byAlbum)
        print(venue_details_query_byAlbum)
        list_of_venue_details_byAlbum = cursor.fetchall()
        
        for i in range(len(list_of_venue_details_byAlbum)):

            display_tour_date = list_of_venue_details_byAlbum[i][0]
            display_country_name = list_of_venue_details_byAlbum[i][1]
            display_venue_name = list_of_venue_details_byAlbum[i][2]
            # global dtd
            # global dcn
            # global dvn
            dtd=display_tour_date
            dcn=display_country_name
            dvn=display_venue_name
            print(display_tour_date,display_country_name,display_venue_name)
            #print(list_of_venue_details_byAlbum)
            return list_of_venue_details_byAlbum
    elif temp_artist!='':

		#print(venue_details_query_byArtist)
        cursor.execute(venue_details_query_byArtist)
        list_of_venue_details_byArtist = cursor.fetchall()
        for i in range(len(list_of_venue_details_byArtist)):
	
            display_tour_date = list_of_venue_details_byArtist[i][0]
            display_country_name = list_of_venue_details_byArtist[i][1]
            display_venue_name = list_of_venue_details_byArtist[i][2]
            # global dtd
            # global dcn
            # global dvn
            dtd=display_tour_date
            dcn=display_country_name
            dvn=display_venue_name
            print(display_tour_date,display_country_name,display_venue_name)
			#print(list_of_venue_details_byArtist)
            return list_of_venue_details_byArtist

def fetch(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        if field=='Song Name':
            if text!='':
                global temp_song
                temp_song = text
                f = open("temp_song.txt", "w")
                f.write("'"+temp_song+"'")
                f.close()
        elif field=='Album Name':
            if text!='':
                global temp_album
                temp_album = text
                print(temp_album)
                f = open("temp_album.txt", "w")
                f.write("'"+temp_album+"'")
                f.close()
        elif field=='Artist Name':
            if text!='':
                global temp_artist
                temp_artist = text
                f = open("temp_artist.txt", "w")
                f.write("'"+temp_artist+"'")
                f.close()

        #print('%s: "%s"' % (field, text)) 
def erase_entries():
    f = open("temp_song.txt", "w")
    f.write("")
    f.close()
    f = open("temp_album.txt", "w")
    f.write("")
    f.close()
    f = open("temp_artist.txt", "w")
    f.write("")
    f.close()
def check_if_null():
    if temp_song!='':
        print(temp_song)
        get_song_details()  
    elif temp_album!='':
        get_album_details()
        get_album_songs()   
    elif temp_artist!='':
        get_artist_details()
        get_artist_albums()
        get_artist_songs()
	
def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=50, text=field, anchor='w')
        ent = tk.Entry(row)
        '''row.grid(row=0, column=0, sticky='nsew')
        lab.grid(row=2, column=0)
        ent.grid(row=2, column=1)'''
        row.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

def win_song_details():
    global song_details_window
    print(display_album_name)
    song_details_window= tk.Toplevel()
    song_details_window.geometry("650x500")
    song_details_window.title("Song Details")
    song_details_bg=tk.PhotoImage(file="C:/Users/Aariz Khan/Desktop/Code/DBMS Songs Lib/song1 show details.png")
    # Show image using label
    labelForSongDetails = Label(song_details_window, image = song_details_bg)
    labelForSongDetails.place(x = 0,y = 0)
    l=get_song_details()
    '''
    genre=l[0][0]
    duration=l[0][1]
    year_released=l[0][2]
    display_artist_name=l[0][3]
    display_album_name=l[0][4]'''
    #Create a Label in New window
    global url
    url = l[0][5]
    def playSong():
        songurl= "start chrome.exe "+url
        os.system(songurl)
    Label(song_details_window, text=temp_song , bg = "#fbf49a", font=('Times 12 bold')).place(x = 200, y = 220)
    Label(song_details_window, text=l[0][4] , bg = "#fbf49a", font=('Times 7 bold')).place(x = 200, y = 310)
    Label(song_details_window, text= l[0][3], bg = "#fbf49a", font=('Times 12 bold')).place(x = 200, y = 395)
    Label(song_details_window, text= l[0][2], bg = "#fbf49a", font=('Times 12 bold')).place(x = 480, y = 220)
    Label(song_details_window, text= l[0][1], bg = "#fbf49a", font=('Times 12 bold')).place(x = 430, y = 308)
    Label(song_details_window, text= l[0][0], bg = "#fbf49a", font=('Times 12 bold')).place(x = 415, y = 395)
    #url_label = tk.Label(song_details_window, text= l[0][5], bg = "#fbf49a", font=('Times 8 bold')).place(x = 2, y = 479)
    songLink = tk.Button(song_details_window, text='Play Now', fg = 'red', bg = 'black', height = 2, width = 20, command=(lambda: [playSong()]))
    
        
    #b4.pack(side=tk.TOP, padx=10, pady=10)
    songLink.place(relx=0.5,y=470, anchor="center")
    '''def callback(event):
        webbrowser.open_new(event.widget.cget("text"))
        
    url_label.bind("<URL>",callback())'''
    song_details_window.mainloop()  
    
def win_tour_details():
        global tour_details_window
        #print(display_album_name)
        tour_details_window= tk.Toplevel()
        tour_details_window.geometry("650x500")
        tour_details_window.title("Song Details")
        tour_details_bg=tk.PhotoImage(file="C:/Users/Aariz Khan/Desktop/Code/DBMS Songs Lib/Tours1 show details.png")
        # Show image using label
        labelForTourDetails = Label(tour_details_window, image = tour_details_bg)
        labelForTourDetails.place(x = 0,y = 0)
        l=get_venue_details()
        #Create a Label in New window
        Label(tour_details_window, text= l[0][1], bg = "#fbf49a", font=('Times 12 bold')).place(x = 320, y = 220)
        Label(tour_details_window, text= l[0][2], bg = "#fbf49a", font=('Times 12 bold')).place(x = 320, y = 310)
        Label(tour_details_window, text= l[0][0], bg = "#fbf49a", font=('Times 12 bold')).place(x = 320, y = 410)
        tour_details_window.mainloop()

def run():
    global root
    geo_x=900
    geo_y=635
    geo=str(geo_x)+'x'+str(geo_y)
    root = tk.Tk()
    root.geometry(geo)
    root.title("Music Database Search Engine")
    bg = tk.PhotoImage(file = "MainBG.png")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = 0)
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
    song_details_window=tk.Toplevel()
    
    '''def open_win():
        new= tk.Toplevel()
        new.geometry("650x500")
        new.title("New Window")
    #Create a Label in New window
        Label(new, text="Hey, Howdy?", font=('Times 17 bold')).pack(pady=30) '''

    
    

    #b1.grid(row=3, column=1)
    #b1.pack(side=tk.BOTTOM, padx=10, pady=10)
    b2 = tk.Button(root, text='QUIT', fg = 'red', bg = 'turquoise', height = 2, width = 10, command=lambda :[root.quit(),erase_entries()])
    #b2.grid(row=3, column=2)
    #b2.pack(side=tk.TOP, padx=10, pady=10)
    b2.place(relx=0.5,y=370,anchor="center")

    b3 = tk.Button(root, text='SHOW DETAILS', fg = 'blue', bg = 'turquoise', height = 2, width = 20, command=(lambda e=ents: [fetch(e),check_if_null(),win_song_details()]))
    #b3.pack(side=tk.TOP, padx=10, pady=10)
    b3.place(relx=0.5,y=185, anchor="center")

    b4 = tk.Button(root, text='SHOW TOUR INFO', fg = 'black', bg = 'turquoise', height = 2, width = 20, command=(lambda e = ents: [fetch(e),get_venue_details(),win_tour_details()]))
    #b4.pack(side=tk.TOP, padx=10, pady=10)
    b4.place(relx=0.5,y=250, anchor="center") 

    '''b5 = tk.Button(root, text='SHOW TOUR INFO', fg = 'orange', bg = 'turquoise', height = 2, width = 20, command=lambda e = ents: fetch(e))
    b5.pack(side=tk.TOP, padx=10, pady=10)
    b5.place(x=320,y=300)'''
    root.mainloop()
run()