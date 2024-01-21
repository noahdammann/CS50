## Traffic sign recognizing AI

The two functions I implemented are 'load_data' and 'get_model.'

#### Load data

For the first time I needed to access files and use Pythons 'os' module, but it wasn't long until I figured out how it worked. I then need to read and resize the image files into numpy arrays, which I did using the cv2 (open cv) module. I was able to do so by making use of the 'imread' and 'resize' functions, which I discovered in their documentation.

#### Get model

The 'get_model' function creates a compiled convolutional neural network model using TensorFlow. I added multiple convolutional and max-pooling layers, which made the model more accurate with each repeat. Then to make the model more robust I added in some dropout to prevent overfitting. I assigned 43 output nodes to the neural network to correlate with the 43 categories of road signs in our database. 

#### Playing around with different numbers

I found the best results for convolution by using 64 filters and a 2x2 kernel. Compared to 32 filters and a 3x3 kernel, it takes the model longer to train but is ultimately more accurate and less prone to over-fitting.