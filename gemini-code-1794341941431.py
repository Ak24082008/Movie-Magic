import streamlit as st

st.title("🍿 Starlight Cinema Experience")

with st.sidebar:
    st.markdown("### 🎟️ Reserve Your Seats")

    category = st.selectbox(
        "Select ticket tier:", 
        ("Student / Senior", "Standard Experience", "IMAX 3D Luxe", "Private Lounge")
    )

    quantity = st.number_input(
        "Select quantity:", min_value=1, max_value=20, value=2
    )

    pricing = {
        "Student / Senior": 150,
        "Standard Experience": 250,
        "IMAX 3D Luxe": 420,
        "Private Lounge": 600
    }

    if st.button("Calculate Total Cost"):
        final_cost = quantity * pricing[category]
        st.success(f"Total Amount: {final_cost:,} EGP")

st.markdown("---")

st.markdown("### 💳 Ticket Pricing & Packages")

box1, box2, box3, box4 = st.columns(4)

with box1:
    st.markdown("#### Student / Senior")
    st.markdown("<p style='font-size: 18px; font-weight: bold; color: #4CAF50;'>150 EGP</p>", unsafe_allow_html=True)
    st.caption("Valid ID required at entry")

with box2:
    st.markdown("#### Standard")
    st.markdown("<p style='font-size: 18px; font-weight: bold; color: #2196F3;'>250 EGP</p>", unsafe_allow_html=True)
    st.caption("Standard seating & audio")

with box3:
    st.markdown("#### IMAX 3D Luxe")
    st.markdown("<p style='font-size: 18px; font-weight: bold; color: #9C27B0;'>420 EGP</p>", unsafe_allow_html=True)
    st.caption("Includes 3D glasses & recliners")

with box4:
    st.markdown("#### Private Lounge")
    st.markdown("<p style='font-size: 18px; font-weight: bold; color: #FF9800;'>600 EGP</p>", unsafe_allow_html=True)
    st.caption("Includes popcorn & refillable drink")