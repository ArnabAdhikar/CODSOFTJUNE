# designing a weather app
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

def main_func():
    city = s_text.get()
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    #print(result)
    home = pytz.timezone(result)
    local_time=datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
    # weather
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=cb3f147cc45fee38a5e3cee029566180"
    json_data = requests.get(api).json()
    print(json_data)
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data["wind"]["speed"]

    t.config(text=(temp,"°"))
    c.config(text=condition)
    d.config(text=description)
    h.config(text=humidity)
    p.config(text=pressure)
    w.config(text=wind)

root = Tk()
root.title("Weather app")
root.geometry("900x500+300+200")
root.resizable(False,False)

# search box
search_image = PhotoImage(file="search.png")
s_image = Label(image=search_image)
s_image.place(x=20, y=20)
s_text = tk.Entry(root, justify="center", width=17, font=("poppins",25), bg="#404040", border=0, fg="white")
s_text.place(x=50,y=40)
s_text.focus()

# search button
bt_icon = PhotoImage(file="icon.png")
bt = Button(image=bt_icon, borderwidth=0, cursor="hand2", bg="#404040", command=main_func)
bt.place(x=400, y=34)

# logo
l_image = PhotoImage(file="logo.png")
l_e = Label(image=l_image)
l_e.place(x=150, y=100)

# blue box
frame_img = PhotoImage(file="box.png")
frame = Label(image=frame_img, )
frame.pack(padx=5,pady=5,side=BOTTOM)

# loc. name & time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30,y=100)
clock = Label(root, font=("arial", 15))
clock.place(x=30, y=130)

# labels in the blue box
label1 = Label(root, text="Wind", font=("Helvetica", 15, "bold"), fg="white", bg= "#1ab5ef")
label1.place(x=120,y=400)
label2 = Label(root, text="Humidity", font=("Helvetica", 15, "bold"), fg="white", bg= "#1ab5ef")
label2.place(x=250,y=400)
label3 = Label(root, text="Description", font=("Helvetica", 15, "bold"), fg="white", bg= "#1ab5ef")
label3.place(x=430,y=400)
label4 = Label(root, text="Pressure", font=("Helvetica", 15, "bold"), fg="white", bg= "#1ab5ef")
label4.place(x=650,y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400,y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400,y=250)
w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120,y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280,y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450,y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670,y=430)

root.mainloop()
