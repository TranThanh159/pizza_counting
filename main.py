import cv2
import numpy as np

from ultralytics import solutions

VIDEO_PATH = [
    "./videos/1461_CH01_20250607193711_203711.mp4", # 0
    "./videos/1462_CH03_20250607192844_202844.mp4", # 1
    "./videos/1462_CH04_20250607210159_211703.mp4", # 2
    "./videos/1464_CH02_20250607180000_190000.mp4", # 3
    "./videos/1465_CH02_20250607170555_172408.mp4", # 4
    "./videos/1467_CH04_20250607180000_190000.mp4", # 5
]

# region_points = [(20, 400), (1080, 400)]                                      # line counting
# region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360)]  # rectangle region

# region to count number of pizza in the video
REGION_POINTS = [
    np.array([[598, 134], [1369, 76], [1473, 276], [540, 334]]),                                
    np.array([[423, 393], [854, 346], [1284, 867], [453, 925]]),
    np.array([[929, 515], [226, 922], [438, 1070], [1014, 1064], [1249, 727], [941, 515]]),
    np.array([[1206, 599], [1598, 710], [1453, 1070], [909, 1073]]),
    np.array([[653, 648], [162, 619], [60, 1067], [604, 1064]]),
    np.array([[1331, 410], [1630, 494], [1319, 1047], [848, 1012]]),
]
# region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360), (20, 400)]   # polygon region



def count_pizza(video_path, region_points, output_file_name="./output/output.avi"):
    cap = cv2.VideoCapture(video_path)
    assert cap.isOpened(), "Error reading video file"

    # Video writer
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    video_writer = cv2.VideoWriter(output_file_name, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    # Initialize object counter object
    counter = solutions.ObjectCounter(
        show=True,  # display the output
        region=region_points,  # pass region points
        model="yolo11n.pt",  # model="yolo11n-obb.pt" for object counting with OBB model.
        classes=[53],  # count specific classes i.e. person and car with COCO pretrained model. Class 53 is pizza
        # tracker="botsort.yaml",  # choose trackers i.e "bytetrack.yaml"
    )

    # Process video
    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            print("Video frame is empty or processing is complete.")
            break

        results = counter(im0)
        # print(results)  # access the output
        video_writer.write(results.plot_im)  # write the processed frame.

    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()  # destroy all opened windows


# run model
for index in range(6):
    # index = 2 # index is from 0-5
    output_file_name = "./output/" + VIDEO_PATH[index][9:-4] + ".avi"
    count_pizza(VIDEO_PATH[index], REGION_POINTS[index], output_file_name=output_file_name)
    print("Run sucessfully in " + VIDEO_PATH[index])