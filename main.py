###import library 
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app=FastAPI()

@component
def Ragshan_SAMSUNG():
### Creating state
    alltodo = use_state([])
    first_name, set_first_name = use_state("")
    Last_name,set_Last_name=use_state("")
    Android_Verson,set_Android_Verson=use_state("Android 13")
    E_mail,set_E_mail=use_state("")
    phone_number,set_phone_number=use_state("")
    password, set_password = use_state(0)



    def submit(event):
        newtodo = {"first_name": first_name,"Last_name":Last_name,"Android_Verson":Android_Verson,"E_mail":E_mail,"phone_number":phone_number,"password": password}

# push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
# login function using the submitted data        
        login(newtodo)  

    
# looping data  to show on web
    list = []
    def handle_event(event):
        print(event)
        
        
# adding baground image
    return html.div(
      {"style": 
         {"padding": "50px","display": "flex",
          "align-items": "Right",
            "justify-content": "Right",
          "background_image":"url(https://reactpy.neocities.org/photo/1.jpg)", 
          "background-size":"cover",
           "margin": "0px",
           "min-height": "700px",
           "min-width":"700px",
           }
           },

#### Here from submitting form

# creating form to get sign up page
        html.form(
        
               {"on submit": submit},
                html.b(html.h1(
                    {"style": {"font-family": "Georgia, serif", "font-size": "50px","color":"LightCyan"}}
                    ,"SAMSUNG  COMMUNITY & FREE",)),
                
                html.br(),

                    html.b(html.h2(
                    {"style": {"font-family": "Georgia, serif", "font-size": "30px","color":"LightCyan"}}
                    ,'Fill Here To SignUP ')),

##here the input parts start   


#First Name 
                html.p(""),
                html.label(
                    {"style": {"font-family": "Georgia, serif", "font-size": "25px","color":"#e6fffa"}}
                    ,"First Name"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "First name",
                        "on_change": lambda event: set_first_name(event["target"]["value"]),
                          "style": {
                             "font-family": "Georgia, serif",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "2px solid #1E90FF",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#ADD8E6",
                            "color": "red",
                            "outline": "none",
                            "box-shadow": "0 0 10px rgba(30, 144, 255, 0.5)",
                            },
                        
                    }
                    ),
                html.br(),

#Last Name        
                html.p(""),
                html.label(
                    {"style": {"font-family": "Georgia, serif", "font-size": "25px","color":"#e6fffa"}}
                    ,"Last Name"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Last name",
                        "on_change": lambda event: set_Last_name(event["target"]["value"]),
                        "style": {
                            "font-family": "Georgia, serif",
                            "font-size": "20px",
                            "padding": "10px 15px",
                            "border": "2px solid #1E90FF",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#ADD8E6",
                            "color": "red",
                            "outline": "none",
                            "box-shadow": "0 0 10px rgba(30, 144, 255, 0.5)",
                            },
                    }
                ),
                html.br(),

#Android verson

# add a drop down box    
                html.p(""),
                html.label(
                    {"style": {"font-family": "Georgia, serif", "font-size": "25px","color":"#e6fffa"}}
                    ,"Android Verson"),
                html.br(),
                html.select(
                    {  
                        "on_change": lambda event: set_Android_Verson(event["target"]["value"]),
                        "style":{
                            "font-family": "Georgia, serif",
                            "font-size": "20px",
                            "padding": "10px 15px",
                            "border": "2px solid #1E90FF",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#ADD8E6",
                            "color": "red",
                            "outline": "none",
                            "box-shadow": "0 0 10px rgba(30, 144, 255, 0.5)"}
                        
#add options to drop down box
                    },
                    
                    html.option(
                    {
                        "value":"Android 13",
                        "style":{
                            "font-family": "Georgia, serif",
                            "font-size": "20px",
                            "padding": "10px 15px",
                            "border": "2px solid #1E90FF",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#ADD8E6",
                            "color": "red",
                            "outline": "none",
                            "box-shadow": "0 0 10px rgba(30, 144, 255, 0.5)"}
                    },"Android 13"),
                    
                    html.option(
                    {
                        "value":"Android 12",
                        "style":{
                            "font-family": "Georgia, serif",
                            "font-size": "20px",
                            "padding": "10px 15px",
                            "border": "2px solid #1E90FF",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#ADD8E6",
                            "color": "red",
                            "outline": "none",
                            "box-shadow": "0 0 10px rgba(30, 144, 255, 0.5)"}
                    },"Android 12"),
                   
                    html.option(
                    {
                        "value":"Android 11",
                        "style":{
                            "font-family": "Georgia, serif",
                            "font-size": "20px",
                            "padding": "10px 15px",
                            "border": "2px solid #1E90FF",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#ADD8E6",
                            "color": "red",
                            "outline": "none",
                            "box-shadow": "0 0 10px rgba(30, 144, 255, 0.5)"}
                    },"Android 11"),

                    html.option(
                    {
                        "value":"Android 10",
                        "style":{
                            "font-family": "Georgia, serif",
                            "font-size": "20px",
                            "padding": "10px 15px",
                            "border": "2px solid #1E90FF",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#ADD8E6",
                            "color": "red",
                            "outline": "none",
                            "box-shadow": "0 0 10px rgba(30, 144, 255, 0.5)"}
                    },"Android 10"),

                    html.option(
                    {
                        "value":"Android 9",
                        "style":{
                            "font-family": "Georgia, serif",
                            "font-size": "20px",
                            "padding": "10px 15px",
                            "border": "2px solid #1E90FF",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#ADD8E6",
                            "color": "red",
                            "outline": "none",
                            "box-shadow": "0 0 10px rgba(30, 144, 255, 0.5)"}
                    },"Android 9"),
                   
                    html.option(
                    {
                        "value":"Android 8",
                        "style":{
                            "font-family": "Georgia, serif",
                            "font-size": "20px",
                            "padding": "10px 15px",
                            "border": "2px solid #1E90FF",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#ADD8E6",
                            "color": "red",
                            "outline": "none",
                            "box-shadow": "0 0 10px rgba(30, 144, 255, 0.5)"}
                    },"Android 8")
                ),
                html.br(),
                html.br(),


       
