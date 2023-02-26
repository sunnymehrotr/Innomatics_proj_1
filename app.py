import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



st.title('Titanic Dataset')
st.text("""The titanic dataset describe the survival status of individual passengers on the Titanic.
It also contains various other important features about the passengers like Age,
Class, Sex,Ticket Price making it a useful and important data for analysis.""")
st.image('titanic.jpg',width=500)
df=pd.read_csv('tested.csv')
st.dataframe(df)
# plotting the number of people survived
fig_1=df['Survived'].value_counts().values
b=[0,1]
class_1=df['Pclass'].value_counts()

col1,col2=st.columns(2)

with col1:
    fig, ax1 = plt.subplots()
    ax1.bar(b, fig_1,color='brown')
    ax1.set_xticks(np.arange(2))
    ax1.set_title('Survived bar chart')
    st.pyplot(fig)

with col2:
    fig, ax1 = plt.subplots()
    ax1.pie(class_1, labels=['3', '1', '2'], autopct='%.2f')
    ax1.set_title('Distribution of classes')
    ax1.legend(labels=['3', '1', '2'], loc='upper right')
    st.pyplot(fig)

fig,ax1=plt.subplots()
ax1.hist(df['Age'])
ax1.set_xlabel('Age')
ax1.set_ylabel('Count')
ax1.set_title('Age Distribution')
st.pyplot(fig)