# Spam Message Detector 🚨

This project is a Python application that uses machine learning to detect whether emails or messages are spam.

[Türkçe README](README.md)

## 🎯 Features

- Classifies email/message text as spam or normal (ham)
- Text cleaning and preprocessing
- TF-IDF vectorization
- Logistic Regression model
- Interactive console interface

## 🛠️ Requirements

- Python 3.8+
- pandas
- numpy
- scikit-learn
- regex

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Semihkulekcioglu/Email_spam_detection.git
cd Email_spam_detection
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Run the program:
```bash
python Spam_Tespit_Edici.py
```

2. Enter the message text you want to test when prompted
3. The program will analyze the text and indicate if it's spam
4. Press 'q' to quit

<img width="640" height="640" alt="Output" src="https://github.com/user-attachments/assets/632b3ca7-0076-4362-8b8d-42e4456d2387" />

## 📊 Model Performance

The model works with high accuracy on test data. Detailed performance metrics are printed to the console when the program is run.

## 📝 Dataset

The project uses the spam_ham_dataset.csv dataset, which contains examples of spam and normal emails.

## 🤝 Contributing

1. Fork this repository
2. Create a new branch (`git checkout -b feature/newFeature`)
3. Commit your changes (`git commit -am 'New feature: XYZ'`)
4. Push to the branch (`git push origin feature/newFeature`)
5. Create a Pull Request

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---
