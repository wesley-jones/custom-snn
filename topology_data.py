# topology_data.py

topology_data = {
    "neurons": [
        {
            "neuron_id": 1,
            "upstream_neurons": [
                {"id": 2, "weight": 0.2},
                {"id": 3, "weight": 0.3}
            ]
        },
        {
            "neuron_id": 2,
            "upstream_neurons": [
                {"id": 3, "weight": 0.1}
            ]
        },
        {
            "neuron_id": 3,
            "upstream_neurons": [
                {"id": 4, "weight": 0.4}
            ]
        },
        {
            "neuron_id": 4,
            "upstream_neurons": [
                {"id": 5, "weight": 0.2}
            ]
        },
        {
            "neuron_id": 5,
            "upstream_neurons": [
                {"id": 2, "weight": 0.3}
            ]
        }
    ]
}
