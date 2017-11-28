import os
import cv2
import time
import argparse
import multiprocessing
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import json

from flask import Flask, request, render_template, jsonify
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util
from tensorflow.python.platform import gfile


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

CWD_PATH = os.getcwd()

# Path to frozen detection graph. This is the actual model that is used for the object detection.
MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
PB_NAME = 'frozen_inference_graph.pb'
PB_TEXT = 'mscoco_label_map.pbtxt'
PATH_TO_CKPT = os.path.join(CWD_PATH, 'object_detection', MODEL_NAME, PB_NAME)
# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join(CWD_PATH, 'object_detection', 'data', PB_TEXT)

NUM_CLASSES = 100

# Loading label map
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)

def detect_objects(image_np, sess, detection_graph):
    image_np_expanded = np.expand_dims(image_np, axis=0)
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
    boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
    scores = detection_graph.get_tensor_by_name('detection_scores:0')
    classes = detection_graph.get_tensor_by_name('detection_classes:0')
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')
    (boxes, scores, classes, num_detections) = sess.run(
        [boxes, scores, classes, num_detections],
        feed_dict={image_tensor: image_np_expanded})
    # Visualization of the results of a detection.
    # vis_util.visualize_boxes_and_labels_on_image_array(
    #     image_np,
    #     np.squeeze(boxes),
    #     np.squeeze(classes).astype(np.int32),
    #     np.squeeze(scores),
    #     category_index,
    #     use_normalized_coordinates=True,
    #     line_thickness=8)
    return image_np, np.squeeze(boxes), np.squeeze(classes).astype(np.int32), np.squeeze(scores), category_index

def format_data(boxes, classes, scores, category_index, max_boxes_to_draw = 20, min_score_thresh = 0.5):
  result = []
  for i in range(min(max_boxes_to_draw, boxes.shape[0])):
    if scores is None or scores[i] > min_score_thresh:
      if classes[i] in category_index.keys():
        class_name = category_index[classes[i]]['name']
      else:
        class_name = 'N/A'
      pred = {'name': class_name, 'score': round(scores[i], 4)}
      result.append(pred)
  return result

@app.route('/api/detect', methods=['POST'])
def detect():
    base64_image = request.form['image']
    encoded_data = base64_image.split(',')[1]
    nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess = tf.Session(graph=detection_graph)
        # frame_rgb = cv2.imread(os.path.expanduser('/Users/zhengguorong/Desktop/IMG_3367.JPG'))
        frame_rgb = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # frame_rgb = cv2.cvtColor(frame_rgb, cv2.COLOR_BGR2RGB)
        image, boxes, classes, scores, category_index = detect_objects(frame_rgb, sess, detection_graph)
        response = format_data(boxes, classes, scores, category_index)
        return jsonify(response)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)