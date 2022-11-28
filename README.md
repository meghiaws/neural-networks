# Neural Networks

An Implementation of some neural networks like Hebb, Perceptron and Adaline Neural Networks along with simple character recognition example using these networks to solve solve in Python and Jupyter.

## Installation

1. Clone the project:

    ```bash
    git clone https://github.com/meghiaws/neural-networks
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv && venv\Scripts\activate
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt && pip install --editable .
    ```

    **`pip install --editable .`** is just for installing local package called **``projects``**, which is simply wrapper for our source codes to be accessible from jupyter notebooks.

4. Install jupyter kernel for the virtual environment

    ```bash
    ipython kernel install --user --name=venv
    ```

5. Select the installed kernel when you want to use jupyter notebook in this virtual environment:

![alt text](https://media.geeksforgeeks.org/wp-content/uploads/20210827225550/Screenshot20210827225304.jpg)
