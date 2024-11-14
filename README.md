# face-recognition-based-attendance-system

This project aims to automate the attendance process using facial recognition technology. It utilizes advanced machine learning techniques to accurately identify individuals and record their attendance in a seamless manner.

## Features

- **Real-Time Facial Recognition**: Uses OpenCV and pre-trained models to detect and recognize faces in real-time.
- **Attendance Logging**: Automatically marks attendance when a recognized face is detected.
- **Data Storage**: Saves the attendance records in a CSV file or database for easy retrieval.
- **User Management**: Allows adding, updating, and removing users from the system.
- **Simple Interface**: Easy-to-use system with a graphical interface for interacting with the application.

## Technologies Used

- **Python**: Main programming language used for developing the system.
- **OpenCV**: For image processing and face recognition tasks.
- **Haar Cascades**: Pre-trained classifiers for detecting faces.
- **Face Recognition Libraries**: For comparing and recognizing faces.
- **Tkinter**: For building a graphical user interface (GUI).
- **Pandas/CSV**: For managing and storing attendance records.

## Installation

### Prerequisites

- Python 3.x
- OpenCV
- NumPy
- pandas
- face_recognition

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/barna0678/face-recognition-based-attendance-system.git
   cd face-recognition-based-attendance-system

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt

3. Ensure you have a working webcam for face detection.
4. Run the system:
    ```bash
   python main.py


## Usage

1. **Add New User**: Capture a new user's face by following the prompts.
2. **Start Attendance**: Once a user is added, you can start the attendance system. The webcam will start, and it will recognize faces.
3. **View Attendance**: The attendance record can be viewed from the stored file (CSV).

## File Structure

- **main.py**: The entry point for running the system. It manages user interactions and coordinates other modules.
- **face_recognition.py**: Contains the face recognition logic to detect and match faces with registered users.
- **attendance.csv**: A CSV file that stores attendance records, including user IDs and timestamps.
- **requirements.txt**: A list of Python packages required to run the project. Example: `opencv-python`, `face_recognition`.
- **images/**: A directory where images of registered users are stored for face recognition purposes.
- **README.md**: Documentation providing an overview of the project, setup instructions, and usage details.


## Contributing

Feel free to fork this project and make contributions. If you find any bugs or have feature requests, open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

