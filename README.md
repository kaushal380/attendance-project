# Attendance System

## Description

This project is an automated attendance system that uses facial recognition to mark attendance. The system captures photos, trains a facial recognition model, and then uses a webcam to recognize faces in real-time. Upon recognition, it records the attendance in a spreadsheet with a timestamp.

## Features

- Extracts photos for training directly from the `index.py` script.
- Uses OpenCV for webcam integration and face detection.
- Utilizes the `face-recognition` module to identify faces.
- Records attendance with a timestamp in a spreadsheet.

## Technologies Used

- Python
- OpenCV
- face-recognition
- numpy

## Installation Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kaushal380/attendance-project
   ```
   install dependencies
   ```bash
   pip install opencv-python face-recognition numpy
   ```

   run the main script
   ``` bash
   python main.py
   ```
## Usage Instructions

1. Place the photos to be used for training in the `photos` folder. These photos are extracted automatically by the `index.py` script.
2. Run the `main.py` script. It will open the webcam and start recognizing faces.
3. When a face is recognized based on the training data, the system records the name along with the current timestamp in a spreadsheet.
![image](https://github.com/user-attachments/assets/7a6844be-7b24-4f8f-8f94-61e431fcf15e)
![image](https://github.com/user-attachments/assets/28a7398b-05cd-4540-97ed-b205a307291a)


## Future Scope

- Enhance the system's ability to detect and recognize multiple people in a single frame.
- Improve the accuracy of face detection and recognition.
- Develop a graphical user interface (GUI) for easier interaction and management.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact [kaushal] at [kaushal.sambanna@gmail.com].


