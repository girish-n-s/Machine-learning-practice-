# 📧 Spam Mail Detection using Naive Bayes

This is a simple but effective **Spam Mail Detection** system built using the **Naive Bayes classifier**. It takes user-input email text and classifies it as **Spam** or **Not Spam** based on the words it contains.

---

## 🚀 Features

- Detects spam emails using trained data and probabilistic logic.
- Custom implementation of Naive Bayes with smoothing.
- Simple front-end form to paste email content.
- Displays prediction result on the **same page** (no redirection).
- Built using Flask – easy to run locally.

---

## 🛠️ Tech Stack

- **Python**
- **Flask** (for web interface)
- **Scikit-learn** & **NLTK** (for model training and text processing)
- **HTML/CSS** (for the front end)

---

## 📂 Project Structure
spam-mail-detector/
│
├── app.py               # Main Flask application
├── model.json           # Saved word probabilities or model structure
├── templates/
│   ├── index.html       # Frontend HTML form
│   └── about.html       # (Optional) About page
├── README.md


---

## ⚙️ How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/spam-mail-detector.git
   cd spam-mail-detector


pip install flask pandas

python app.py


## 📊 Dataset Used

- The project uses labeled email data to distinguish between **spam** and **ham (not spam)** messages.
- You can use open datasets like the [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/jayaprakashpondy/email-spam).
- The dataset is cleaned, tokenized, and used to calculate word probabilities for the Naive Bayes classifier.
- You can also extend this project using real email text data from your inbox (just for learning purposes).


## 🔗 Connect with Me

💼 [LinkedIn](https://www.linkedin.com/in/girish-n-s-024a06259?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BbtkGRRQSQVaZzqtkX1Y1Rw%3D%3D)    
⭐ GitHub: [github.com/yourusername](https://github.com/girish-n-s)

