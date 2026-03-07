# # # import streamlit as st
# # # import requests
# # # import pandas as pd

# # # API_URL = "http://localhost:8000/api/v1/analyze/"

# # # st.title("YouTube Sentiment Analysis Dashboard")

# # # video_id = st.text_input("Enter YouTube Video ID")

# # # if st.button("Analyze"):

# # #     response = requests.get(API_URL + video_id)

# # #     data = response.json()

# # #     results = data["results"]

# # #     df = pd.DataFrame(results)

# # #     st.write("Sentiment Results")
# # #     st.dataframe(df)

# # #     sentiment_counts = df["sentiment"].value_counts()

# # #     st.bar_chart(sentiment_counts)
# # import streamlit as st
# # import requests
# # import pandas as pd

# # API_URL = "http://localhost:8000/api/v1/analyze/"

# # st.set_page_config(page_title="YouTube Sentiment Analysis", layout="wide")

# # st.title("📊 YouTube Comment Sentiment Analysis")
# # st.write("Analyze sentiment of YouTube comments using HuggingFace NLP")

# # video_id = st.text_input("Enter YouTube Video ID")

# # if st.button("Analyze"):

# #     with st.spinner("Fetching comments and analyzing sentiment..."):

# #         response = requests.get(API_URL + video_id)
# #         data = response.json()
# #         results = data["results"]

# #         df = pd.DataFrame(results)

# #     st.subheader("📝 Comment Sentiment Results")
# #     st.dataframe(df, use_container_width=True)

# #     # Sentiment counts
# #     sentiment_counts = df["sentiment"].value_counts()

# #     st.subheader("📊 Sentiment Distribution")
# #     st.bar_chart(sentiment_counts)

# #     # Summary metrics
# #     total = len(df)
# #     positive = (df["sentiment"] == "POSITIVE").sum()
# #     negative = (df["sentiment"] == "NEGATIVE").sum()

# #     col1, col2, col3 = st.columns(3)

# #     col1.metric("Total Comments", total)
# #     col2.metric("Positive Comments", positive)
# #     col3.metric("Negative Comments", negative)

# #     # Percentages
# #     if total > 0:
# #         pos_percent = round((positive / total) * 100, 2)
# #         neg_percent = round((negative / total) * 100, 2)

# #         st.subheader("📈 Sentiment Percentage")

# #         percentage_df = pd.DataFrame({
# #             "Sentiment": ["Positive", "Negative"],
# #             "Percentage": [pos_percent, neg_percent]
# #         })

# #         st.bar_chart(percentage_df.set_index("Sentiment"))

# #     # Show top positive and negative comments
# #     st.subheader("⭐ Top Positive Comments")
# #     st.write(df[df["sentiment"] == "POSITIVE"]["comment"].head(5))

# #     st.subheader("⚠️ Top Negative Comments")
# #     st.write(df[df["sentiment"] == "NEGATIVE"]["comment"].head(5))
# import streamlit as st
# import requests
# import pandas as pd

# API_URL = "http://127.0.0.1:8000/api/v1/analyze/"

# st.set_page_config(page_title="YouTube Sentiment Analysis", layout="wide")

# st.title("📊 YouTube Comment Sentiment Analysis Dashboard")
# st.write("Analyze YouTube comments using HuggingFace NLP sentiment model")

# video_id = st.text_input("Enter YouTube Video ID")

# if st.button("Analyze"):

#     with st.spinner("Fetching comments and analyzing sentiment..."):

#         try:
#             response = requests.get(API_URL + video_id)
#             data = response.json()

#             results = data["results"]

#         except Exception as e:
#             st.error("Error fetching data from API")
#             st.stop()

#         df = pd.DataFrame(results)

#     # ---------------------------------------------------
#     # Comment Table
#     # ---------------------------------------------------
#     st.subheader("📝 Comment Sentiment Results")
#     st.dataframe(df, use_container_width=True)

#     # ---------------------------------------------------
#     # Sentiment Counts
#     # ---------------------------------------------------
#     sentiment_counts = df["sentiment"].value_counts()

#     positive = sentiment_counts.get("POSITIVE", 0)
#     negative = sentiment_counts.get("NEGATIVE", 0)
#     neutral = sentiment_counts.get("NEUTRAL", 0)

#     total = len(df)

#     # ---------------------------------------------------
#     # Metrics
#     # ---------------------------------------------------
#     st.subheader("📈 Summary Metrics")

#     col1, col2, col3, col4 = st.columns(4)

#     col1.metric("Total Comments", total)
#     col2.metric("Positive", positive)
#     col3.metric("Negative", negative)
#     col4.metric("Neutral", neutral)

#     # ---------------------------------------------------
#     # Percentage Calculation
#     # ---------------------------------------------------
#     if total > 0:

#         pos_percent = round((positive / total) * 100, 2)
#         neg_percent = round((negative / total) * 100, 2)
#         neu_percent = round((neutral / total) * 100, 2)

#         percentage_df = pd.DataFrame({
#             "Sentiment": ["Positive", "Negative", "Neutral"],
#             "Percentage": [pos_percent, neg_percent, neu_percent]
#         })

#         st.subheader("📊 Sentiment Percentage")
#         st.bar_chart(percentage_df.set_index("Sentiment"))

#         st.subheader("🥧 Sentiment Distribution")
#         st.write(percentage_df.set_index("Sentiment"))

