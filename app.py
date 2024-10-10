import streamlit as st

# welcome message
st.title("Hi, welcome to [Hidayah](https://hidayahlgbt.com). We are a volunteer-led organisation with a mission to provide support and welfare for LGBTQ+ Muslims across the US and UK.")

# Extension for future: "You always go to the [chatgpt bot](https://chatgpt.com/g/g-nC9Kkvdgo-rainbow-rafiq) as well!"

with st.chat_message("user"):
    st.write("Hello 👋 Where are you currently based?")
    uk = st.button("1. UK")
    us = st.button("2. US")
    international = st.button("3. International")

 # set initial button counters - do not touch this code
if 'about_count' not in st.session_state:
    st.session_state.about_count = 0
if 'member_count' not in st.session_state:
    st.session_state.member_count = 0
if 'events_count' not in st.session_state:
    st.session_state.events_count = 0
if 'resources_count' not in st.session_state:
    st.session_state.resources_count = 0
if 'volunteer_count' not in st.session_state:
    st.session_state.volunteer_count = 0
if 'mentor_count' not in st.session_state:
    st.session_state.mentor_count = 0
if 'contact_count' not in st.session_state:
    st.session_state.contact_count = 0
if 'us_count' not in st.session_state:
    st.session_state.us_count = 0
if 'uk_count' not in st.session_state:
    st.session_state.uk_count = 0

def about_counter():
    st.session_state.about_count += 1

def member_counter():
    st.session_state.member_count += 1

def events_counter():
    st.session_state.events_count += 1

def resources_counter():
    st.session_state.resources_count += 1

def volunteer_counter():
    st.session_state.volunteer_count += 1

def mentor_counter():
    st.session_state.mentor_count += 1

def contact_counter():
    st.session_state.contact_count += 1

def uk_counter():
    st.session_state.uk_count = 1

def us_counter():
    st.session_state.us_count = 1


# define the initial help set of options
def help_options():
    with st.chat_message("user"):
        st.write("How can we help you today?")
        c1, c2 = st.columns(2)
        with c1:
            st.button("Learn about Hidayah", on_click=about_counter)
            st.button("Membership", on_click=member_counter)
            st.button("Resources for wellbeing", on_click=resources_counter)
        with c2:
            st.button("Events", on_click=events_counter)
            st.button("Volunteering", on_click=volunteer_counter)
            st.button("Mentoring", on_click=mentor_counter)
            st.button("Something else", on_click=contact_counter)


# what the user should see when they click on the first set of options
if us:
    us_counter()
    st.session_state.uk_count = 0
    help_options()
elif uk:
    uk_counter()
    st.session_state.us_count = 0
    help_options()
elif international:
    st.write("Unfortunately we are currently based in the US and UK. Please see our international resource list [here](https://hidayahlgbt.com/international-resources/).")

# if st.session_state.uk_count == 1:
#     st.write("test")


# if the user picks about
if st.session_state.about_count==1:
    st.session_state.about_count = 0 # reset it to zero
    help_options()
    if st.session_state.uk_count == 1:
        with st.chat_message("user"):
            st.write("You can learn more about Hidayah UK [here]()")

            text = """X<br>
            Y<br>
            Z<br>
            <br>Profile
            """

#         st.write(f'<p style="font-size: 14px; color:grey">{text}</p>',
#                  unsafe_allow_html=True)
#
# # if the user picks blogs
# if st.session_state.blogs_count==1:
#     st.session_state.blogs_count = 0 # reset it to zero
#     resource_options()
#     with st.chat_message("user"):
#         st.write("Blog resources")
#
#         text = """X<br>
#             Y<br>
#             Z<br>
#             <br>Profile
#             """
#
#         st.write(f'<p style="font-size: 14px; color:grey">{text}</p>',
#                  unsafe_allow_html=True)
#
# # if the user picks podcasts
# if st.session_state.podcast_count ==1:
#     st.session_state.podcast_count = 0 # reset it to zero
#     resource_options()
#     with st.chat_message("user"):
#         st.write("Podcast resources")
#
#         text = """X<br>
#                Y<br>
#                Z<br>
#                <br>Profile
#                """
#
#         st.write(f'<p style="font-size: 14px; color:grey">{text}</p>',
#                  unsafe_allow_html=True)
#
# # if the user picks organisation
# if st.session_state.org_count ==1:
#     st.session_state.org_count = 0 # reset it to zero
#     resource_options()
#     with st.chat_message("user"):
#         st.write("Organisation resources")
#
#         text = """X<br>
#                Y<br>
#                Z<br>
#                <br>Profile
#                """
#
#         st.write(f'<p style="font-size: 14px; color:grey">{text}</p>',
#                  unsafe_allow_html=True)



# # set initial button counters - do not touch this code
# if 'video_count' not in st.session_state:
#     st.session_state.video_count = 0
# if 'podcast_count' not in st.session_state:
#     st.session_state.podcast_count = 0
# if 'blogs_count' not in st.session_state:
#     st.session_state.blogs_count = 0
# if 'org_count' not in st.session_state:
#     st.session_state.org_count = 0
#
# def video_counter():
#     st.session_state.video_count += 1
#
# def podcast_counter():
#     st.session_state.podcast_count += 1
#
# def blogs_counter():
#     st.session_state.blogs_count += 1
#
# def org_counter():
#     st.session_state.org_count += 1

# define the resource set of options
# def resource_options():
#     with st.chat_message("user"):
#         st.write("What type of resources are you looking for?")
#
#         c1, c2 = st.columns(2)
#
#         with c1:
#             st.button("🎥 Videos", on_click=video_counter)
#             st.button("Podcasts", on_click=podcast_counter)
#         with c2:
#             st.button("Blogs", on_click=blogs_counter)
#             st.button("Organisation", on_click=org_counter)



# if the user picks video
# if st.session_state.video_count==1:
#     st.session_state.video_count = 0 # reset it to zero
#     resource_options()
#
#     with st.chat_message("user"):
#         st.write("Video resources")
#
#         text = """X<br>
#         Y<br>
#         Z<br>
#         <br>Profile
#         """
#
#         st.write(f'<p style="font-size: 14px; color:grey">{text}</p>',
#                  unsafe_allow_html=True)
#
# # if the user picks blogs
# if st.session_state.blogs_count==1:
#     st.session_state.blogs_count = 0 # reset it to zero
#     resource_options()
#     with st.chat_message("user"):
#         st.write("Blog resources")
#
#         text = """X<br>
#             Y<br>
#             Z<br>
#             <br>Profile
#             """
#
#         st.write(f'<p style="font-size: 14px; color:grey">{text}</p>',
#                  unsafe_allow_html=True)
#
# # if the user picks podcasts
# if st.session_state.podcast_count ==1:
#     st.session_state.podcast_count = 0 # reset it to zero
#     resource_options()
#     with st.chat_message("user"):
#         st.write("Podcast resources")
#
#         text = """X<br>
#                Y<br>
#                Z<br>
#                <br>Profile
#                """
#
#         st.write(f'<p style="font-size: 14px; color:grey">{text}</p>',
#                  unsafe_allow_html=True)
#
# # if the user picks organisation
# if st.session_state.org_count ==1:
#     st.session_state.org_count = 0 # reset it to zero
#     resource_options()
#     with st.chat_message("user"):
#         st.write("Organisation resources")
#
#         text = """X<br>
#                Y<br>
#                Z<br>
#                <br>Profile
#                """
#
#         st.write(f'<p style="font-size: 14px; color:grey">{text}</p>',
#                  unsafe_allow_html=True)
