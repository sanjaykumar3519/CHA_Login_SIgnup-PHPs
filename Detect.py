import cv2
import numpy as np
import os
import os.path
import sys
import time
#clip for 10 sec
t = 10
startTime = time.time();

# Load Yolo
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
#colors = np.random.uniform(0, 255, size=(len(classes), 3))
#'D:/Datasets/'+
# Loading image
cctv=""
for a in sys.argv[1:]:
    cctv = a
path =cctv
cap = cv2.VideoCapture(path)
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))

snap = 0
ret, frame1 = cap.read()
ret, frame2 = cap.read()
while cap.isOpened():
    if ret==False:
        break
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:
            continue
        #cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 0, 255), 3)
        snap = snap + 1
        if(snap==100):
            cv2.imwrite("000.jpeg",frame1)
            cap.release()
            cv2.destroyAllWindows()
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    #image = cv2.resize(frame1, (1280,720))
    #out.write(image)
    #cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    if(time.time() - startTime < t):
        cap.release()
        cv2.destroyAllWindows()
    #if cv2.waitKey(40) == 27:
        #break

if(os.path.isfile("000.jpeg")):

    img = cv2.imread("000.jpeg")
    img = cv2.resize(img, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)


    count = 0
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    #print(indexes)
    #font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            #x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            #color = colors[class_ids[i]]
            #cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            #cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
            if(label=="person"):
                count = count + 1;

    print(count)
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
else:
    print("none")