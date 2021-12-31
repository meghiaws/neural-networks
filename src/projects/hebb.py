class TwoInputHebbNetwork:
    def __init__(self):
        self.w1 = 0
        self.w2 = 0
        self.bias = 0

    def train(self, x1, x2, bias, target):
        self.w1 += x1 * target
        self.w2 += x2 * target
        self.bias += bias * target

    def calculate_net_input(self, x1, x2):
        net_input = self.bias + (x1 * self.w1 + x2 * self.w2)
        return net_input

    def activation_function(self, net_input):
        if net_input >= 0:
            return 1
        return -1


class HebbNetwork:
    def __init__(self, input_count):
        self.w = [0] * input_count
        self.bias = 0
        self.input_count = input_count

    def train(self, x: list[int], target: int, bias: int = 1):

        for i in range(self.input_count):
            self.w[i] += x[i] * target

        self.bias += bias * target

    def calculate_net_input(self, x: list[int]):
        net_input = self.bias
        for i in range(self.input_count):
            net_input += (x[i] * self.w[i])
        
        return net_input

    def activation_function(self, net_input):
        if net_input >= 0:
            return 1
        return -1
