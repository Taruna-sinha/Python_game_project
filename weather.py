from tkinter import*
from PIL import Image,ImageTk
import w
import requests
class MyWeather:
    def __init__(self,root):
        self.root=root
        self.root.title("My weather app")
        w=550
        h=300
        x=450    
        y=300
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        #==icon===
        self.search_icon=Image.open("icons/search_icon.png")
        self.search_icon=self.search_icon.resize((30,30),Image.ANTIALIAS)
        self.search_icon=ImageTk.PhotoImage(self.search_icon)

        #====variable====
        self.var_search=StringVar()
        self.root.config(bg="white")
        title=Label(self.root,text="Weather App",font=("goudy old style",30,"bold"),bg="Black",fg="white").place(x=0,y=0,relwidth=1,height=60)
        lbl_city=Label(self.root,text="City Name",font=("goudy old style",15),bg="dark blue",fg="white",anchor="w").place(x=0,y=60,relwidth=1,height=40)
        txt_city=Entry(self.root,textvariable=self.var_search,font=("goudy old style",15),bg="lightyellow",fg="black").place(x=100,y=65,width=200,height=30)
        btn_city=Button(self.root,cursor="hand2",image=self.search_icon,bd=0,bg="dark blue",command=self.get_weather).place(x=500,y=65,width=40,height=30)

        #Result
        self.lbl_city=Label(self.root,font=("goudy old style",15),bg="white",fg="green")
        self.lbl_city.place(x=0,y=110,relwidth=1,height=20)

        self.lbl_icons=Label(self.root,font=("goudy old style",15),bg="white")
        self.lbl_icons.place(x=0,y=132,relwidth=1,height=80)

        self.lbl_temp=Label(self.root,font=("goudy old style",15),bg="white",fg="blue")
        self.lbl_temp.place(x=0,y=200,relwidth=1,height=20)

        self.lbl_wind=Label(self.root,font=("goudy old style",15),bg="white",fg="dark blue")
        self.lbl_wind.place(x=0,y=220,relwidth=1,height=20)

        self.lbl_Error=Label(self.root,font=("goudy old style",15),bg="white",fg="Red")
        self.lbl_Error.place(x=0,y=245,relwidth=1,height=20)
        #footer
        self.lbl_footer=Label(self.root,text="Developed by Taruna",font=("goudy old style",15),bg="dark blue",fg="white")
        self.lbl_footer.pack(side="bottom",fill="x")

    def get_weather(self):
        api_key=w.api_key
        complete_url=f"http://api.openweathermap.org/data/2.5/weather?q={self.var_search.get()}&appid={api_key}"
        #cityname,country name,icons,temp_c,temp_f,wind
        if self.var_search.get()=="":
            self.lbl_city.config(text="")
            self.lbl_icons.config(image="")
            self.lbl_temp.config(text="")
            self.lbl_wind.config(text="")
            self.lbl_Error.config(text="City name required")
        else:
            result=requests.get(complete_url)
            if result:
                json=result.json()
                city_name=json["name"]
                country=json["sys"]["country"]
                icons=json["weather"][0]["icon"]
                temp_c=json["main"]["temp"]-273.15            
                temp_f=(json["main"]["temp"]- 273.15)*9/5 + 32
                wind=json["weather"][0]["main"]
                self.lbl_city.config(text=city_name+","+country)
                #new_icon
                self.search_icon2=Image.open(f"icons/{icons}.png")
                self.search_icon2=self.search_icon2.resize((80,80),Image.ANTIALIAS)
                self.search_icon2=ImageTk.PhotoImage(self.search_icon2)
                self.lbl_icons.config(image=self.search_icon2)
                deg=u"\N{degree sign}"
                self.lbl_temp.config(text=str(round(temp_c,2))+deg+" C | "+str(round(temp_f,2))+deg+"f")
                self.lbl_wind.config(text=wind)
                self.lbl_Error.config(text="")
                # print(city_name,country,icons,temp_c,temp_f,wind)
            else:
                self.lbl_city.config(text="")
                self.lbl_icons.config(image="")
                self.lbl_temp.config(text="")
                self.lbl_wind.config(text="")
                self.lbl_Error.config(text="Invalid city name")
root=Tk()
obj=MyWeather(root)
root.mainloop()
