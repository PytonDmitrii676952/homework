def sit_down(distance,max_distance):
    if distance < max_distance:
        print(f"Chair is too far away. I need to walk another {max_distance - distance} cm ")
    elif distance == max_distance:
        print(f"Distance from chair is satisfactorily enough. It's equal to {distance} cm . Starting to sit down")
    elif distance > max_distance:
        print(f"I walked too far. Chair is {distance - max_distance} cm behind")
distance_input= int(input("how many cm robot is moving to the chair?"))
max_distance_input = int(input("how far is chair from robot?"))
sit_down(distance_input,max_distance_input)