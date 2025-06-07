from flask import Flask, request, render_template
import logging
from datetime import datetime

# For demo, replace this with your actual model prediction function
def split_cust(email):
    words=[]
    common_words = set(['a','as','are','at','to','too','or','and','subject','what','when','not','re','let'])

    email =email.lower()
    i=0
    j=0
    count=0
    while (i<len(email)):
        while((i<len(email))and(email[i]!=' ' and email[i]!='\n' and email[i]!='\t' and email[i]!=',' and email[i]!='-' and email[i]!=':' and email[i]!='.' and email[i]!= "'" and email[i]!='"' and email[i]!='_')):
            i+=1
        word = email[j:i]
        while((i<len(email))and(email[i]==' ' or email[i]=='\n' or email[i]=='\t' or email[i]==',' or email[i]=='-' or email[i]==':' or email[i]=='.' or email[i]== "'" or email[i]=='"' or email[i]=='_')):
            i+=1
        j=i
        if  word not in common_words and word != '':
            words.append(word)
            count+=1
    return words

    
    

def predict_mail(text):
    import json
    from collections import defaultdict
    import numpy as np
    with open("model.json",'r') as file:
        model_data = json.load(file)
        total_unique_words = model_data['number_of_words']
        total_spam_words = model_data["spam_word_count"]
        total_ham_words = model_data["ham_word_count"]
        prob_word_spam  = model_data["prob_word_spam"]
        prob_word_ham   = model_data["prob_word_ham"]
        prob_spam = model_data["prob_spam"]
        prob_ham = model_data["prob_ham"]
    
    prob_word_spam = defaultdict(int,prob_word_spam)
    prob_word_ham = defaultdict(int,prob_word_ham)
    
    words= split_cust(text)
    p_spam =0
    p_ham = 0
    
    for w in words:
        if(prob_word_spam[w]==0):
            prob_word_spam[w]=1/(total_spam_words+total_unique_words)
        p_spam += np.log(prob_word_spam[w])
        if(prob_word_ham[w]==0):
            prob_word_ham[w]=1/(total_ham_words+total_unique_words)
        p_ham += np.log(prob_word_ham[w])
    p_spam+=np.log(prob_spam)
    p_ham += np.log(prob_ham)
    if p_spam>p_ham:
        return "Predicted as SPAM be cautious " 
    return "No need to worry"

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        mail_text = request.form.get('mail')
        if mail_text:
            result = predict_mail(mail_text)  # Your ML prediction function
    return render_template('index.html', result=result)


@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
