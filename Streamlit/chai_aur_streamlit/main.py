import streamlit as st

st.title("Hello Chai App")
st.subheader("Made with streamlit")
st.text("Welcome to our first interactive app")
st.write("Choose your favorite variety of chai")

chai = st.selectbox("Select your favorite chai", ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Lemon Chai"])

st.write(f" You choose {chai}. Excellent choice!")

st.success("Enjoy your cup of chai! ☕")

if st.button("Make Chai"):
    st.success("Your chai is being prepared! Please wait a moment...")

add_masala = st.checkbox("Add Masala")
if add_masala:
    st.write("Masala added to your chai! It will be extra flavorful.")

tea_type = st.radio("Choose your tea base", ["Milk", "Almond Milk", "Water"])
st.write(f"You selected {tea_type} as your tea base.")  

flavour = st.selectbox("Select a flavor", ["Cardamom", "Ginger", "Clove", "Cinnamon"])
st.write(f"You selected {flavour} flavor for your chai.")

suger = st.slider("Select the amount of sugar in spoons", 0, 5, 2)
st.write(f"You selected {suger} spoons of sugar for your chai.")

cups = st.number_input("How many cups of chai would you like?", min_value=1, max_value=10, value=1)
st.write(f"You have ordered {cups} cups of chai. We will prepare it right away!")

name = st.text_input("Enter your name")
if name:
    st.write(f"Thank you, {name}! Your chai will be ready soon.")
    
dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth is: {dob}")