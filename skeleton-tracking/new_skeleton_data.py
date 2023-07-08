import cv2
import csv
import pandas as pd

# Frame number
filename = '20230405-000645.mp4'
csv_filename = 'points.csv'

protoFile = "pose_deploy_linevec_faster_4_stages.prototxt"
weightsFile = "model/pose_iter_160000.caffemodel"

nPoints = 15
POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]
x_coords = []
y_coords = []
waving_labels = []

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

source = cv2.VideoCapture(filename)

frame_counter = 0
waving = False

while (source.isOpened()):
    has_frame, frame = source.read()
    if not has_frame:
        break

    im = frame
    inWidth = im.shape[1]
    inHeight = im.shape[0]

    netInputSize = (368, 368)
    inpBlob = cv2.dnn.blobFromImage(im, 1.0 / 255, netInputSize, (0, 0, 0), swapRB=True, crop=False)
    net.setInput(inpBlob)

    # Forward Pass
    output = net.forward()

    scaleX = inWidth / output.shape[3]
    scaleY = inHeight / output.shape[2]

    # Empty list to store the detected keypoints
    points = []

    # Threshold
    threshold = 0.1

    for i in range(nPoints):
        probMap = output[0, i, :, :]
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)
        x = scaleX * point[0]
        y = scaleY * point[1]

        if prob > threshold:
            points.append((int(x), int(y)))
        else:
            points.append(None)

    imSkeleton = im.copy()

    # Draw skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]

        if points[partA] and points[partB]:
            x_coords.append(points[partA][0])
            y_coords.append(points[partA][1])

            x_coords.append(points[partB][0])
            y_coords.append(points[partB][1])

            waving_labels.append(waving)

    # Check if waving state should be toggled
    if frame_counter == 10:
        waving = True

    frame_counter += 1

df = pd.DataFrame({'x': x_coords, 'y': y_coords, 'waving': waving_labels})
df.to_csv(csv_filename, index=False)
print("CSV file written successfully")

source.release()
