import streamlit as st

st.title("Hi, Welcome to Hadiyah(). We are a voluntary organisation XXXX")

with st.chat_message("user"):
    st.write("Hello 👋 Are you based in the UK or US")
    uk = st.button("1. UK")
    us = st.button("2. US")
    international = st.button("3. International")

# set button counters
if 'video_count' not in st.session_state:
    st.session_state.video_count = 0
if 'podcast_count' not in st.session_state:
    st.session_state.podcast_count = 0
if 'blogs_count' not in st.session_state:
    st.session_state.blogs_count = 0
if 'org_count' not in st.session_state:
    st.session_state.org_count = 0

def video_counter():
    st.session_state.video_count += 1

def podcast_counter():
    st.session_state.podcast_count += 1

def blogs_counter():
    st.session_state.blogs_count += 1

def org_counter():
    st.session_state.org_count += 1

def first_set_options():
    with st.chat_message("user"):
        st.write("What type of resources are you looking for?")

        c1, c2 = st.columns(2)

        with c1:
            st.button("🎥 Videos", on_click=video_counter)
            st.button("Podcasts", on_click=podcast_counter)
        with c2:
            st.button("Blogs", on_click=blogs_counter)
            st.button("Organisation", on_click=org_counter)


if international:
    st.write("Unfortunately we do not provide this info")
elif uk or us:
    first_set_options()


if st.session_state.video_count==1:
    st.session_state.video_count = 0 # reset it to zero
    first_set_options()

    with st.chat_message("user"):
        st.write("Video resources")

        text = """X<br>   
        Y<br>  
        Z<br>
        <br>Profile
        """

        st.write(f'<p style="font-size: 14px; color:grey">{text}</p>',
                 unsafe_allow_html=True)

if st.session_state.blogs_count==1:
    st.session_state.blogs_count = 0 # reset it to zero
    first_set_options()
    with st.chat_message("user"):
        st.write("Blog resources")

        text = """X<br>   
            Y<br>  
            Z<br>
            <br>Profile
            """

        st.write(f'<p style="font-size: 14px; color:grey">{text}</p>',
                 unsafe_allow_html=True)

if st.session_state.podcast_count ==1:
    st.session_state.podcast_count = 0 # reset it to zero
    first_set_options()
    with st.chat_message("user"):
        st.write("Podcast resources")

        text = """X<br>   
               Y<br>  
               Z<br>
               <br>Profile
               """

        st.write(f'<p style="font-size: 14px; color:grey">{text}</p>',
                 unsafe_allow_html=True)

if st.session_state.org_count ==1:
    st.session_state.org_count = 0 # reset it to zero
    first_set_options()
    with st.chat_message("user"):
        st.write("Organisation resources")

        text = """X<br>   
               Y<br>  
               Z<br>
               <br>Profile
               """

        st.write(f'<p style="font-size: 14px; color:grey">{text}</p>',
                 unsafe_allow_html=True)







