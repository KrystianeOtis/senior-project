import cv2
import keras
import pandas as pd
import tensorflow as tf
import numpy as np
# Load the model using OpenCV

column_names = [
  'index',
  'x_left_wrist',
  'y_left_wrist',
  'x_left_elbow',
  'y_left_elbow',
  'x_left_shoulder',
  'y_left_shoulder',
  'x_right_wrist',
  'y_right_wrist',
  'x_right_elbow',
  'y_right_elbow',
  'x_right_shoulder',
  'y_right_shoulder',
  'waving'
]

loaded_model = keras.models.load_model('C:/Users/mosia/OneDrive/Desktop/Senior Project/senior-project/assets/mymodel.h5')
d = pd.DataFrame(0.0, index=np.arange(10), columns=column_names)

def create_dataset(X, step=10):
    Xs = []
    max_length = 0  # Track the maximum sequence length

    for i in range(0, len(X), step):
        v = X.iloc[i:(i + step)].values
        Xs.append(v)
        max_length = max(max_length, len(v))

    # Pad sequences to have the same length
    Xs_padded = []
    for sequence in Xs:
        if len(sequence) < max_length:
            padded_sequence = np.pad(sequence, ((0, max_length - len(sequence)), (0, 0)), mode='constant')
        else:
            padded_sequence = sequence
        Xs_padded.append(padded_sequence)

    return np.array(Xs_padded)


X = create_dataset(
    d[['x_left_wrist', 'y_left_wrist', 'x_left_elbow', 'y_left_elbow',
              'x_left_shoulder', 'y_left_shoulder', 'x_right_wrist',
              'y_right_wrist', 'x_right_elbow', 'y_right_elbow',
              'x_right_shoulder', 'y_right_shoulder']]
)


print(X)

print(loaded_model(X))
