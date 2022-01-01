class PerceptronNetwork:
    def __init__(self, input_count, learning_rate, threshold):
        self.w = [0] * input_count
        self.bias = 0
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.input_count = input_count

    def train(self, x: list, bias, target):
        net_input = self.calculate_net_input(x)
        result = self.activation_function(net_input)

        if result != target:
            self.bias += self.learning_rate * bias * target
            for i in range(self.input_count):
                self.w[i] += self.learning_rate * x[i] * target


    def weights_changed(self, old_weights, old_bias):
        if self.bias != old_bias:
            return True
        for i in range(self.input_count):
            if self.w[i] != old_weights[i]:
                return True
        return False

    def calculate_net_input(self, x: list[int]):
        net_input = self.bias
        for i in range(self.input_count):
            net_input += (x[i] * self.w[i])
        
        return net_input

    def activation_function(self, net_input):
        if net_input > self.threshold:
            return 1
        if net_input < -self.threshold:
            return -1
        return 0
