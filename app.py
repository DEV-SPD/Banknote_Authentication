import streamlit as st 
import pickle 

with open('BanknoteAuthentication','rb') as f:
    model = pickle.load(f)


def main():
    st.title('BANK NOTE AUTHENTICATION') 

    # Taking User Inputs
    v1 = st.text_input('VARIANCE')
    v2 = st.text_input('SKEWNESS')
    v3 = st.text_input('CUROSITY')
    v4 = st.text_input('ENTROPY')

    if (st.button('PREDICT')):
        prediction = model.predict([[v1,v2,v3,v4]])
        st.success(prediction)


if __name__ == '__main__':
    main()
