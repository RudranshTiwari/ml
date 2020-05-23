# written by rudransh tiwari , 22-apr-2020
# Sample program that runs on TF2.0
# I had to downgrade to TF2.0.1 from TF2.1.0 source -- https://github.com/tensorflow/tensorflow/issues/35749
# import numpy as np
# import tensorflow as tf
# from tensorflow import keras

# # print(tf.__version__)
# # msg = tf.constant('Hello, TensorFlow!')
# # tf.print(msg)

# # a = tf.Variable(2,)
# # b = tf.Variable(34,)
# # x = tf.math.add(a,b)

# # s = a + b
# # print(s.numpy())
# model = keras.Sequential([keras.layers.Dense(units= 1, input_shape=[1])])
# model.compile(optimizer= "sgd", loss = 'mean_squared_error')

# import tensorflow as tf
# import numpy as np
# from tensorflow import keras
# def house_model(y_new):
#     xs = np.array([1,2,3,4], dtype = float)
#     ys = np.array([100,150,200,250], dtype = float)
#     model = model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
#     model.compile(optimizer='sgd', loss='mean_squared_error')
#     model.fit(xs,ys,epochs = 100)
#     return model.predict(y_new)[0]
# prediction = house_model([7])
# print(prediction)
  

# model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# model.compile(optimizer='sgd', loss='mean_squared_error')
# # xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
# # ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)
# # model.fit(xs, ys, epochs=70)
# # print(model.predict([10.0]))
import tensorflow as tf

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('accuracy')>0.6):
      print("\nReached 60% accuracy so cancelling training!")
      self.model.stop_training = True

mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

callbacks = myCallback()

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer=tf.optimizers.Adam(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, callbacks=[callbacks])