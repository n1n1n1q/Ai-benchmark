def draw_spider(leg_size, body_size, mouth, eye):
    leg_types = {1: ("^", "^"), 2: ("/\\", "/\\"), 3: ("/╲", "╱\\"), 4: ("╱╲", "╱╲")}

    body_types = {1: ("(", ")"), 2: ("((", "))"), 3: ("(((", ")))")}

    legs = leg_types[leg_size]
    body_open, body_close = body_types[body_size]

    eyes_count = 2**body_size
    eyes = eye * eyes_count

    spider = f"{legs[0]}{body_open}{eyes[:eyes_count//2]}{mouth}{eyes[eyes_count//2:]}{body_close}{legs[1]}"
    return spider
