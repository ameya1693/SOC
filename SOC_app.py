import numpy as np
import tensorflow as  tf
import pandas as pd
import streamlit as st

#st.set_option('depreciation.showfileUploaderEncoading', False)
@st.cache(allow_output_mutation=True)

def load_model():
    model = tf.keras.models.load_model("my_model2.hdf5")
    return model
model= load_model()
# file= open("model2.json","r")
# loaded_model_json= file.read()
# file.close()

# model.load_weights("model2.h5")
# classifier= pickle_in.load(pickle_in)

def predict_soc(hour, speed, voltage, current, temp):
    prediction= model.predict([[hour, speed, voltage, current, temp]])
    print(prediction)
    return prediction

def main():
    st.title("Battery SOC Predictor")
    html_temp="""
    <div style="bacground-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit SOC Predictor ML App</h2>
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    # day = st.text_input("Day")
    hour= st.number_input("Hour")
    speed= st.number_input("Speed")
    voltage = st.number_input("Voltage")
    current = st.number_input("Current")
    temp = st.number_input("Temp")

    result=""
    if st.button("predict"):
        result= predict_soc(hour, speed, voltage, current, temp)
    st.success('The output is {}'.format(result))

if __name__ == '__main__':
    main()