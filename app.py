import streamlit as st
import numpy as np

# Set the page configuration
st.set_page_config(page_title="Portfolio App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Profile", "BMI Calculator", "Contact Us"])

# Homepage
if page == "Profile":
    st.title("Welcome to My Profile for Srinakharinwirot University application!")
    st.image("https://cdn.discordapp.com/attachments/1281945784769843210/1314809758087118869/LINE_ALBUM__241202_2.jpg?ex=67551f82&is=6753ce02&hm=eb33da59301090680e802dfa350a2ac2c16afd93e8ba7e8a9d165f096cda3c47&", caption="My Profile", use_column_width=True)
    st.write("""
    Hi! I'm Nipitpon Sutthaluck,  i have a expertise in  Unity 3D program and blender program , i have a bacis for coding python and C# script
    
    ### About Me
    - I am interested in pursuing a degree in Computer Engineering.
    - I have a dream that one day I will become a programmer, and I want to be study at Srinakharinwirot University
    

   I hope to receive a response from the Srinakharinwirot university !
    """)
if page == "BMI Calculator":
    with st.form("contact_form"):
        name = st.text_input("Enter Your Name")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success(name)
        age = st.text_input("Enter Your age")
     # import the streamlit library


        


# give a title to our app
        st.title('Welcome to BMI Calculator')
        
        # TAKE WEIGHT INPUT in kgs
        weight = st.number_input("Enter your weight (in kgs)")
        
        # TAKE HEIGHT INPUT
        # radio button to choose height format
        status = st.radio('Select your height format: ',
                          ('cms', 'meters', 'feet'))

# compare status value
    if(status == 'cms'):
        # take height input in centimeters
        height = st.number_input('Centimeters')
    
        try:
            bmi = weight / ((height/100)**2)
        except:
            st.text("Enter some value of height")
    
    elif(status == 'meters'):
        # take height input in meters
        height = st.number_input('Meters')
    
        try:
            bmi = weight / (height ** 2)
        except:
            st.text("Enter some value of height")
    
    else:
        # take height input in feet
        height = st.number_input('Feet')
    
        # 1 meter = 3.28
        try:
            bmi = weight / (((height/3.28))**2)
        except:
            st.text("Enter some value of height")
    
    # check if the button is pressed or not
    if(st.button('Calculate BMI')):
    
        # print the BMI INDEX
        st.text("Your BMI Index is {}.".format(bmi))
    
        # give the interpretation of BMI index
        if(bmi < 16):
            st.error("You are Extremely Underweight")
        elif(bmi >= 16 and bmi < 18.5):
            st.warning("You are Underweight")
        elif(bmi >= 18.5 and bmi < 25):
            st.success("Healthy")
        elif(bmi >= 25 and bmi < 30):
            st.warning("Overweight")
        elif(bmi >= 30):
            st.error("Extremely Overweight")

# Contact Us
elif page == "Contact Us":
    st.title("Contact Me")
    st.write("""
    I'd love to hear from you! Please fill out the form below or use the provided contact details to get in touch.
    """)
    
    # Contact Form
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")
        
        if submitted:
            st.success("Thank you for reaching out! I'll get back to you soon.")
    
    # Additional Contact Info
    st.write("### Alternatively, you can reach me at:")
    st.write("- Email: nipitponsuttluck@gmail.com")
    st.write("- GitHub: https://github.com/fork923)")
