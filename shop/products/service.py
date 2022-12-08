import matplotlib.pyplot as plt
from tensorflow import keras
import tensorflow as tf


class MyFashion:

    def exec(self):
        (train_input, train_target), (train_input, train_target) = keras.datasets.fashion_mnist.load_data()
        fig, axs = plt.subplots(1, 10, figsize=(10,10))
        for i in range(10):
            axs[i].imshow(train_input[i], cmap ='gray_r')
            axs[i].axis('off')
        plt.show()


if __name__ == '__main__':
    m = MyFashion()
    m.exec()
