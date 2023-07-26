import mysql.connector
import tkinter  as tk 
from tkinter import * 
import pyodbc 
#from Song_Lib_Input import *
#from variables_for_queries import *

def listToString(s):
   
    str1 = ""
    return (str1.join(s))

'''def get_venue_details():

	if temp_song!='':
		global display_tour_date
		global display_country_name
		global display_venue_name
		#print(venue_details_query_bySong)
		cursor.execute(venue_details_query_bySong)
		list_of_venue_details_bySong = cursor.fetchall()
		for i in range(len(list_of_venue_details_bySong)):
			display_tour_date = list_of_venue_details_bySong[i][0]
			display_country_name = list_of_venue_details_bySong[i][1]
			display_venue_name = list_of_venue_details_bySong[i][2]
			print(display_tour_date,display_country_name,display_venue_name)
			#print(list_of_venue_details_bySong)
	elif temp_album!='':
		global display_tour_date
		global display_country_name
		global display_venue_name
		#print(venue_details_query_byAlbum)
		cursor.execute(venue_details_query_byAlbum)
		list_of_venue_details_byAlbum = cursor.fetchall()
		for i in range(len(list_of_venue_details_byAlbum)):
			display_tour_date = list_of_venue_details_byAlbum[i][0]
			display_country_name = list_of_venue_details_byAlbum[i][1]
			display_venue_name = list_of_venue_details_byAlbum[i][2]
			print(display_tour_date,display_country_name,display_venue_name)
			#print(list_of_venue_details_byAlbum)
	elif temp_artist!='':
		global display_tour_date
		global display_country_name
		global display_venue_name
		#print(venue_details_query_byArtist)
		cursor.execute(venue_details_query_byArtist)
		list_of_venue_details_byArtist = cursor.fetchall()
		for i in range(len(list_of_venue_details_byArtist)):

			display_tour_date = list_of_venue_details_byArtist[i][0]
			display_country_name = list_of_venue_details_byArtist[i][1]
			display_venue_name = list_of_venue_details_byArtist[i][2]
			print(display_tour_date,display_country_name,display_venue_name)
			#print(list_of_venue_details_byArtist)'''

		
with open('temp_album.txt') as f:
    album_name = f.read()
album_name = listToString(album_name)
with open('temp_artist.txt') as f:
	artist_name = f.read()
artist_name = listToString(artist_name)
with open('temp_song.txt') as f:
	song_name = f.read()
song_name = listToString(song_name)

conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=(LocalDb)\LocalDBTest;'
                      'Database=music_library;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
query = "SELECT * FROM Albums where Name = " + album_name
song_details_query= "Select s.Genre, s.Duration, s.[Year Released], a.Name, d.Name, s.[spotify links] from Songs s,Artists a, Albums d  where s.[song ID]=(Select [Song ID] from Songs where Name ="+ song_name +") and s.[Artist ID]  = a.[Artist ID] and s.[Album ID] = d.[Album ID]"
album_details_query = "Select a.Name, d.[Year Released] from Albums d, Artists a where d.[Album ID] =(Select [Album ID] from Albums where Name ="+ album_name+")and d.[Artist ID] = a.[Artist ID]"
album_songs_query = "Select s.Name from Albums d, Songs s where d.[Album ID] =(Select [Album ID] from Albums where Name ="+album_name+") and d.[Album ID] = s.[Album ID]"
artist_details_query = "Select a.[Debut Year], l.Label, l.[Signed On], m.Name from Artists a, Label l, Managers m where a.[Artist ID] =(Select [Artist ID] from Artists where Name ="+ artist_name +") and a.[Artist ID] = l.[Artist ID] and l.[Label ID] = m.[Label ID]"
artist_albums_query = "Select d.Name from Albums d, Artists a where a.[Artist ID] =(Select [Artist ID] from Artists where Name ="+ artist_name +") and a.[Artist ID] = d.[Artist ID]"
artist_songs_query = "Select s.Name from Artists a, Songs s where a.[Artist ID] =(Select [Artist ID] from Artists where Name ="+ artist_name +") and a.[Artist ID] = s.[Artist ID]"
venue_details_query_bySong = "Select t.Date, t.Country, v.Name from Tours t, Venue v, Songs s where [Song ID]=(Select [Song ID] from Songs where Name =" + song_name+") and s.[Artist ID] = t.[Artist ID] and  t.[Venue ID]  = v.[Venue ID]"
venue_details_query_byArtist = "Select t.Date, t.Country, v.Name from Tours t, Venue v, Artists a where a.[Artist ID]=(Select [Artist ID] from Artists where Name =" + artist_name+") and a.[Artist ID] = t.[Artist ID] and  t.[Venue ID]  = v.[Venue ID]"
venue_details_query_byAlbum = "Select t.Date, t.Country, v.Name from Tours t, Venue v, Albums d where d.[Album ID]=(Select [Album ID] from Albums where Name =" + album_name+") and d.[Artist ID] = t.[Artist ID] and  t.[Venue ID]  = v.[Venue ID]"

