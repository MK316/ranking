import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data for the DataFrame
data = {
    "Name": ["SS Park", "Bob", "Charlie", "David", "Eve"],
    "Score": [100, 75, 92, 70, 65],
    "Time": ["24.11.11", "24.11.10", "24.11.12", "24.11.10", "24.10.31"]
}

# Create a DataFrame
df = pd.DataFrame(data)

def main():
    st.title("IPA King/Queen")
    st.caption("Since Nov 11, 2024")

    # Creating tabs
    tab1, tab2 = st.tabs(["IPA records", "Top Rank"])

    # Tab 1: Show the DataFrame
    with tab1:
        st.write("Here is the record:")
        st.dataframe(df)

    # Tab 2: Show the bar plot sorted by Scores with hexadecimal color differentiation
    with tab2:
        st.write("Top Scores (asof Nov. 11, 2024)")
        st.caption("My students submit their highest scores after practicing with the IPA practice app. The following is the high scores achieved with no mistakes.")
        # Sort the DataFrame by Score in descending order for better visualization
        sorted_df = df.sort_values('Score', ascending=False)
        fig, ax = plt.subplots()
        # Colors for the bars: First bar in a specific color
        colors = ['#66BEFF'] + ['#CCE5FF' for _ in range(len(sorted_df) - 1)]  # Orange for the highest score, light blue for others
        bars = ax.bar(sorted_df['Name'], sorted_df['Score'], color=colors)
        
        # Adding the text inside the bars with the date and heart emoji for the top score
        for i, bar in enumerate(bars):
            yval = bar.get_height()
            date = sorted_df.iloc[i]["Time"]
            if i == 0:
                # Top bar: Add heart emoji and date inside
                ax.text(bar.get_x() + bar.get_width()/2, yval / 2, f"❤️  {date}", ha='center', va='center', color='black', fontsize=8)
            else:
                # Other bars: Add date inside
                ax.text(bar.get_x() + bar.get_width()/2, yval / 2, date, ha='center', va='center', color='black', fontsize=8)
            # Display score above each bar
            ax.text(bar.get_x() + bar.get_width()/2, yval - 5, round(yval, 1), ha='center', va='bottom', color='black')

        ax.set_ylabel("Score")
        ax.set_xlabel("Name")
        ax.set_title("Top Scores")
        st.pyplot(fig)

if __name__ == "__main__":
    main()
