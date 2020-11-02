import streamlit as st
import numpy as np
import cv2

class BoundingBox():

    def __init__(self, image: np.ndarray, bboxes: np.ndarray):
        """[summary]

        Args:
            image (np.ndarray): shape(height, width, channels)
            bboxes (np.ndarray): shape(n_heads, num_objects, 5)
        """
        
        # [] slider
        st.markdown('### Top-attended bounding boxes')
        st.markdown(
            'To answer the question, the system pays more attention to some regions of the image\
            than others. The boxes here depict those regions.\n\n'
            'The green boxes denote the regions with > 10% attention, blue boxes\
            with attention score between 5% to 10% and the red boxes with less than 5%.'
        )

        self.image = np.copy(image)
        self.bboxes = bboxes

        self.show_all = st.checkbox(
            label='Show/Hide all objects', value=True, key='show_all'
        )
        self.confidence_th = st.slider(
            label='Only objects with >= than this threshold will be shown', 
            min_value=0.0, max_value=1.0, value=0.07, step=0.01
        )

        self.colors = {
            "max": [0, 255, 0],
            "mid": [0, 0, 170],
            "min": [100, 0, 0]
        }

        self.plot_boxes()

    
    def plot_boxes(self):

        image_with_boxes = self.image.astype(np.float64)
        
        height, width, channels = image_with_boxes.shape

        if self.show_all:

            for (xmin, ymin, xmax, ymax, confidence) in self.bboxes:

                if (confidence >= self.confidence_th):

                    if (confidence <= 0.05):
                        cat = "min"
                    elif (0.05 < confidence <= 0.1):
                        cat = "mid"
                    else:
                        cat = "max"

                    image_with_boxes[int(ymin*height):int(ymax*height),int(xmin*width):int(xmax*width),:] += self.colors[cat]
                    image_with_boxes[int(ymin*height):int(ymax*height),int(xmin*width):int(xmax*width),:] /= 2
                    cv2.putText(
                        img=image_with_boxes, text=f'{confidence*100:.2f}%', org=(int(xmin*width),int(ymin*height)), color=(0,0,0),
                        fontFace=0, fontScale=0.8, thickness=2
                    )
                

        st.image(
            image_with_boxes.astype(np.uint8), use_column_width=True,
            caption='Image with bounding boxes (Green > 10%, 5% < blue < 10%, red < 5%)'
        )
            
        




