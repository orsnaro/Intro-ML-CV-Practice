import numpy as np
from tensorflow.keras.datasets import cifar10
import matplotlib.pyplot as plt

# Load CIFAR-10 dataset
(train_images, train_labels), (_, _) = cifar10.load_data()

# Define the number of samples to select
num_samples = 25

# Get random indices for the samples
random_indices = np.random.choice(len(train_images), num_samples, replace=False)

# Select images and labels based on the random indices
sampled_images = train_images[random_indices]
sampled_labels = train_labels[random_indices]

# Define the labels in CIFAR-10 dataset
cifar_labels = {
    0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer',
    5: 'dog', 6: 'frog', 7: 'horse', 8: 'ship', 9: 'truck'
}

# Visualize the sampled images with their labels
plt.figure(figsize=(15, 10))
for i in range(num_samples):
    plt.subplot(5, 5, i+1)
    plt.imshow(sampled_images[i])
    plt.title(f"Label: {cifar_labels[sampled_labels[i][0]]}")
    plt.axis('off')

print(random_indices)
plt.tight_layout()
plt.show()
