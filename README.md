# Perceptron Neural Network

An Implementation of Perceptron Neural Network in Python and Jupyter

## Installation

1. Clone the project:

    ```bash
    git clone https://github.com/meghiaws/perceptron
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv && venv\Scripts\activate
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt && pip install --editable .
    ```

    **`pip install --editable .`** is just for installing local package called **``network``**, which is simply wrapper for our source codes to be accessible from jupyter notebooks

4. Install jupyter kernel for the virtual environment

    ```bash
    ipython kernel install --user --name=venv
    ```
