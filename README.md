# Icarus
Man shall never reach his full capacity while chained to the earth. We must take wing and conquer the REST API framework for Django.



# Docker
```
docker-compose run web python3 manage.py migrate
docker-compose up
```

## View for apply sdkl-campaign rules and to show API requests stored in database
http://localhost:8000/coupons.  
Use form to add SDKL-Campaign rules.  
(submit form).

## First need to get TOKEN:
```
curl --header "Content-Type: application/json" \
--request POST   \
--data '{"username":"evvs7testcase","password":"pleasetoken"}' \
http://127.0.0.1:8000/get-api-token/
```

## Okay, we ready to fight ( API request )
```
curl -H "Content-Type: application/json" \
   -H 'Authorization: Token %TOKEN%' \
   --request POST \
   --data '{
        "ptcs": {
            "ADT": 1,
            "CHD": 1,
            "INF": 1
        },
        "ssdkl": "9a9c4face96c4314b8ff939f9682be14",
        "origin": "DME",
        "destination": "LED",
        "departure": "2018-10-20"
    }' \
   http://127.0.0.1:8000/dpcheck
```

## Can use POSTMAN
https://www.getpostman.com/.   
Dont forget about TOKEN and valid HEADER.  
![Post form example](https://preview.ibb.co/b6tD9U/2018-10-13-19-48-18.png)

