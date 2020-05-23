# import tensorflow as tf
# import numpy as np
# from tensorflow import keras

# # GRADED FUNCTION: house_model
# def house_model(y_new):
#     xs = np.array([1,2,3,4], dtype = float)
#     ys = np.array([100,150,200,250], dtype = float)
#     model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
#     model.compile(optimizer='sgd', loss='mean_squared_error')
#     model.fit(xs,ys,epochs = 500)
#     return model.predict(y_new)[0]

# prediction = house_model([7])
# print(prediction)    
import tensorflow as tf

mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(linewidth=200)
import matplotlib.pyplot as plt
plt.imshow(training_images[0])
print(training_labels[0])
print(training_images[0])
training_images  = training_images / 255.0
test_images = test_images / 255.0
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), 
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])
model.compile(optimizer = tf.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)
model.evaluate(test_images, test_labels)
classifications = model.predict(test_images)

print(classifications[0])
print(test_labels[0])                                    