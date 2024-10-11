import streamlit as st

# set the page config info
st.set_page_config(
    page_title="Chat with Hidayah",
    page_icon="🌙")

# welcome message
st.title("Hi, welcome to [Hidayah](https://hidayahlgbt.com). We are a volunteer-led organisation with a mission to provide support and welfare for LGBTQ+ Muslims across the US and UK.")

# Extension for future: "You always go to the [chatgpt bot](https://chatgpt.com/g/g-nC9Kkvdgo-rainbow-rafiq) as well!"

with st.chat_message("user"):
    st.write("Hello 👋 Where are you currently based?")
    uk = st.button("1. UK")
    us = st.button("2. US")
    international = st.button("3. International")

# set button counters - do not touch this code
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
if 'donate_count' not in st.session_state:
    st.session_state.donate_count = 0
if 'video_count' not in st.session_state:
    st.session_state.video_count = 0
if 'podcast_count' not in st.session_state:
    st.session_state.podcast_count = 0
if 'book_count' not in st.session_state:
    st.session_state.book_count = 0
if 'help_count' not in st.session_state:
    st.session_state.help_count = 0
if 'revert_count' not in st.session_state:
    st.session_state.revert_count = 0

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

def donate_counter():
    st.session_state.donate_count += 1

def video_counter():
    st.session_state.video_count += 1

def podcast_counter():
    st.session_state.podcast_count += 1

def book_counter():
    st.session_state.book_count += 1

def help_counter():
    st.session_state.help_count += 1

def revert_counter():
    st.session_state.revert_count += 1

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
            st.button("Make a donation", on_click=donate_counter)
        with c2:
            st.button("Events", on_click=events_counter)
            st.button("Volunteering", on_click=volunteer_counter)
            st.button("Mentoring", on_click=mentor_counter)
            st.button("Something else", on_click=resources_counter)

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
    st.write("Unfortunately we are currently based in the US and UK. Please see our international resources list [here](https://hidayahlgbt.com/international-resources/).  If you would like to make a donation, please select UK or US above. Thank you.")

# define the resource set of options
def resource_options():
    with st.chat_message("user"):
        st.write("What type of resources are you looking for?")
        c1, c2 = st.columns(2)
        with c1:
            st.button("History of Homosexuality in Islam", on_click=video_counter)
            st.button("Books and Academic Journals", on_click=book_counter)
            st.button("Helplines", on_click=help_counter)
        with c2:
            st.button("Listen to a Podcast", on_click=podcast_counter)
            st.button("LGBTQ+ Muslim Revert FAQs", on_click=revert_counter)
            st.button("Other", on_click=contact_counter)

# if the user picks resources
if st.session_state.resources_count==1:
    st.session_state.resources_count = 0 # reset it to zero
    help_options()
    resource_options()
    # with st.chat_message("user"):
    #     st.write("Check out our wellbeing hub [here](https://hidayahlgbt.com/wellbeing/).")

# if the user picks about
if st.session_state.about_count==1:
    st.session_state.about_count = 0 # reset it to zero
    help_options()
    if st.session_state.uk_count == 1:
        with st.chat_message("user"):
            st.write("Hidayah was founded in 2017 in the United Kingdom and in 2020, branched out to the United States. Hidayah means guidance in Arabic and our mission is to provide support and welfare for LGBTQ+ Muslims while promoting social justice and education about our community to counter discrimination, prejudice and injustice. You can learn more about Hidayah UK [here](https://hidayahlgbt.com/about-hidayah-uk/).")
    if st.session_state.us_count == 1:
        with st.chat_message("user"):
            st.write("Hidayah was founded in 2017 in the United Kingdom and in 2020, branched out to the United States. Hidayah means guidance in Arabic and our mission is to provide support and welfare for LGBTQ+ Muslims while promoting social justice and education about our community to counter discrimination, prejudice and injustice. You can learn more about Hidayah US [here](https://hidayahlgbt.com/about-hidayah-us/).")

# if the user picks member
if st.session_state.member_count==1:
    st.session_state.member_count = 0 # reset it to zero
    help_options()
    with st.chat_message("user"):
        st.write("Hidayah proudly presents our Hidayah Membership Program: fostering connections among queer Muslims worldwide in a secure virtual space. [Sign up](https://hidayahlgbt.beaconforms.com/form/fdfb65f0) as a member for free today! Learn more about membership [here](https://hidayahlgbt.com/membership/).")

# if the user picks donate
if st.session_state.donate_count==1:
    st.session_state.donate_count = 0 # reset it to zero
    help_options()
    if st.session_state.uk_count == 1:
        with st.chat_message("user"):
            st.write("Your donations help us provide support for LGBTQ+ Muslims while promoting social justice and education about our community to counter discrimination, prejudice and injustice. Thank you for being a pillar of Hidayah UK's continued success, please see donation link [here](https://donorbox.org/hidayahlgbtdonation?utm_source=website&utm_medium=banner).")
    if st.session_state.us_count == 1:
        with st.chat_message("user"):
            st.write("Your donations help us provide support for LGBTQ+ Muslims while promoting social justice and education about our community to counter discrimination, prejudice and injustice. Thank you for being a pillar of support for Hidayah US, please see donation link [here](https://www.zeffy.com/en-US/donation-form/8abb2e69-e001-4a85-908e-822511c4fbfc).")

