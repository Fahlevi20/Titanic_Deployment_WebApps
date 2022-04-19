from matplotlib.pyplot import title
import numpy
import pandas as pd
import streamlit as st
import pickle
import numpy as np

model=pickle.load(open(r'svcobj.pickle','rb'))


def main():
    st.title('Prediksi Korban Titanic')
    st.image(r'download.jpeg')
    st.write("""apakah korban tersebut selamat?""")

    st.sidebar.header('more detail:')

    st.title("--          Periksa yuk berapa persen peluang hidup mereka          --")
    AgeGroup = st.slider('Masukkan Kategori Umur:',1,5,7)
    
    SibSp = st.selectbox("How many Siblings or spouses are t    ravelling with you?", [0, 1, 2, 3, 4, 5, 6, 7, 8]) # Select box
    
    Parch = st.selectbox("How many Parents or children are travelling with you?", [0, 1, 2, 3, 4, 5, 6, 7, 8]) # Select box
    
    sex = st.selectbox("Select Gender:", ["Male","Female"])                         # select box for gender[Male|Female]
    if (sex == "Male"):                                                             # selected gender changes to [Male:0 Female:1]
        Sex=0
    else:
        Sex=1
    
    Pclass= st.selectbox("Select Passenger-Class:",[1,2,3])                        # Select box for passenger-class
    
    cabin = st.selectbox("Di dalam cabin:", ["ya","tidak"])                         # select box for gender[Male|Female]
    if (cabin == "ya"):                                                             # selected gender changes to [Male:0 Female:1]
        cabin=1
    else:
        cabin=0
    
    boarded_location = st.selectbox("Boarded Location:", ["Southampton","Cherbourg","Queenstown"]) ## Select Box for Boarding Location
    #Embarked_C,Embarked_Q,Embarked_S=0,0,0                     # initial values are 0
    # As we encoded these using one-hot-encode im ml model; so if 'Q' selected value is C=2,Q=3;S=1 , if 'S' selected value is C=0,Q=0;S=1 likewise
    if boarded_location == "Queenstown":
        boarded_location=3
    elif boarded_location == "Southampton":
        boarded_location=1
    else:
        boarded_location=2
    
    title_mapping = st.selectbox('panggilan/gelar:', ["Mr", "Miss", "Mrs", "Master", "Royal", "Rare"])
    title_Mr,title_Miss,title_Mrs,title_Master,title_Royal,title_Rare=0,0,0,0,0,0
    if title_mapping == 'Mr':
        title_mapping=1
    elif title_mapping == "Miss":
        title_mapping=2
    elif title_mapping == "Mrs":
        title_mapping=3
    elif title_mapping == "Master":
        title_mapping = 4
    elif title_mapping == "Royal":
        title_mapping = 5
    else: 
        title_mapping = 6
    
    fare_band = st.selectbox('kategori uang:', ['rendah','normal','agak tinggi','tinggi'])
    fare_rendah,fare_normal,fare_AgakTinggi,fare_tinggi=0,0,0,0
    if fare_band == 'rendah':
        fare_band = 1
    elif fare_band == 'normal':
        fare_band = 2
    elif fare_band == 'agak tinggi':
        fare_band = 3
    elif fare_band == 'tinggi':
        fare_band = 4    

    data={"Pclass":Pclass,"Sex":Sex,"SibSp":SibSp,"Parch":Parch,"board_location":boarded_location, "AgeGroup":AgeGroup,"CabinBool":cabin,"title":title_mapping,"fare band":fare_band}
    df=pd.DataFrame(data,index=[0])      ## converting dictionary to Dataframe
    return df

data=main()                             ## calling Main()

if st.button("Predict"):                                                                ## prediction button created,which returns predicted value from ml model(pickle file)
    result = model.predict(data)                                                        ## prediction of user-input
    proba=model.predict_proba(data)                                                     ## probabilty prediction of user-input
    #st.success('The output is {}'.format(result))

    if result[0] == 1:
        st.write("***congratulation !!!....*** **You probably would have made it!**")
        st.image(r"lifeboat.jfif")
        st.write("**Survival Probability Chances :** 'NO': {}%  'YES': {}% ".format(round((proba[0,0])*100,2),round((proba[0,1])*100,2)))
    else:
        st.write("***Better Luck Next time !!!!...*** **you're probably Ended up like 'Jack'**")
        st.image(r"Rip.jfif")
        st.write("**Survival Probability Chances :** 'NO': {}%  'YES': {}% ".format(round((proba[0,0])*100,2),round((proba[0,1])*100,2)))

## Working Button:
if st.button("Working"):                                                      # creating Working button, which gets some survival tips & info.
    st.write("""# How's prediction Working :- Insider Survival Facts and Tips: 
             - Only about `32%` of passengers survived In this Accident\n
             - Ticket price:
                    1st-class: $150-$435 ; 2nd-class: $60 ; 3rd-class: $15-$40\n
             - About Family Factor:
                If You Boarded with atleast one family member `51%` Survival rate
               """)
    st.image(r"gr.PNG")

## Author Info.
if st.button("Author"):
    st.write("## dibuat oleh Mukhammad Fahlevi Ali Rafsanjani")
    st.write("## yang akan menjadi peneliti paling bebas di dunia")