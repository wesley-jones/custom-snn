from topology_data import topology_data
from input_data import input_data

class Neuron:
    spike_threshold = 0.5  # Universal spike threshold

    def __init__(self, neuron_id):
        self.neuron_id = neuron_id
        self.fired_time_step = None
        self.upstream_neurons = []

    def add_upstream_neuron(self, upstream_neuron_id, weight):
        self.upstream_neurons.append({"id": upstream_neuron_id, "weight": weight})

    def get_fired_upstream_neurons(self, current_time_step):
        fired_neurons = []
        for upstream_neuron_info in self.upstream_neurons:
            upstream_neuron = neuron_lookup[upstream_neuron_info["id"]]
            if upstream_neuron.fired_time_step == current_time_step - 1:
                fired_neurons.append(upstream_neuron_info)
        return fired_neurons

    def update(self, current_time_step):
        # Neuron hasn't fired yet
        fired_neurons = self.get_fired_upstream_neurons(current_time_step)
        total_weighted_input = sum(upstream_neuron_info["weight"] for upstream_neuron_info in fired_neurons)
        if total_weighted_input >= Neuron.spike_threshold:
            self.fired_time_step = current_time_step
            for upstream_neuron_info in self.upstream_neurons:
                weight_delta = 0.1  # Adjust as needed
                upstream_neuron_info["weight"] += weight_delta

# Create neurons and build the neuron lookup
neuron_lookup = {}
neurons = []

for neuron_info in topology_data["neurons"]:
    neuron_id = neuron_info["neuron_id"]
    neuron = Neuron(neuron_id)
    for upstream_info in neuron_info["upstream_neurons"]:
        neuron.add_upstream_neuron(upstream_info["id"], upstream_info["weight"])
    neuron_lookup[neuron_id] = neuron
    neurons.append(neuron)

# Simulate time
for time_step, input_spike_targets in enumerate(input_data):
    print(f"Time Step {time_step}")
    print("------------")
    for neuron in neurons:
        print(f"Neuron {neuron.neuron_id}")
        print(f"   Old upstream neuron weights: {[upstream_neuron_info for upstream_neuron_info in neuron.upstream_neurons]}")
        print(f"   Old fired_time_step: {neuron.fired_time_step}")
        neuron.update(time_step)  # Update all neurons before processing new input data
        print(f"   New fired_time_step: {neuron.fired_time_step}")
        print(f"   New upstream neurons: {[upstream_neuron_info for upstream_neuron_info in neuron.upstream_neurons]}")
        print()

    # Process the input data
    for i, input_spike in enumerate(input_spike_targets):
        if input_spike:
            neurons[i].fired_time_step = time_step  # Set the fired_time_step for targeted neurons
    
    
