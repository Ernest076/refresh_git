from pysimverse import Drone
import cv2

# connect drone
drone = Drone()

drone.connect()

# start camera stream
drone.streamon()

while True:

    # get frame
    frame = drone.get_frame()

    # show camera feed
    cv2.imshow("Drone Camera", frame)

    key = cv2.waitKey(1)

    # press q to close camera
    if key == ord('q'):
        break

cv2.destroyAllWindows()