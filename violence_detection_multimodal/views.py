from django.http import HttpResponse
from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from .models import Audio
from .forms import AudioForm
from .predictviolence import VideoCamera
import cv2
from tensorflow import keras
from videoreader import VideoReader
from keras.models import load_model
from keras import models
import numpy as np
from skimage.transform import resize
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.feature_extraction.text import TfidfVectorizer
import speech_recognition as sr
import joblib
import moviepy.editor as mp

from scipy.io.wavfile import read
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import tensorflow as tf

from django.views.generic.edit import FormView
from multiprocessing import context
from django.shortcuts import render


from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Flatten
import requests
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
import json


reloadModel=joblib.load('./models/mymodel.pkl')
tfidf = TfidfVectorizer(stop_words='english', analyzer='word',
                        max_features=10000, ngram_range=(1, 3))
df = pd.read_csv('data_violence3.csv')
X = tfidf.fit_transform(df['notes'])
multilabel = MultiLabelBinarizer()
y = multilabel.fit_transform(
    [['domestic_violence', 'fatalities', 'psychological_violence', 'sexual_violence']])
y = df[['domestic_violence', 'fatalities',
        'psychological_violence', 'sexual_violence']]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)


def predicthelpHandSignal():

    
    if request.method == 'POST':
        
        if 'fist' in names:
            context = {'classes':'help needed'}
        else:
            context = {'classes': 'no help needed'}
        return render(request,'index.html', context)


def process_file(filename):
    arr = []
    model =  keras.models.load_model("finalhebhai.pb")
    model1 =  keras.models.load_model("gendermodel2.pb")
    print("Scream Detection model loaded")
    
    data, rs = read(filename)
    
    suitable_length_for_model = 48250
    rs = rs.astype(float)
    rs = rs[0:suitable_length_for_model+1]
    a = pd.Series(rs)
    arr.append(a)
    df = pd.DataFrame(arr)
    X2 = df.iloc[0:, 1:]
    #print(X2)
    predictions = model.predict(X2)
    predictions1 = model1.predict(X2)
    rounded = [round(x[0]) for x in predictions]
    rounded1 = [round(x[0]) for x in predictions1]
    print("predicted value is" + str(rounded))
    print("predicted value is" + str(rounded1))
    if str(rounded1)=='[1]':
        print("FEMALE SCREAMS DETECTED")
        return "FEMALE SCREAMS DETECTED"
    elif str(rounded)=='[1]':
        print("SCREAMS DETECTED (NO FEMALE SCREAMS DETECTED) ")
        return "SCREAMS DETECTED (NO FEMALE SCREAMS DETECTED) "
    else:
        print("NO SCREAMS DETECTED")
        return "NO SCREAMS DETECTED"
def predictViolence(request):
    form= AudioForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    lastaudio= Audio.objects.last()
    temp=lastaudio.text
    print(temp)
    if temp=="":

        audiofile= lastaudio.audiofile
        context= {'audiofile': audiofile,
                  'form': form
                  }
        print("#####___________#######https://mynirbhaynaari.s3.amazonaws.com/static/"+str(audiofile))
        temp1 ="https://mynirbhaynaari.s3.amazonaws.com/static/"+str(audiofile)#"https://mynirbhaynaari.s3.ap-south-1.amazonaws.com/static/"+str(audiofile)
        filename = temp1
        r = sr.Recognizer()
        doc = requests.get(temp1)
        with open('myfile.wav', 'wb') as f:
            f.write(doc.content)
        with sr.AudioFile('myfile.wav') as source:
            print("HIIIIIIIII")
            audio_data = r.record(source)
            temp = r.recognize_google(audio_data)
    testDtaa = [temp]
    vectorized_input_data = tfidf.transform(testDtaa)
    pred=reloadModel.predict(vectorized_input_data)
    scoreval = multilabel.inverse_transform(pred)
    context = {'scoreval': scoreval}
    print(scoreval)
    return render(request,'colorapp/storyresult.html', context)

    # if request.method == 'POST':
    #     temp = request.POST.get('story')
    #     if temp == "":
    #         temp1 = request.POST.get('storyaudio')
    #         filename = temp1
    #         r = sr.Recognizer()
    #         with sr.AudioFile(filename) as source:
    #             audio_data = r.record(source)
    #             temp = r.recognize_google(audio_data)
    #     testDtaa = [temp]
    #     vectorized_input_data = tfidf.transform(testDtaa)
    #     pred=reloadModel.predict(vectorized_input_data)
    #     scoreval = multilabel.inverse_transform(pred)
    #     context = {'scoreval': scoreval}
    #     print(scoreval)
    #     return render(request,'colorapp/storyresult.html', context)
    # else:
    #     return render(request,'colorapp/storyresult.html','something went wrong')

def pred_fight(model,video,acuracy=0.9):
    pred_test = model.predict(video)
    print(pred_test[0][1])
    if pred_test[0][1] >=acuracy:
        return True , pred_test[0][1]
    else:
        return False , pred_test[0][1]

def home(request):
    context = {}
    return render(request, 'colorapp/home.html', context)

def about(request):
    context = {}
    return render(request, 'colorapp/about.html', context)

def loginpage(request):
    context = {}
    return render(request, 'colorapp/login.html', context)

def report(request):
    context ={}
    context['form']= VideoForm()
    return render(request, 'colorapp/report.html', context)
