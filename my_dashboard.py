import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = "Reading List",
    page_icon = "📚",
    layout = "wide"
)

st.title("Reading List Dashboard")

# Books (I love reading YA and/or fictional novels so chose these books for this)

BOOKS = pd.DataFrame({
    "Title": ["Six of Crows", "The Hunger Games", "A Good Girl's Guide to Murder",
              "The Fault in Our Stars", "Divergent", "Fourth Wing", "We Were Liars",
              "The Cruel Prince", "Red, White & Royal Blue", "Legendborn"],
    "Author": ["Leigh Bardugo", "Suzanne Collins", "Holly Jackson",
               "John Green", "Veronica Roth", "Rebecca Yarros", "E. Lockhart",
               "Holly Black", "Casey McQuiston", "Tracy Deonn"],
    "Genre": ["Fantasy", "Dystopian", "Mystery", "Contemporary", "Dystopian",
              "Fantasy", "Mystery", "Fantasy", "Romance", "Fantasy"],
    "Pages": [465, 374, 400, 313, 487, 517, 242, 370, 421, 501],
    "Rating": [5, 5, 4, 3, 3, 4, None, None, None, None],
    "Status": ["Finished", "Finished", "Finished", "Finished", "Finished",
               "Finished", "Reading", "To Read", "To Read", "To Read"],
})

LAST_YEAR_AVG_RATING = 3.8

# Sidebar controls
st.sidebar.header("Filters")

genre = st.sidebar.selectbox(
    "Genre", ["All", "Fantasy", "Dystopian", "Mystery", "Contemporary", "Romance"]
)
yearly_goal = st.sidebar.slider("Yearly reading goal (books)", 5, 50, 12)
show_to_read = st.sidebar.checkbox("Include 'To Read' books", value=True)

# Apply filters
view = BOOKS if genre == "All" else BOOKS[BOOKS["Genre"] == genre]
if not show_to_read:
    view = view[view["Status"] != "To Read"]

finished = view[view["Status"] == "Finished"]

books_done = len(finished)
pages_read = finished["Pages"].sum()

# Display yearly goal progress
st.sidebar.header("Progress")
st.sidebar.metric("Books Finished", books_done, delta=f"{books_done - yearly_goal} from goal")

col1, col2, col3 = st.columns(3)

col1.metric("Books Finished", books_done, delta="+2 this month")
col2.metric("Pages Read", f"{pages_read:,}", delta="+748 this month")

if books_done:
    avg_rating = finished["Rating"].mean()
    col3.metric(
        "Avg Rating",
        f"{avg_rating:.1f} ⭐",
        delta=round(avg_rating - LAST_YEAR_AVG_RATING, 1),
    )
else:
    col3.metric("Avg Rating", "—")

st.divider()

tab1, tab2 = st.tabs(["📊 Overview", "📋 Details"])

with tab1:
    st.subheader("Pages Read by Genre")
    if books_done:
        st.bar_chart(finished.groupby("Genre")["Pages"].sum())
    else:
        st.info("No finished books in this genre yet.")

    st.subheader("Yearly Goal")
    st.progress(
        min(books_done / yearly_goal, 1.0),
        text=f"{books_done} of {yearly_goal} books",
    )

with tab2:
    st.subheader("Full Book List")
    st.dataframe(view, hide_index=True)

with st.expander("ℹ️ About this dashboard"):
    st.write("""
    - **Genre** filters the metrics, chart, and book list.
    - **Yearly goal** updates the progress bar and the sidebar progress metric.
    - **Include 'To Read' books** shows or hides books I haven't started yet.
    - **Avg Rating** delta compares to last year's average (3.8).
    - Ratings are only given to finished books. All data is hardcoded.
    """)