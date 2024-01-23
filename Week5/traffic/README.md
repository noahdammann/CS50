## About The Project

  - Trains an AI to identify which traffic sign appears in a photograph
  - Creates a convolutional neural network with multiple layers using TensorFlow
  - The neural network contains multiple convolutional and max-pooling layers
  - Achieved the best results for convolution by using 64 filters and a 2x2 kernel
  - Compared to 32 filters and a 3x3 kernel, it takes the model longer to train but is ultimately more accurate and less prone to over-fitting
  - The nerual network contains dropout to prevent overfitting
  
## Prerequisites

  - Python 3 - [Download & Install Python 3](https://www.python.org/downloads/)

## Installation

1. Clone the repo
   ```sh
    git clone https://github.com/noahdammann/CS50 -b CS50AI
   ```
2. Move into traffic
   ```sh
    cd CS50/Week5/traffic
   ```
3. Install requirements
  ```sh
    pip3 install -r requirements.txt
  ```
4. Unzip data set
   ```
     unzip gtsrb.zip
   ```
   
## Usage

```
  python traffic.py gtsrb
```

