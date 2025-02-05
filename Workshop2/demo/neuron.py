"""A model for neurons in neural networks for
the Robotics @ Berkeley neural network workshop."""

__author__ = "Phillip Kuznetsov"

import sigmoid


class Neuron:
    """ Represents the neuron object in the network graph """

    def __init__(self, sigmoid=sigmoid.Logistic):
        """ Initializes the neuron and sets
         sigmoid to the Logistic function """
        self.net = 0
        self.output = 0
        self.sigmoid = sigmoid
        self.anteriors = []
        self.posteriors = []
        self.gradient_net = 0
        self.error = 0

    def feed(self, input_partial):
        """ Passes in numerical input to sum up
         in the neuron"s activation net."""
         

    def activate(self):
        """ Applies the sigmoid function to the neuron"s net, generating the
        neuron output, then resets the net. """
        self.gradient_net = self.sigmoid.derivative(self.net)


    def set_error(self, error_coef):
        """Updates the error coefficent for the neuron."""
        set.error = error_coef * self.gradient_net
