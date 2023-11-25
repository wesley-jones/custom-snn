# input_data.py

# Provide the neuron IDs that fire in each step

# Quick Sample Test
input_data_sample = [
    [1],
    [1],
    [1],
    [1],
]

input_data = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [1], #10
    [1],
    [1], #12
    [1],
    [1,4,], #14
    [1],
    [1], #16
    [1],
    [1],
    [1,4,], #19
    [1,4,],
    [1,4,],
    [1,4,],
    [1,4,],
    [1,4,],
    [1,4,],
    [1,4,9], #26
    [1,4,9],
    [1,4,9],
    [1,4,9],
    [1,4,9],
    [1,4,9],
    [1,4,9],
    [1,4,], #33
    [1,4,],
    [1,4,],
    [1,4,],
    [1,4,],
    [1,4,],
    [1], #39
    [1],
    [1],
    [1],
    [1],
    [1],
    [1], #45
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

def display_alert_dog():
    alert_dog = """
      / \\__
     (    @\\___
     /         O
    /   (_____/
    /_____/   U
    """
    print(alert_dog)

def display_running_dog():
    running_dog = """
        ____
     o-''|\\_____/)
      \\_/|_)     )
         \\  __  /
         (_/ (_/ 
    """
    print(running_dog)

neuron_actions = {
    25: display_alert_dog,
    26: display_alert_dog,
    27: display_alert_dog,
    28: display_alert_dog,
    29: display_alert_dog
}
