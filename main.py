from fastapi import FastAPI

app=FastAPI(title= "My FastAPI app") #Defualt for all project main.py to connect fastapi

@app.get("/") #Decorator to define a GET endpoint at the root URL
def read_root(): #Function to handle the GET request
    return {"message":"Hello, FastAPI!"} #Return a JSON response with a message


