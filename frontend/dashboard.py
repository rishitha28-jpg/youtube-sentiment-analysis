# import streamlit as st
# import requests
# import pandas as pd
# import matplotlib.pyplot as plt

# # Chart style
# plt.style.use("ggplot")

# # Backend API
# API_URL = "http://127.0.0.1:8000/api/v1/analyze/"

# # Page config
# st.set_page_config(
#     page_title="YouTube Sentiment Analysis",
#     layout="wide"
# )

# # Title
# st.title("📊 YouTube Comment Sentiment Analysis Dashboard")
# st.write("Analyze YouTube comments using HuggingFace NLP sentiment model")

# # Input
# video_id = st.text_input("Enter YouTube Video ID")

# # Analyze button
# if st.button("Analyze"):

#     if not video_id:
#         st.warning("Please enter a YouTube Video ID")
#         st.stop()

#     with st.spinner("Fetching comments and analyzing sentiment..."):

#         try:
#             response = requests.get(API_URL + video_id)

#             if response.status_code != 200:
#                 st.error("Backend API returned an error.")
#                 st.stop()

#             data = response.json()

#             if "results" not in data:
#                 st.error("Invalid API response.")
#                 st.stop()

#             results = data["results"]

#         except Exception as e:
#             st.error("Error connecting to backend API.")
#             st.write(e)
#             st.stop()

#     # Convert to dataframe
#     df = pd.DataFrame(results)

#     if df.empty:
#         st.warning("No comments found.")
#         st.stop()

#     # --------------------------------------------------
#     # Comment Table
#     # --------------------------------------------------

#     st.subheader("📝 Comment Sentiment Results")
#     st.dataframe(df, width="stretch")

#     # --------------------------------------------------
#     # Sentiment Counts
#     # --------------------------------------------------

#     sentiment_counts = df["sentiment"].value_counts()

#     positive = sentiment_counts.get("POSITIVE", 0)
#     negative = sentiment_counts.get("NEGATIVE", 0)
#     neutral = sentiment_counts.get("NEUTRAL", 0)

#     total = len(df)

#     # --------------------------------------------------
#     # Metrics
#     # --------------------------------------------------

#     st.subheader("📈 Summary Metrics")

#     col1, col2, col3, col4 = st.columns(4)

#     col1.metric("Total Comments", total)
#     col2.metric("Positive", positive)
#     col3.metric("Negative", negative)
#     col4.metric("Neutral", neutral)

#     # --------------------------------------------------
#     # Sentiment Percentage Chart
#     # --------------------------------------------------

#     if total > 0:

#         pos_percent = round((positive / total) * 100, 2)
#         neg_percent = round((negative / total) * 100, 2)
#         neu_percent = round((neutral / total) * 100, 2)

#         percentage_df = pd.DataFrame({
#             "Sentiment": ["Positive", "Negative", "Neutral"],
#             "Percentage": [pos_percent, neg_percent, neu_percent]
#         })

#         st.subheader("📊 Sentiment Percentage")

#         fig_percent, ax_percent = plt.subplots(figsize=(4,3))

#         ax_percent.bar(
#             percentage_df["Sentiment"],
#             percentage_df["Percentage"],
#             width=0.4
#         )

#         ax_percent.set_ylabel("Percentage (%)")
#         ax_percent.set_title("Sentiment %")

#         st.pyplot(fig_percent, use_container_width=False)

#     # --------------------------------------------------
#     # Distribution Charts
#     # --------------------------------------------------

#     st.subheader("📊 Sentiment Distribution")

#     col1, col2 = st.columns(2)

#     # Bar Chart
#     with col1:

#         fig_bar, ax_bar = plt.subplots(figsize=(5,4))

#         ax_bar.bar(
#             sentiment_counts.index,
#             sentiment_counts.values
#         )

#         ax_bar.set_title("Sentiment Count")
#         ax_bar.set_xlabel("Sentiment")
#         ax_bar.set_ylabel("Number of Comments")

#         st.pyplot(fig_bar)

#     # Pie Chart
#     with col2:

#         fig_pie, ax_pie = plt.subplots(figsize=(5,4))

#         ax_pie.pie(
#             sentiment_counts,
#             labels=sentiment_counts.index,
#             autopct="%1.1f%%",
#             startangle=90
#         )

#         ax_pie.set_title("Sentiment Percentage")
#         ax_pie.axis("equal")

#         st.pyplot(fig_pie)

#     # --------------------------------------------------
#     # Top Positive Comments
#     # --------------------------------------------------

#     st.subheader("⭐ Top Positive Comments")

#     pos_comments = df[df["sentiment"] == "POSITIVE"]["comment"].head(5)

#     if not pos_comments.empty:
#         for c in pos_comments:
#             st.success(c)
#     else:
#         st.write("No positive comments found.")

#     # --------------------------------------------------
#     # Top Negative Comments
#     # --------------------------------------------------

#     st.subheader("⚠️ Top Negative Comments")

#     neg_comments = df[df["sentiment"] == "NEGATIVE"]["comment"].head(5)

#     if not neg_comments.empty:
#         for c in neg_comments:
#             st.error(c)
#     else:
#         st.write("No negative comments found.")
import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Chart style
plt.style.use("ggplot")

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

    # Convert to dataframe
    df = pd.DataFrame(results)

    if df.empty:
        st.warning("No comments found.")
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
    # Overall Video Sentiment
    # --------------------------------------------------

    st.subheader("🎯 Overall Video Sentiment")

    if positive > negative:
        overall = "POSITIVE"
    elif negative > positive:
        overall = "NEGATIVE"
    else:
        overall = "NEUTRAL"

    st.success(f"Overall Sentiment: {overall}")

    # --------------------------------------------------
    # Sentiment Percentage Chart
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

        fig_percent, ax_percent = plt.subplots(figsize=(4,3))

        ax_percent.bar(
            percentage_df["Sentiment"],
            percentage_df["Percentage"],
            width=0.4
        )

        ax_percent.set_ylabel("Percentage (%)")
        ax_percent.set_title("Sentiment %")

        st.pyplot(fig_percent, use_container_width=False)

    # --------------------------------------------------
    # Distribution Charts
    # --------------------------------------------------

    st.subheader("📊 Sentiment Distribution")

    col1, col2 = st.columns(2)

    # Bar Chart
    with col1:

        fig_bar, ax_bar = plt.subplots(figsize=(5,4))

        ax_bar.bar(
            sentiment_counts.index,
            sentiment_counts.values
        )

        ax_bar.set_title("Sentiment Count")
        ax_bar.set_xlabel("Sentiment")
        ax_bar.set_ylabel("Number of Comments")

        st.pyplot(fig_bar)

    # Pie Chart
    with col2:

        fig_pie, ax_pie = plt.subplots(figsize=(5,4))

        ax_pie.pie(
            sentiment_counts,
            labels=sentiment_counts.index,
            autopct="%1.1f%%",
            startangle=90
        )

        ax_pie.set_title("Sentiment Percentage")
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