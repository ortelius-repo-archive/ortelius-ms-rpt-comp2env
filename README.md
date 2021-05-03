# ortelius-ms-rpt-comp2env
A python flask app that maintains the list of countries and there presidents and supports CRUD operations around it. 

### API LIST
Following APIs are available in the app.

#### Add a president
**Method :** POST  
**Endpoint :** http://localhost:5000/presidents  

#### Delete a president
**Method :** DELETE  
**Endpoint :** http://localhost:5000/presidents/country

#### Update a president
**Method :** PUT  
**Endpoint :** http://localhost:5000/presidents

#### Get a president
**Method :** GET  
**Endpoint :** http://localhost:5000/presidents/country

#### Get all presidents
**Method :** GET  
**Endpoint :** http://localhost:5000/presidents

### Run the app
To run the app locally use Python 3 \
`$ python main.py`

To dockerize the app \
`$ cd ortelius-ms-rpt-comp2env` \
`$ docker build -t comp2env:v1 .` \
`$ docker run -it -p 5000:80 comp2env:v1`