# if the user picks events
if st.session_state.events_count==1:
    st.session_state.events_count = 0 # reset it to zero
    help_options()
    with st.chat_message("user"):
        st.write("Check out our upcoming events [here](https://hidayahlgbt.com/event-calendar/list/).")

# if the user picks volunteer
if st.session_state.volunteer_count==1:
    st.session_state.volunteer_count = 0 # reset it to zero
    help_options()
    if st.session_state.uk_count == 1:
        with st.chat_message("user"):
            st.write("We offer a range of volunteering opportunities and we want to hear from you! Please email Hidayah UK directly [here](mailto:hr@hidayahlgbt.co.uk).")
    if st.session_state.us_count == 1:
        with st.chat_message("user"):
            st.write("We offer a range of volunteering opportunities and we want to hear from you! Please email Hidayah US directly [here](mailto:info@hidayahlgbt.com).")

# if the user picks mentor
if st.session_state.mentor_count==1:
    st.session_state.mentor_count = 0 # reset it to zero
    help_options()
    if st.session_state.uk_count == 1:
        with st.chat_message("user"):
            st.write("Apply to be a Hidayah UK mentor / mentee [here](https://hidayahlgbt.com/al-naasih/).")
    if st.session_state.us_count == 1:
        with st.chat_message("user"):
            st.write("For future mentoring opportunities, please email Hidayah US directly [here](mailto:info@hidayahlgbt.com).")

# if the user picks video
if st.session_state.video_count==1:
    st.session_state.video_count = 0 # reset it to zero
    help_options()
    resource_options()
    with st.chat_message("user"):
            st.write("Islamic history has a rich tradition of homosexuality being expressed through stories and poetry. Check out this vide on [Homosexuality in the Islamic World](https://youtu.be/mQ3Z7Qcv2N8?si=hhoJ3RDzbSk6bG0I) or click [here](https://hidayahlgbt.com/media/) for Hidayah's media hub.")

# if the user picks book
if st.session_state.book_count==1:
    st.session_state.book_count = 0 # reset it to zero
    help_options()
    resource_options()
    with st.chat_message("user"):
            st.write("Check out our curated list of [books](https://hidayahlgbt.com/books/) and [academic journals](https://hidayahlgbt.com/journal-articles/). We also have a Hidayah blog you can read [here](https://hidayahlgbt.com/blog/).")

# if the user picks help
if st.session_state.help_count==1:
    st.session_state.help_count = 0 # reset it to zero
    help_options()
    resource_options()
    if st.session_state.uk_count == 1:
        with st.chat_message("user"):
            st.write("[Switchboard](https://switchboard.lgbt/) is the national LGBTQIA+ support line for anyone, anywhere in the country, at any point in their journey: [IM](https://switchboard.lgbt/) or call 0800 0119 100. Please see [here](https://hidayahlgbt.com/resource-list/) for a comprehensive list of helplines and organisations or [email](mailto:hello@hidayahlgbt.co.uk) Hidayah UK directly.")
    if st.session_state.us_count == 1:
        with st.chat_message("user"):
            st.write("The [LGBT National Help Center](https://lgbthotline.org/) provides free & confidential peer-support, information, and local resources through online programs and national hotlines: [chat online](https://lgbthotline.org/chat/) or call 888-843-4564. Please see [here](https://hidayahlgbt.com/resource-list/) for a comprehensive list of helplines and organisations or [email](mailto:info@hidayahlgbt.com) Hidayah US directly.")

# if the user picks podcast
if st.session_state.podcast_count==1:
    st.session_state.podcast_count = 0 # reset it to zero
    help_options()
    resource_options()
    with st.chat_message("user"):
            st.write("Listen to Hidayah’s very own podcast [here](https://hidayahlgbt.com/podcast/) to hear about stories shared by other queer Muslims.")

# if the user picks revert
if st.session_state.revert_count==1:
    st.session_state.revert_count = 0 # reset it to zero
    help_options()
    resource_options()
    with st.chat_message("user"):
            st.write("Welcome to the community! Access our revert toolkit [here](https://docs.google.com/document/d/10GDFxA8PYjUac_m793kMruMte2NfaB9TFZycNwrWkow/edit?usp=sharing)")

# if the user picks other
if st.session_state.contact_count==1:
    st.session_state.contact_count = 0 # reset it to zero
    help_options()
    resource_options()
    if st.session_state.uk_count == 1:
        with st.chat_message("user"):
            st.write("Please see our full resource list [here](https://hidayahlgbt.com/wellbeing/) or [email](mailto:hello@hidayahlgbt.co.uk) Hidayah UK directly.")
    if st.session_state.us_count == 1:
        with st.chat_message("user"):
            st.write("Please see our full resource list [here](https://hidayahlgbt.com/wellbeing/). You are welcome to chat with [Rainbow Rafiq](https://chatgpt.com/g/g-nC9Kkvdgo-rainbow-rafiq) or please [email](mailto:info@hidayahlgbt.com) Hidayah US directly.")


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
