import streamlit as st

# Setting the page configuration
st.set_page_config(page_title="Elevator Company", layout="wide")

# Header Section
st.markdown(
    """
    <style>
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #004080;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
    <div class="header">Welcome to Our Elevator Solutions</div>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.image(
    r"img1.jpg", 
    caption="Rising Above Expectations", use_container_width=True
)
st.button("Explore Services", key="hero_button")

# Services Section
st.subheader("Our Services")
cols = st.columns(3)
services = [
    ("Installation", "We provide state-of-the-art elevator installations for residential, commercial, and industrial spaces."),
    ("Maintenance", "Keep your elevators running smoothly with our regular maintenance services."),
    ("Modernization", "Upgrade your existing elevators with the latest technology and designs.")
]

for i, (title, desc) in enumerate(services):
    with cols[i]:
        st.markdown(f"**{title}**")
        st.write(desc)

# Portfolio Section
st.subheader("Our Projects")
st.write("Here are some of the projects we’ve completed:")
images = [
    r"project1.jpeg",
    r"project2.jpeg",
    r"project3.jpeg"
]
cols = st.columns(3)
for i, img in enumerate(images):
    with cols[i]:
        st.image(img, caption=f"Project {i+1}", use_container_width=False, width=400)
        st.markdown(
            """
            <style>
                img {
                    height: 500px; /* Fixed height for uniformity */
                    object-fit: cover; /* Ensures the image fits within the height */
                }
            </style>
            """,
            unsafe_allow_html=True
        )
# About Us Section
st.subheader("About Us")
st.write(
    """
    We are a leading elevator company with decades of experience in providing safe, reliable, and efficient vertical transportation solutions.
    Our team is committed to excellence and customer satisfaction.
    """
)

# Contact Section
st.subheader("Contact Us")
st.write("Have questions? Reach out to us:")
contact_form = st.form("contact_form")
with contact_form:
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success("Thank you! We will get back to you shortly.")

# Footer Section
st.markdown(
    """
    <style>
        .footer {
            font-size: 14px;
            text-align: center;
            color: #808080;
            margin-top: 50px;
        }
    </style>
    <div class="footer">
        © 2025 Elevator Company. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)
