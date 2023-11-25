# topology_data.py


# Quick Sample Topolgoy
topology_data_sample = [

    ### Input Layer ###
    {
        # input neuron
        "neuron_id": 1,
        "upstream_neurons": []
    },
    {
        "neuron_id": 2,
        "upstream_neurons": [
            {"id": 1, "weight": 1},
        ]
    },
    {
        # input neuron
        "neuron_id": 3,
        "upstream_neurons": [
            {"id": 2, "weight": 1},
        ]
    },
    {
        # output neuron
        "neuron_id": 4,
        "upstream_neurons": [
            {"id": 3, "weight": 1},
        ]
    },
]

topology_data = [

    ### Input Layer ###
    {
        # input neuron
        "neuron_id": 1,
        "upstream_neurons": []
    },
    {
        # input neuron
        "neuron_id": 2,
        "upstream_neurons": []
    },
    {
        # input neuron
        "neuron_id": 3,
        "upstream_neurons": []
    },
    {
        # input neuron
        "neuron_id": 4,
        "upstream_neurons": []
    },
    {
        # input neuron
        "neuron_id": 5,
        "upstream_neurons": []
    },
    {
        # input neuron
        "neuron_id": 6,
        "upstream_neurons": []
    },
    {
        # input neuron
        "neuron_id": 7,
        "upstream_neurons": []
    },
    {
        # input neuron
        "neuron_id": 8,
        "upstream_neurons": []
    },
    {
        # input neuron
        "neuron_id": 9,
        "upstream_neurons": []
    },
    {
        # input neuron
        "neuron_id": 10,
        "upstream_neurons": []
    },
    {
        # input neuron
        "neuron_id": 11,
        "upstream_neurons": []
    },
    {
        # input neuron
        "neuron_id": 12,
        "upstream_neurons": []
    },



    ### Layer 1 ###
    {
        # Neuron 1 Layer 1
        "neuron_id": 13,
        "upstream_neurons": [
            {"id": 5, "weight": 1},
            {"id": 7, "weight": 1},
            {"id": 11, "weight": 1}
        ]
    },
    {
        # Neuron 2 layer 1
        "neuron_id": 14,
        "upstream_neurons": [
            {"id": 2, "weight": 1},
            {"id": 6, "weight": 1},
            {"id": 10, "weight": 1}
        ]
    },
    {
        # Neuron 3 layer 1
        "neuron_id": 15,
        "upstream_neurons": [
            {"id": 1, "weight": 1},
            {"id": 4, "weight": 1},
            {"id": 9, "weight": 1}
        ]
    },
    {
        # Neuron 4 layer 1
        "neuron_id": 16,
        "upstream_neurons": [
            {"id": 3, "weight": 1},
            {"id": 8, "weight": 1},
            {"id": 12, "weight": 1}
        ]
    },


    ### Layer 2 ###
    {
        # Neuron 1 layer 2
        "neuron_id": 17,
        "upstream_neurons": [
            {"id": 14, "weight": 1},
            {"id": 15, "weight": 1},
            {"id": 13, "weight": 1}
        ]
    },
    {
        # Neuron 2 layer 2
        "neuron_id": 18,
        "upstream_neurons": [
            {"id": 14, "weight": 1},
            {"id": 15, "weight": 1},
            {"id": 16, "weight": 1}
        ]
    },
    {
        # Neuron 3 layer 2
        "neuron_id": 19,
        "upstream_neurons": [
            {"id": 13, "weight": 1},
            {"id": 15, "weight": 1},
            {"id": 16, "weight": 1}
        ]
    },
    {
        # Neuron 4 layer 2
        "neuron_id": 20,
        "upstream_neurons": [
            {"id": 13, "weight": 1},
            {"id": 14, "weight": 1},
            {"id": 15, "weight": 1}
        ]
    },
    {
        # Neuron 5 layer 2
        "neuron_id": 21,
        "upstream_neurons": [
            {"id": 13, "weight": 1},
            {"id": 14, "weight": 1},
            {"id": 16, "weight": 1}
        ]
    },
    {
        # Neuron 6 layer 2
        "neuron_id": 22,
        "upstream_neurons": [
            {"id": 14, "weight": 1},
            {"id": 15, "weight": 1},
            {"id": 16, "weight": 1}
        ]
    },
    {
        # Neuron 7 layer 2
        "neuron_id": 23,
        "upstream_neurons": [
            {"id": 13, "weight": 1},
            {"id": 15, "weight": 1},
            {"id": 16, "weight": 1}
        ]
    },
    {
        # Neuron 8 layer 2
        "neuron_id": 24,
        "upstream_neurons": [
            {"id": 13, "weight": 1},
            {"id": 14, "weight": 1},
            {"id": 15, "weight": 1}
        ]
    },


    ### Output Layer ###
    {
        # Neuron 1 Output Layer
        "neuron_id": 25,
        "upstream_neurons": [
            {"id": 17, "weight": 1},
            {"id": 18, "weight": 1},
            {"id": 19, "weight": 1},
        ]
    },
    {
        # Neuron 2 Output Layer
        "neuron_id": 26,
        "upstream_neurons": [
            {"id": 19, "weight": 1},
            {"id": 20, "weight": 1},
        ]
    },
    {
        # Neuron 3 Output Layer
        "neuron_id": 27,
        "upstream_neurons": [
            {"id": 20, "weight": 1},
            {"id": 21, "weight": 1},
        ]
    },
    {
        # Neuron 4 Output Layer
        "neuron_id": 28,
        "upstream_neurons": [
            {"id": 21, "weight": 1},
            {"id": 22, "weight": 1},
            {"id": 23, "weight": 1},
        ]
    },
    {
        # Neuron 5 Output Layer
        "neuron_id": 29,
        "upstream_neurons": [
            {"id": 22, "weight": 1},
            {"id": 23, "weight": 1},
            {"id": 24, "weight": 1},
        ]
    },
]

