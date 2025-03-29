import cv2
import face_recognition
import numpy as np

def detect_faces(image_path: str):
    image = face_recognition.load_image_file(image_path)
    face_locations = face_recognition.face_locations(image)
    return face_locations

def recognize_faces(known_faces, known_names, unknown_image_path):
    unknown_image = face_recognition.load_image_file(unknown_image_path)
    unknown_encodings = face_recognition.face_encodings(unknown_image)

    for encoding in unknown_encodings:
        matches = face_recognition.compare_faces(known_faces, encoding)
        if True in matches:
            index = matches.index(True)
            return known_names[index]
    return None
