# Icarus
Man shall never reach his full capacity while chained to the earth. We must take wing and conquer the REST API framework for Django.

# POST JSON
## Via curl


## First need to get TOKEN:
```
curl --header "Content-Type: application/json" \
--request POST   \
--data '{"username":"usertoken","password":"s7testcasetoken"}' \
http://127.0.0.1:8000/get-api-token/
```

## Okay, we ready to fight
```
curl -H "Content-Type: application/json" \
   -H 'Authorization: Token 850652a6a769687a7f10af2768e458a4c7464dfd' \
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

## Via POSTMAN
https://www.getpostman.com/
Dont forget about TOKEN and valid HEADER.
![Post form example](https://preview.ibb.co/b6tD9U/2018-10-13-19-48-18.png)

