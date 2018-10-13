from datetime import datetime as dt
valid_json = {
        "ptcs": {
            "ADT": 1,
            "CHD": 1,
            "INF": 1
        },
        "ssdkl": "9a9c4face96c4314b8ff939f9682be14",
        "origin": "DME",
        "destination": "LED",
        "departure": "{}-{}-{}".format(dt.now().year, dt.now().month, dt.now().day)
}

invalid_adt_count = {
        "ptcs": {
            "ADT": 0,
            "CHD": 1,
            "INF": 1
        },
        "ssdkl": "9a9c4face96c4314b8ff939f9682be14",
        "origin": "DME",
        "destination": "LED",
        "departure": "{}-{}-{}".format(dt.now().year, dt.now().month, dt.now().day)
}

invalid_iata = {
        "ptcs": {
            "ADT": 1,
            "CHD": 1,
            "INF": 1
        },
        "ssdkl": "9a9c4face96c4314b8ff939f9682be14",
        "origin": "QQQ",
        "destination": "LED",
        "departure": "{}-{}-{}".format(dt.now().year, dt.now().month, dt.now().day)
}

invalid_departure = {
        "ptcs": {
            "ADT": 1,
            "CHD": 1,
            "INF": 1
        },
        "ssdkl": "9a9c4face96c4314b8ff939f9682be14",
        "origin": "DME",
        "destination": "LED",
        "departure": "1005-234-100"
}

invalid_ptcs = {
        "ptcs": {
            "ADT": 1
        },
        "ssdkl": "9a9c4face96c4314b8ff939f9682be14",
        "origin": "DME",
        "destination": "LED",
        "departure": "{}-{}-{}".format(dt.now().year, dt.now().month, dt.now().day)
}

invalid_json_frm = {
        "ssdkl": "9a9c4face96c4314b8ff939f9682be14",
        "origin": "DME",
        "destination": "LED",
        "departure": "{}-{}-{}".format(dt.now().year, dt.now().month, dt.now().day)
}