#     # ---------------------------------------------------
#     # Distribution Chart
#     # ---------------------------------------------------
#     st.subheader("📊 Sentiment Distribution (Count)")
#     st.bar_chart(sentiment_counts)

#     # ---------------------------------------------------
#     # Top Comments
#     # ---------------------------------------------------
#     st.subheader("⭐ Top Positive Comments")
#     pos_comments = df[df["sentiment"] == "POSITIVE"]["comment"].head(5)

#     if len(pos_comments) > 0:
#         for c in pos_comments:
#             st.success(c)
#     else:
#         st.write("No positive comments found.")

#     st.subheader("⚠️ Top Negative Comments")
#     neg_comments = df[df["sentiment"] == "NEGATIVE"]["comment"].head(5)

#     if len(neg_comments) > 0:
#         for c in neg_comments:
#             st.error(c)
#     else:
#         st.write("No negative comments found.")
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Backend API
API_URL = "http://127.0.0.1:8000/api/v1/analyze/"

# Page config
st.set_page_config(
    page_title="YouTube Sentiment Analysis",
    layout="wide"
)

# Title
st.title("📊 YouTube Comment Sentiment Analysis Dashboard")
st.write("Analyze YouTube comments using HuggingFace NLP sentiment model")

# Input
video_id = st.text_input("Enter YouTube Video ID")

# Analyze button
if st.button("Analyze"):

    if not video_id:
        st.warning("Please enter a YouTube Video ID")
        st.stop()

    with st.spinner("Fetching comments and analyzing sentiment..."):

        try:
            response = requests.get(API_URL + video_id)

            if response.status_code != 200:
                st.error("Backend API returned an error.")
                st.stop()

            data = response.json()

            if "results" not in data:
                st.error("Invalid API response.")
                st.stop()

            results = data["results"]

        except Exception as e:
            st.error("Error connecting to backend API.")
            st.write(e)
            st.stop()

    # Convert to DataFrame
    df = pd.DataFrame(results)

    if df.empty:
        st.warning("No comments found for this video.")
        st.stop()

    # --------------------------------------------------
    # Comment Table
    # --------------------------------------------------
    st.subheader("📝 Comment Sentiment Results")
    st.dataframe(df, width="stretch")

    # --------------------------------------------------
    # Sentiment Counts
    # --------------------------------------------------
    sentiment_counts = df["sentiment"].value_counts()

    positive = sentiment_counts.get("POSITIVE", 0)
    negative = sentiment_counts.get("NEGATIVE", 0)
    neutral = sentiment_counts.get("NEUTRAL", 0)

    total = len(df)

    # --------------------------------------------------
    # Metrics
    # --------------------------------------------------
    st.subheader("📈 Summary Metrics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Comments", total)
    col2.metric("Positive", positive)
    col3.metric("Negative", negative)
    col4.metric("Neutral", neutral)

    # --------------------------------------------------
    # Percentage Chart
    # --------------------------------------------------
    if total > 0:

        pos_percent = round((positive / total) * 100, 2)
        neg_percent = round((negative / total) * 100, 2)
        neu_percent = round((neutral / total) * 100, 2)

        percentage_df = pd.DataFrame({
            "Sentiment": ["Positive", "Negative", "Neutral"],
            "Percentage": [pos_percent, neg_percent, neu_percent]
        })

        st.subheader("📊 Sentiment Percentage")

        fig_percent, ax_percent = plt.subplots(figsize=(6,4))
        ax_percent.bar(
            percentage_df["Sentiment"],
            percentage_df["Percentage"]
        )
        ax_percent.set_ylabel("Percentage (%)")
        ax_percent.set_title("Sentiment Percentage Distribution")

        st.pyplot(fig_percent)

    # --------------------------------------------------
    # Distribution Charts
    # --------------------------------------------------
    col1, col2 = st.columns(2)

    # Bar Chart
    with col1:

        st.subheader("📊 Sentiment Distribution (Count)")

        fig_bar, ax_bar = plt.subplots(figsize=(6,4))

        sentiment_counts.plot(
            kind="bar",
            ax=ax_bar
        )

        ax_bar.set_xlabel("Sentiment")
        ax_bar.set_ylabel("Number of Comments")
        ax_bar.set_title("Comment Sentiment Count")

        st.pyplot(fig_bar)

    # Pie Chart
    with col2:

        st.subheader("🥧 Sentiment Distribution")

        fig_pie, ax_pie = plt.subplots(figsize=(5,5))

        ax_pie.pie(
            sentiment_counts,
            labels=sentiment_counts.index,
            autopct='%1.1f%%',
            startangle=90
        )

        ax_pie.axis("equal")

        st.pyplot(fig_pie)

    # --------------------------------------------------
    # Top Positive Comments
    # --------------------------------------------------
    st.subheader("⭐ Top Positive Comments")

    pos_comments = df[df["sentiment"] == "POSITIVE"]["comment"].head(5)

    if not pos_comments.empty:

        for c in pos_comments:
            st.success(c)

    else:
        st.write("No positive comments found.")

    # --------------------------------------------------
    # Top Negative Comments
    # --------------------------------------------------
    st.subheader("⚠️ Top Negative Comments")

    neg_comments = df[df["sentiment"] == "NEGATIVE"]["comment"].head(5)

    if not neg_comments.empty:

        for c in neg_comments:
            st.error(c)

    else:
        st.write("No negative comments found.")