class TwoInputPerceptron:
    def __init__(self, learning_rate: float = 0.3, threshold: float = 1):
        self.w1 = 0
        self.w2 = 0
        self.bias = 0
        self.learning_rate = learning_rate
        self.threshold = threshold

    def train(self, x1, x2, bias, target):
        net_input = self.calculate_net_input(x1, x2)
        result = self.activation_function(net_input)
        if (result != target):
            self.w1 += self.learning_rate * x1 * target
            self.w2 += self.learning_rate * x2 * target
            self.bias += self.learning_rate * bias * target

    def calculate_net_input(self, x1, x2):
        net_input = self.bias + (x1 * self.w1 + x2 * self.w2)
        return net_input

    def activation_function(self, net_input):
        if net_input > self.threshold:
            return 1
        if net_input < -self.threshold:
            return -1
        return 0