#E-Mail Address
                html.p(""),
                html.label(
                    {"style": {"font-family": "Georgia, serif", "font-size": "25px","color":"#e6fffa"}}
                    ,"E-Mail Address"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Email",
                        "on_change": lambda event: set_E_mail(event["target"]["value"]),
                        "style": {
                            "font-family": "Georgia, serif",
                            "font-size": "20px",
                            "padding": "10px 15px",
                            "border": "2px solid #1E90FF",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#ADD8E6",
                            "color": "red",
                            "outline": "none",
                            "box-shadow": "0 0 10px rgba(30, 144, 255, 0.5)",
                            },
                    }
                    ),
                html.br(),

        
#Phone Number
                html.p(""),
                html.label(
                    {"style": {"font-family": "Georgia, serif", "font-size": "25px","color":"#e6fffa"}}
                    ,"Phone Number"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Phone number",
                        "on_change": lambda event: set_phone_number(event["target"]["value"]),
                        "style": {
                             "font-family": "Georgia, serif",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "2px solid #1E90FF",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#ADD8E6",
                            "color": "red",
                            "outline": "none",
                            "box-shadow": "0 0 10px rgba(30, 144, 255, 0.5)",
                            },
                    }
                ),
                html.br(),

        
#password
                html.p(""),
                html.label(
                    {"style": {"font-family": "Georgia, serif", "font-size": "25px","color":"#e6fffa"}}
                    ,"Password"),
                html.br(),
                html.input(
                    {
                        "type": "password",
                        "placeholder": "Password",
                        "on_change": lambda event: set_password(event["target"]["value"]),
                        "style": {
                             "font-family": "Georgia, serif",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "2px solid #1E90FF",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#ADD8E6",
                            "color": "red",
                            "outline": "none",
                            "box-shadow": "0 0 10px rgba(30, 144, 255, 0.5)",
                            },
                    }
                ),   
                html.br(),



# creating submit button on form

#button 1
                html.p(""),
                html.button(
                    {
                        "type": "Create an Account",
                        "on_click":event(lambda event:submit(event)),
                        "style": {
                             "font-family": "Georgia, serif",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "darkblue",
                            "color": "#f4f5f0",
                            "outline": "none",
                            "animation":"pulse 2s infinite"
                            
                            },
                    },
                    "Create A Samsung Account",
                ),

        
#button 2
                html.button(
                {
                    "type": "Clear",
                    "on_click":lambda event: set_first_name("") and set_Last_name("") and set_Android_Verson("") and set_E_mail("") and set_phone_number("") and set_password(0),
                    "style": {
                            "font-family": "Georgia, serif",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "darkblue",
                            "color": "#f4f5f0",
                            "outline": "none",
                            "animation":"pulse 2s infinite"
                            },
                },
                "Clear Input Data",
                ),
                ),
        html.ul(list),  
       
    )

##Connect with mongoDB with my database using my admin access
uri = "mongodb+srv://admin:123@cluster1.zswhydo.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi("1"))

#defining the database name and collection
db = client["DataA"]
collection = db["DataB"]

#checking the connection 
try:
    client.admin.command("ping")
    print("SUCESSFULLY CONNECTED WITH MONGIDB")
except Exception as r:
    print(r)


def login(
    login_data: dict,
):  

# removed async, since await makes code execution pause for the promise to resolve anyway. doesnt matter.
    first_name= login_data["first_name"]
    Last_name=login_data["Last_name"]
    Android_Verson=login_data["Android_Verson"]
    E_mail=login_data["E_mail"]
    phone_number=login_data["phone_number"]
    password = login_data["password"]

# Create a document to insert into the collection
    Private_data = {"first_name": first_name,"Last_name":Last_name,"Android_Verson":Android_Verson,"phone_number":phone_number}

#Creating a document within a document (optimising the data)
    document = {"E_mail":E_mail,"Private_data":Private_data,"password": password}



#sample log in message
    print(document)

# Insert the document into the collection
    post_id = collection.insert_one(document).inserted_id  # insert document
    print(post_id)

    return {"message": "YOU ARE LOGIN SUCESSFULLY"}

configure(app, Ragshan_SAMSUNG)

