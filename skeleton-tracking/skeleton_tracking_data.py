import cv2
import csv
import pandas as pd

filename = '20230405-000645.mp4'
csv_filename = 'points.csv'

protoFile = "pose_deploy_linevec_faster_4_stages.prototxt"
weightsFile = "model/pose_iter_160000.caffemodel"

nPoints = 15
POSE_PAIRS = [[0,1], [1,2], [2,3], [3,4], [1,5], [5,6], [6,7], [1,14], [14,8], [8,9], [9,10], [14,11], [11,12], [12,13] ]

df = pd.DataFrame(POSE_PAIRS, columns=['x', 'y'])

df.to_csv('pose_pairs.csv', index=False)
print("CSV file written successfully")

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

feature_params = dict( maxCorners = 500, qualityLevel = 0.2, minDistance = 15, blockSize = 9)

result = None

source = cv2.VideoCapture(filename)

frame_width = int(source.get(3))
frame_height = int(source.get(4))

if (source.isOpened()== False):
    print("Error opening video stream or file")

out_mp4 = cv2.VideoWriter(f'{filename[:-4]}-sk.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width,frame_height))

while (source.isOpened()):
    has_frame, frame = source.read()
    if not has_frame:
        break

    # im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    im = frame
    inWidth = im.shape[1]
    inHeight = im.shape[0]


    netInputSize = (368, 368)
    inpBlob = cv2.dnn.blobFromImage(im, 1.0 / 255, netInputSize, (0, 0, 0), swapRB=True, crop=False)
    net.setInput(inpBlob)


    # Forward Pass
    output = net.forward()


    # X and Y Scale
    scaleX = inWidth / output.shape[3]
    scaleY = inHeight / output.shape[2]



    # Empty list to store the detected keypoints
    points = []



    # Treshold 
    threshold = 0.1



    for i in range(nPoints):
        # Obtain probability map
        probMap = output[0, i, :, :]

        # Find global maxima of the probMap.
        minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

        # Scale the point to fit on the original image
        x = scaleX * point[0]
        y = scaleY * point[1]



        if prob > threshold :
            # Add the point to the list if the probability is greater than the threshold
            points.append((int(x), int(y)))
        else :
            points.append(None)



    imSkeleton = im.copy()



    # Draw skeleton
    for pair in POSE_PAIRS:
        partA = pair[0]
        partB = pair[1]


        if points[partA] and points[partB]:
            cv2.line(imSkeleton, points[partA], points[partB], (255, 255,0), 2)
            cv2.circle(imSkeleton, points[partA], 8, (255, 0, 0), thickness=-1, lineType=cv2.FILLED)




    result = imSkeleton



    out_mp4.write(result)



source.release()
out_mp4.release()