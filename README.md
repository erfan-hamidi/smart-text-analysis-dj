# smart-text-analysis-dj
System Analysis and Design Project - Buali Sina university
## <a href="https://docs.google.com/document/d/1FNOPGcMwcgWNx5GGXCWIE0_kgJKzGjx4ChPE7sT29m4/edit?usp=sharing"> Project Report link </a>
## -> this project have to main AI parts :
1. sentiment analysis (Persian and english support) : this Phase is based on CNN model and used IMDB Dataset of 50K Movie Reviews .
2. text summarization (Persian and english support) : this Phase is based on Bart model that is a Seq-to-Seq Pre-training model for Natural Language Generation, Translation, and Comprehension . our dataset is cnn_dailymail .
3. image retreieval system  : this Phase is based on VGG16 Deep model .
4. spam sms/email detection : using ensemble learning using : 1- MultinomialNB()  2-LinearSVC()  3-DecisionTreeClassifier() with 98.5% accuracy

downlaod model :
<p><a href="https://drive.google.com/file/d/13QmMsfNwvm6U4asXd6gurvSkl3nbuIEL/view?usp=drive_link"> english sentiment analysis model link (imdb dataset)</a>  </p>
<p><a href="https://drive.google.com/file/d/1T3IXeqAld5d6xq1Qq6DMsqXkvNzviYFc/view?usp=sharing"> persian sentiment analysis model link (digikala dataset) </a>  </p>
<p><a href="https://drive.google.com/file/d/10EZapoHN0lJ2MTZDTI6qS04ta0h0P9Bx/view?usp=sharing"> english text summarization model link (cnn-dailymail dataset) </a>  <p><a href="https://drive.google.com/file/d/1sESyT11mTa2pI4PT4vMqVufeC1NE2s45/view?usp=sharing"> english spam detection model link  </a>

<a href="https://www.aparat.com/v/zliNs" > AI part technical report video</a> 

## Charts
plots of persian sentiment analysis model 
<img src="https://s8.uupload.ir/files/per-sen-model-chart_0jbt.png" width="750" height="330" > 

plots of english sentiment analysis model 
<img src="https://s8.uupload.ir/files/sen-ana-en-plt_n12z.png" width="750" height="330" > 

## image retrieval output result :
<img src="https://s8.uupload.ir/files/run_prj_b8n.png" >
## Installation

```bash
    $ cd smart-text-analysis
    $ python -m venv venv
    $ source venv/Scripts/activate
    (venv) pip install -r requirements.txt
    (venv) python manage.py makemigrations
    (venv) python manage.py migrate
    (venv) python manage.py runserver
```
