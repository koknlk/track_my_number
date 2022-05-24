from ast import operator
from time import time
from tkinter import *
from turtle import heading, home, title
from unittest import result
from matplotlib.pyplot import text;
import phonenumbers;
from phonenumbers import carrier;
from phonenumbers import geocoder;
from phonenumbers import timezone;
from timezonefinder import TimezoneFinder;
from geopy.geocoders import Nominatim;
from datetime import date, datetime;
import pytz;


root=Tk();
root.title("Ping My Number");
root.geometry("365x584+400+200");
root.resizable(False,False);

def track():
    enter_number=entry.get();
    number=phonenumbers.parse(enter_number);
    #country
    locate=geocoder.description_for_number(number, "en");
    country.config(text=locate);

    #operator
    operator=carrier.name_for_number(number,"en");
    sim.config(text=operator);

    #phone timezone
    time=timezone.time_zones_for_number(number);
    zone.config(text=time);

    #longitude and latitude
    geolocator=Nominatim(user_agent="geopiExercises");
    location=geolocator.geocode(locate);

    lng=location.longitude;
    lat=location.latitude;
    longitude.config(text=lng);
    latitude.config(text=lat);

    #time showing in phone
    obj = TimezoneFinder();
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude);

    home=pytz.timezone(result);
    local_time=datetime.now(home);
    current_time=local_time.strftime("%I:%M:%p");
    clock.config(text=current_time);

#app logo
logo=PhotoImage(file="logo.png");

Label(root,image=logo).place(x=240,y=70);

Heading=Label(root,text="Track Number", font=("arial",20));
Heading.place(x=90,y=110);

#searchbox
entry=StringVar();
enter_number=Entry(root,textvariable=entry, width=17,bd=0, font=("arial",20),justify="center");
enter_number.place(x=50,y=220);

#button
search=Button(command=track,borderwidth=0,bd=0,bg="#57adff" ,cursor="hand2", text="Search",font=("arial",16), justify="center");
search.place(x=130,y=300);

#bottom
country=Label(root,text="Country",bg="#57adff", fg="#000",font=("arial", 10,"bold"));
country.place(x=50,y=400);

sim=Label(root,text="Sim",bg="#57adff", fg="#000",font=("arial", 10,"bold"));
sim.place(x=200,y=400);

zone=Label(root,text="Timezone",bg="#57adff", fg="#000",font=("arial", 10,"bold"));
zone.place(x=50,y=450);

clock=Label(root,text="Phone Time",bg="#57adff", fg="#000",font=("arial", 10,"bold"));
clock.place(x=50,y=450);

longitude=Label(root,text="Longitude",bg="#57adff", fg="#000",font=("arial", 10,"bold"));
longitude.place(x=50,y=500);

latitude=Label(root,text="Latitude",bg="#57adff", fg="#000",font=("arial", 10,"bold"));
latitude.place(x=200,y=400);

root.mainloop();