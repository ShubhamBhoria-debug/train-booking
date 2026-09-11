import streamlit as st

# 1. Session State Initialization (Yeh check karega ki pehle se variables bane hain ya nahi)
if 'count_con' not in st.session_state:
    st.session_state.count_con = 0
if 'count_bjp' not in st.session_state:
    st.session_state.count_bjp = 0
if 'count_aap' not in st.session_state:
    st.session_state.count_aap = 0
if 'count_cjp' not in st.session_state:
    st.session_state.count_cjp = 0

st.title("Voting Poll")

# Instructions

with st.expander("Voting Instruction"):
    st.write("""
    1. First verify your documents for voting\n
    2. First see the voting machine clearly so that any kind of confusion are not created\n
    3. Vote wisely
    """)

# Sidebar Inputs
name = st.sidebar.text_input("Enter your name:")
if name:
    st.write(f"Welcome **{name}** for voting!")

dob = st.sidebar.date_input("Enter your DOB")

# Voting Columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.header("Congress")
    st.image("https://dm0qx8t0i9gc9.cloudfront.net/thumbnails/video/rMadI-Zz9l0vd44f0/videoblocks-indian-national-congress-political-party-logo-india-election-waving-flag_hjavpzpq0_thumbnail-1080_10.png", width=150)
    vote1 = st.button("Vote Congress")
     
with col2:
    st.header("BJP")
    st.image("https://tse2.mm.bing.net/th/id/OIP.P2ZuUln6_ACC2qSEBP90WwHaFj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3", width=150)
    vote2 = st.button("Vote BJP")
     
with col3:
    st.header("AAP")
    st.image("https://5.imimg.com/data5/SELLER/Default/2024/11/466136376/NL/ZF/DI/15580937/aam-aadmi-party-flag-satin-1000x1000.jpg", width=150)
    vote3 = st.button("Vote AAP")
     
with col4:
    st.header("CJP")
    st.image("https://www.bing.com/th/id/OIP._dPg5j5Rl41z3yvcrLpNSAHaHa?w=193&h=193&c=8&rs=1&qlt=90&o=6&dpr=1.4&pid=ImgAns&rm=2", width=150)
    vote4 = st.button("Vote CJP")

# Vote Logic & Success Messages
if vote1:
    st.session_state.count_con += 1
    st.success("Thank you for voting! Your vote for Congress is added successfully.")
    
elif vote2:
    st.session_state.count_bjp += 1
    st.success("Thank you for voting! Your vote for BJP is added successfully.")

elif vote3:
    st.session_state.count_aap += 1
    st.success("Thank you for voting! Your vote for AAP is added successfully.")

elif vote4:
    st.session_state.count_cjp += 1
    st.success("Thank you for voting! Your vote for CJP is added successfully.")


st.markdown("---")
st.subheader("📊 Live Voting Results Tracker")

# Metrics  kan use krna pde ga taaki live scores alag dikhein
r_col1,r_col2,r_col3,r_col4=st.columns(4)

with r_col1:
    st.metric("Congress", st.session_state.count_con)
with r_col2:
    st.metric("BJP", st.session_state.count_bjp)
with r_col3:
    st.metric("AAP", st.session_state.count_aap)
with r_col4:
    st.metric("CJP", st.session_state.count_cjp)

# Graphical View (Optional)
vote_data = {
    "Congress": st.session_state.count_con,
    "BJP": st.session_state.count_bjp,
    "AAP": st.session_state.count_aap,
    "CJP": st.session_state.count_cjp
}
st.bar_chart(vote_data)