

# Nirbhay Naari - An Artificial Intelligence Tool for Detection of Crime Against Women

Nirbhay Naari is a comprehensive AI tool designed to detect and address crimes against women through a secure portal. The tool integrates multi-label story classification, audio-video violence detection, and help signal recognition to enhance women's safety and provide timely assistance.

## Project Link

[Project Link](#)

## Research Paper

Find our research paper published in Springer Lecture Notes in Electrical Engineering [here](#).

## Overview

The Nirbhay Naari project aims to develop a reliable, robust, and accurate model for detecting potential violent acts against women. The system is composed of two main components:

1. **Real-time Crime Against Women Detection**
2. **Violence/Harassment Story Summarization Module**

## Methodology

### 5.1 Methodology Employed for Development

**Data Preprocessing:**
- Web scraping was used to collect over 100 video categories, split into violent and non-violent scenes.
- Data augmentation involved models such as Adversarial Training and Generative Adversarial Networks (GANs).
- Tools: Keras ImageDataGenerator, Skimage, OpenCV.

**Data Modeling:**
- **Violence/Crime Scene Detection:** Utilized CNN and LSTM models for frame classification and spectrogram/audio-to-text conversion.
- **Audio Classification:** Employed SVM and Random Forest algorithms.
- **Help Hand Signal Detection:** Used datasets from Kaggle and NUS for ASL alphabet and hand posture recognition.
- **Multi-label Story Classification:** Collected posts from Facebook using the Graph API, classified into categories such as sexual violence, domestic violence, psychological violence, and fatalities.

### 5.2 Algorithms and Flowcharts for Modules

**Algorithms:**
- **CNN:** Used for video classification with feature extraction and prediction layers.
- **LSTM/GRU:** Applied for handling long-term dependencies in sequence data.
- **SVM:** Implemented for hyperplane classification in audio data.
- **Random Forest:** Utilized for ensemble decision-making in audio classification.

**Flowcharts:**
- Block diagram and modular diagram of the project:
  ![Block Diagram](https://github.com/user-attachments/assets/e6932ec8-58d6-4a9b-af60-35a305ba96dc)
  ![Modular Diagram](https://github.com/user-attachments/assets/98dd4c2b-6b1f-4ec7-b897-5f8b31a3afbd)

### 5.3 Dataset Source and Utilization

**Audio Detection of Harassment:**
- Audio data sourced from [Free Sound Effects](https://www.freesoundeffects.com/) and [Zenodo](https://zenodo.org/record/1188976).
- Data extracted from Twitter and Facebook using Tweepy and facebook-scraper.

**Violence/Crime Scene Detection Module:**
- Created a custom YouTube video dataset. [Access here](https://drive.google.com/drive/folders/1LJLhCdwJkzx8oC_ns4sDWUCRcP6YBLoD?usp=sharing).

**Help Hand Signal Detection:**
- Utilized Kaggle ASL alphabet dataset and NUS hand posture dataset for evaluation.

## Technologies Used

- **Backend:** Django
- **Cloud Services:** AWS S3 for storage
- **Machine Learning:** TensorFlow, Keras
- **NLP:** Python Libraries

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nirbhay-naari.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up AWS credentials and database configurations as per the `config.py` file.

4. Run the application:
   ```bash
   python manage.py runserver
   ```

## Screenshots of User Interface (UI) for Respective Modules

- **Homepage of Portal:**
  ![Homepage](https://github.com/user-attachments/assets/1608d53a-b6ab-4686-807d-02e67f4c24f0)
  
- **Additional Functionalities:**
  ![Additional Functionalities 1](https://github.com/user-attachments/assets/78576d41-f903-417b-9a8f-97fc896f46f9)
  ![Additional Functionalities 2](https://github.com/user-attachments/assets/9ebbfb53-65bd-4f44-a35e-c337ebbf087d)

- **Section for Victim to Provide Audio/Video Proof:**
  ![Audio/Video Proof](https://github.com/user-attachments/assets/56bfce73-8ba3-495c-8dc1-e3011fb0506c)

- **Model Accuracy Display:**
  ![Model Accuracy](https://github.com/user-attachments/assets/8861bef6-84d0-44bf-9aa4-789a663c1d89)

- **Story Narration Section:**
  ![Story Narration](https://github.com/user-attachments/assets/17cc3418-7204-4575-991d-c42300fe8b34)

- **Output Depicting Violence Type:**
  ![Violence Type](https://github.com/user-attachments/assets/59b62d8d-bd7e-47f5-b457-c50e905be585)

- **Video Proof Upload Section:**
  ![Video Proof](https://github.com/user-attachments/assets/9a38c8f8-f369-4ac2-b574-c804622ec8c8)

- **Portal Detecting Violence Presence:**
  ![Violence Detection](https://github.com/user-attachments/assets/3e82412a-103e-45d3-857f-5bbe1cb13eac)

- **Contact Us Page:**
  ![Contact Us](https://github.com/user-attachments/assets/82815b90-3948-4fb8-b6bf-12f75e26dcba)

- **Live Coordinates Sharing with Emergency Contact:**
  ![Live Coordinates](https://github.com/user-attachments/assets/1c0d21a1-3b13-418e-905c-48d547fdfc59)

- **Message to Emergency Contact:**

  ![Message to Emergency Contact](https://github.com/user-attachments/assets/8154214d-7633-4111-a32f-0682c7dbdaaf)

