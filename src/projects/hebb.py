
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
