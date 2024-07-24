from ultralytics import YOLO

def run():
    # Use this code to detecte keypoints in your image.
    model = YOLO(r"path_to_model") 
    # Image will be saved.
    model.predict(r"path_to_image",save=True)
    
if __name__ == "__main__":
    run()
