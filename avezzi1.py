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
    <div class="header">Welcome to "THE LIFTS"</div>
    """,
    unsafe_allow_html=True
)

# Hero Section
st.image(
    r"img1.jpg", 
    use_container_width=True
)
st.markdown(
    f"<p style='font-weight:bold; font-size:22px; font-style:italic; text-align:center;'>&quot;Rising Above Expectations&quot;</p>",
    unsafe_allow_html=True
)
# About Us Section
st.markdown(
    """
    <h2 style="font-size:40px; color:#004080; font-weight:bold; margin-bottom:10px; text-align:center;">
        About Us
    </h2>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="font-size:20px; font-family: Arial, sans-serif; color:#316723; line-height:1.8; text-align:center; padding:20px; border-left:5px solid #004080; margin-bottom:30px;">
        <p><strong><em>We are a leading elevator company with decades of experience providing safe, reliable, and efficient vertical transportation solutions.</em></strong></p>
        <p><em>"Our team is committed to excellence and customer satisfaction."</em></p>
    </div>
    """,
    unsafe_allow_html=True
)
#st.button("Explore Services", key="hero_button")
# Services Section
st.markdown(
    """
    <h2 style="font-size:40px; color:#004080; font-weight:bold; margin-bottom:10px; text-align:center;">
        Services
    </h2>
    """,
    unsafe_allow_html=True
)
cols = st.columns(3)
services = [
    ("Installation", "We provide advanced elevator installations for residential, commercial, and industrial spaces."),
    ("Maintenance", "Keep your elevators running smoothly with our regular maintenance services."),
    ("Modernization", "Upgrade your existing elevators with the latest technology and designs.")
]

for i, (title, description) in enumerate(services):
    with cols[i]:
        st.markdown(f"<h3 style='font-size:24px; font-weight:bold; color:#17212b; margin-bottom:10px; text-align:center;'>{title}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='font-size:18px; line-height:1.6; color:#555555; text-align:center;'> {description} </p>", unsafe_allow_html=True)
        st.markdown("<hr style='border-top: 2px solid #004080; margin: 20px 0;'>", unsafe_allow_html=True)

# Portfolio Section
# Styled Section Header
st.markdown(
    """
    <h2 style="font-size:40px; color:#004080; font-weight:bold; margin-bottom:10px; text-align:center;">
        Projects
    </h2>
    """,
    unsafe_allow_html=True
)

# Styled Description
st.markdown(
    """
    <p style="font-size:30px; font-style:italic; color:#333333; line-height:1.6; text-align:center; margin-bottom:30px;">
        Here are some of the projects we’ve completed
    </p>
    """,
    unsafe_allow_html=True
)

# Define images, captions, and descriptions
projects = [
    {
        "image": r"project1.jpeg",
        "caption": "Houses",
        "description": '"Our residential elevator solutions bring convenience and luxury to homes with cutting-edge technology and sleek designs."'
    },
    {
        "image": r"project2.jpeg",
        "caption": "Commercials",
        "description": """We specialize in commercial elevators that prioritize efficiency, safety, and cutting-edge technology. 
        Whether it's for bustling shopping malls, modern office buildings, or industrial facilities, our solutions are designed 
        to handle high traffic with ease and reliability. With advanced features like energy-efficient drives, touchless controls, 
        and robust safety systems, our elevators ensure a seamless experience for both building owners and users."""
    },
    {
        "image": r"project3.jpeg",
        "caption": "Legacy",
        "description": """Preserving the charm of legacy buildings is our priority. Through our elevator modernization services, we seamlessly combine 
        heritage aesthetics with modern functionality. In addition to new installations, we also ensure the longevity and reliability 
        of older systems through our dedicated maintenance services, keeping the essence of the past alive while meeting present-day 
        safety and performance standards."""
    }
]

# Loop through each project and create alternating layouts
for i, project in enumerate(projects):
    cols = st.columns([1, 2])  # Adjust width ratio (1:2) for better alignment
    if i % 2 == 0:  # Image on the left, description on the right
        with cols[0]:
            st.image(project["image"], use_container_width=True)
            st.markdown(f"<p style='font-weight:bold; font-size:22px; font-style:italic; text-align:center;'>{project['caption']}</p>", unsafe_allow_html=True)
        with cols[1]:
            st.markdown(
                f"""
                <div style="font-size:30px; font-style:italic; line-height:1.5; text-align:justify; margin-left:10px; margin-top:25%;">
                    {project['description']}
                </div>
                """,
                unsafe_allow_html=True
            )
    else:  # Image on the right, description on the left
        with cols[0]:
            st.markdown(
                f"""
                <div style="font-size:30px; font-style:italic; line-height:1.5; text-align:justify; margin-right:10px; margin-top:50%;">
                    {project['description']}
                </div>
                """,
                unsafe_allow_html=True
            )
        with cols[1]:
            st.image(project["image"], use_container_width=True)
            st.markdown(f"<p style='font-weight:bold; font-size:22px; font-style:italic; text-align:center;'>{project['caption']}</p>", unsafe_allow_html=True)

# Tagline/Trust Section
st.markdown(
    """
    <h3 style="font-size:28px; font-weight:bold; text-align:center; color:#004080;">Why Choose Us?</h3>
    <ul style="font-size:18px; color:#333333; line-height:1.6; text-align:left;">
        <li>Our engineers bring valuable experience from prestigious Middle Eastern countries like Dubai, ensuring global expertise.</li>
        <li>With over 10 years of hands-on experience in elevator design, installation, and maintenance, our team is built on trust and quality.</li>
        <li>We prioritize safety, efficiency, and innovative solutions that cater to both residential and commercial sectors.</li>
        <li>Our customer-first approach has made us a trusted partner in providing reliable and efficient vertical transportation systems.</li>
        <li>We are committed to delivering solutions that stand the test of time, ensuring that every project is executed with the highest standards.</li>
    </ul>
    """,
    unsafe_allow_html=True
)

# Contact Section
st.subheader("Contact Us")
# Contact Information with Styling
st.markdown(
    """
    <div style="font-size:18px; color:#333333; line-height:1.6; text-align:left; margin-top:10px;">
        <p><strong>Phone:</strong> +91 97552 39922</p>
        <!--<p><strong>Address:</strong> 123 Elevator St., Building 5, New York, NY 10001</p>-->
        <p><strong>Email:</strong> <a href="mailto:contact@thelifts.com" style="color:#004080; text-decoration:none;">contact@thelifts.com</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
# st.write("Have questions? Reach out to us:")
# contact_form = st.form("contact_form")
# with contact_form:
#     name = st.text_input("Name")
#     email = st.text_input("Email")
#     phone = st.text_input("Phone")
#     message = st.text_area("Message")
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.success("Thank you! We will get back to you shortly.")

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