def livereport(request):
    context ={}

    return render(request, 'colorapp/livereport.html', context)
def showvideo(request):
    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    lastvideo= Video.objects.last()

    videofile= lastvideo.videofile
    context= {'videofile': videofile,
              'form': form
              }

    #print("model loaded")
    
    model = models.load_model("DV_model.h5")
    print("Hii model loaded")
    print("##########","https://mynirbhaynaari.s3.amazonaws.com/static/"+str(videofile))
    cap = cv2.VideoCapture("https://mynirbhaynaari.s3.amazonaws.com/static/"+str(videofile))
    my_audio_clip = mp.VideoFileClip(r"https://mynirbhaynaari.s3.amazonaws.com/static/"+str(videofile))
    #my_audio_clip.audio.write_audiofile(r"media/"+"my_result.mp3")

    # src = "media/"+"my_result.mp3"
    # dst = "media/"+"my_result1.wav"

    # # convert wav to mp3                                                            
    # audSeg = AudioSegment.from_mp3(src)
    # audSeg.export(dst, format="wav")
    # return
    output2 = process_file("media/"+"samplescream.wav")
    scoreval=[]
    


    i = 0
    frames = np.zeros((30, 160, 160, 3), dtype=np.float)
    old = []
    j = 0
    
    try:
        violence=0
        help=0
        while (cap.isOpened()):
            ret, frame = cap.read()
                    
            # describe the type of font
            # to be used.
            #font = cv2.FONT_HERSHEY_SIMPLEX
            if i > 29:
                ysdatav2 = np.zeros((1, 30, 160, 160, 3), dtype=np.float)
                ysdatav2[0][:][:] = frames
                predaction = pred_fight(model, ysdatav2, acuracy=0.96)
                print(predaction)
                if predaction[0] == True:
                    violence=1
                    break
                i = 0
                j += 1
                frames = np.zeros((30, 160, 160, 3), dtype=np.float)
                old = []
            else:
                frm = resize(frame, (160, 160, 3))
                old.append(frame)
                fshape = frame.shape
                fheight = fshape[0]
                fwidth = fshape[1]
                frm = np.expand_dims(frm, axis=0)
                if (np.max(frm) > 1):
                    frm = frm / 255.0
                frames[i][:] = frm
                i += 1
            #cv2.imshow('video', frame)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
                #break

        if violence==0:
            print('NO VIOLENCE DETECTED...')
            scoreval.append('NO VIOLENCE DETECTED...')
        else:
            scoreval.append('VIOLENCE DETECTED...')
            print('VIOLENCE DETECTED...')
        if help==1:
            scoreval.append("HELP NEEDED")
        elif help==0:
            scoreval.append("HELP HAND SIGNAL NOT DETECTED")
        
    except AttributeError:
        print('NO VIOLENCE DETECTED...')
    cap.release()
    scoreval.append(output2)
    print(scoreval)
    context = {'scoreval': scoreval}
    
    return render(request, 'colorapp/report1.html', context)

def signup(request):
    context = {}
    return render(request, 'colorapp/signup.html', context)  

def story(request):
    context = {}
    context['form']= AudioForm()
    return render(request, 'colorapp/story.html', context) 

def location(request):
    context = {}
    return render(request, 'colorapp/location.html', context) 
REV_CLASS_MAP = {
    0: "help",
    1: "None"
}


def mapper(val):
    return REV_CLASS_MAP[val]


def predictSOS(request):
    if request.method == 'POST':
        model = load_model("./models/userlocationtosos.h5")

        cap = cv2.VideoCapture(0)

        prev_move = None
        count = 0
        while True:
            # print("#######")
            ret, frame = cap.read()
            if not ret:
                continue
            cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)
            roi = frame[100:500, 100:500]
            img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
            img = cv2.resize(img, (227, 227))

            # predict the move made
            pred = model.predict(np.array([img]))
            move_code = np.argmax(pred[0])
            user_move_name = mapper(move_code)

            if user_move_name == "help":
                count+=1

            if prev_move != user_move_name:
                prev_move = user_move_name
            

            # display the information
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, "Your Move: " + user_move_name,
                        (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.imshow("SOS", frame)

            k = cv2.waitKey(10)
            if k == ord('q'):
                break
            
            if count>=3:
                print("help needed")
                cap.release()
                cv2.destroyAllWindows()
                return render(request,'colorapp/location.html')

@csrf_exempt
def getmylocation(request):
    if request.method == 'POST':
        print(request.body)
        a = request.body
        b = (json.loads(a.decode('utf-8')))
        mylong = (b.get("Longitude"))
        mylat = (b.get("Latitude"))

        account_sid = "AC2e72152d243f6b4c578356fcf38c3d81"
        auth_token = "c4b7044a765a0d171033e2f99939f06b"
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                                    body="I am in DANGER, i need help. Please urgently reach me out. Here are my coordinates.\n" + "http://www.google.com/maps/place/" + str(mylat) + "," + str(mylong),
                                    from_='+19126003960',
                                    to='+919767314066'
                                )
        print(message.sid)
        if len(message.sid)!=0:
            # print("send")
            context = {"SEND": "SENT"}
            print(context.get("SEND"))
            return render(request,'colorapp/location.html')
        return render(request,'colorapp/location.html')
        