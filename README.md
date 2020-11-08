# Library App
My first python app using flask 
## endpoints
* save new book 
```
curl --location --request POST 'http://localhost:5000/books' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "book 1"
}'
```
* get all books  
```
curl --location --request GET 'http://localhost:5000/books'
```

* get one by id 
```
curl --location --request GET 'http://localhost:5000/books/<id>'
```
