"""
Module that contains functions to perform Entropy Analysi of the data.
For a more specific explaination please refer to the relative notebook.
"""

def calculate_entropy(transition_matrix):
    # Initialize entropy
    entropy = {}

    # Calculate entropy for each source article
    for source in transition_matrix.index:
        # Get the probabilities for transitions from this source
        probabilities = transition_matrix.loc[source]

        # Calculate entropy, treating zero probabilities as contributing zero
        entropy_value = 0
        for p in probabilities:
            if p > 0:  # Only calculate for non-zero probabilities
                entropy_value -= p * np.log2(p)  # Use log2 for bits

        # Store the entropy value for the source article
        entropy[source] = entropy_value

    return entropy