import streamlit as st

# Set page configuration
st.set_page_config(page_title="Kishore Aquarium", page_icon="🐠", layout="wide")

# --- HEADER SECTION ---
st.title("🐠 WELCOME TO KISHORE AQUARIUM")
st.subheader("Discover the magical world beneath the waves.")
st.write("Explore our species, check daily feeding times, or contact us for tickets.")

# --- SIDEBAR NAVIGATION ---
st.sidebar.header("Navigation")
menu = st.sidebar.radio("Go to:", ["Home", "Species Showcase", "Visitor Info"])

# --- CONTENT SECTIONS ---
if menu == "Home":
    st.image("https://www.bunnycart.com/blog/aquarium-decor-dos-and-donts-every-aquarist-should-know/") 
    st.write("Welcome to the most interactive aquarium in the city.")

elif menu == "Species Showcase":
    st.header("✨ Meet Our Marine Friends")
    
    # Using columns for layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Clownfish")
        st.image("https://images.unsplash.com/photo-1599488126756-f6f70a7d5a57?q=80&w=300")
        st.write("Small, vibrant, and famously found in anemones.")
        
    with col2:
        st.subheader("Blue Tang")
        st.image("https://images.unsplash.com/photo-1598971836109-17d91f24d1a2?q=80&w=300")
        st.write("Recognizable by its stunning blue color and yellow tail.")
        
    with col3:
        st.subheader("Sea Turtle")
        st.image("https://images.unsplash.com/photo-1549117625-f37e466d790f?q=80&w=300")
        st.write("Gentle giants swimming gracefully in the deep.")

elif menu == "Visitor Info":
    st.header("📅 Plan Your Visit")
    st.write("Open Daily: 9:00 AM - 6:00 PM")
    
    # Form for contact
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Ask us anything!")
        submit = st.form_submit_button("Submit")
        
        if submit:
            st.success(f"Thanks {name}! We will get back to you at {email}.")

# --- FOOTER ---
st.write("---")
st.write("© 2025 Kishore Aquarium | Built with Streamlit")