def get_song_details():

	print(song_details_query)
	cursor.execute(song_details_query)
	#print(cursor.fetchall())]
	list_of_song_details = cursor.fetchall()
	return list_of_song_details
	
	print(list_of_song_details)
	
def get_album_details():
	global display_artist_name
	global year_released
	print(album_details_query)
	cursor.execute(album_details_query)
	list_of_album_details = cursor.fetchall()
	display_artist_name=list_of_album_details[0][0]
	year_released=list_of_album_details[0][1]
	#print(list_of_album_details)

def get_album_songs():
	global display_song_name
	print(album_songs_query)
	cursor.execute(album_songs_query)
	list_of_album_songs = cursor.fetchall()
	for i in range(len(list_of_album_songs)):
		display_song_name = list_of_album_songs[i][0]
		print(display_song_name)
		#print(list_of_album_songs)

def get_artist_details():
	global debut_year
	global label_name
	global signed_on
	global manager_name
	print(artist_details_query)
	cursor.execute(artist_details_query)
	list_of_artist_details = cursor.fetchall()
	debut_year=list_of_artist_details[0][0]
	label_name=list_of_artist_details[0][1]
	signed_on=list_of_artist_details[0][2]
	manager_name=list_of_artist_details[0][3]
	#print(list_of_artist_details)

def get_artist_albums():
	global display_album_name
	print(artist_albums_query)
	cursor.execute(artist_albums_query)
	list_of_artist_albums = cursor.fetchall()
	for i in range(len(list_of_artist_albums)):
		display_album_name = list_of_artist_albums[i][0]
		print(display_album_name)
		#print(list_of_artist_albums)
	#print(list_of_artist_albums)

def get_artist_songs():
	global display_song_name
	print(album_songs_query)
	cursor.execute(artist_songs_query)
	list_of_artist_songs = cursor.fetchall()
	for i in range(len(list_of_artist_songs)):
		display_song_name = list_of_artist_songs[i][0]
		print(display_song_name)
		#print(list_of_artist_songs)
	#print(list_of_artist_songs)

'''def get_venue_details():
	if temp_song!='':
		#print(venue_details_query_bySong)
		cursor.execute(venue_details_query_bySong)
		list_of_venue_details_bySong = cursor.fetchall()
		print(list_of_venue_details_bySong)
	elif temp_artist!='':
		#print(venue_details_query_byArtist)
		cursor.execute(venue_details_query_byArtist)
		list_of_venue_details_byArtist = cursor.fetchall()
		print(list_of_venue_details_byArtist)
	elif temp_album!='':
		#print(venue_details_query_byAlbum)
		cursor.execute(venue_details_query_byAlbum)
		list_of_venue_details_byAlbum = cursor.fetchall()
		print(list_of_venue_details_byAlbum)'''