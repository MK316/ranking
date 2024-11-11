import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data for the DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Score": [100, 75, 92, 70, 65],
    "Time": ["24.11.11", "24.11.10", "24.11.12", "24.11.10", "24.10.31"]
}

# Create a DataFrame
df = pd.DataFrame(data)

def main():
    st.title("IPA King/Queen (since Nov 11, 2024)")

    # Creating tabs
    tab1, tab2 = st.tabs(["IPA records", "Bar Plot"])

    # Tab 1: Show the DataFrame
    with tab1:
        st.write("Here is the DataFrame:")
        st.dataframe(df)

    # Tab 2: Show the bar plot sorted by Scores with hexadecimal color differentiation
    with tab2:
        st.write("Bar plot of Scores sorted by values")
        # Sort the DataFrame by Score in descending order for better visualization
        sorted_df = df.sort_values('Score', ascending=False)
        fig, ax = plt.subplots()
        # Colors for the bars: First bar in a specific color
        colors = ['#FF8000'] + ['#CCE5FF' for _ in range(len(sorted_df) - 1)]  # Gold for the highest score, blue for others
        bars = ax.bar(sorted_df['Name'], sorted_df['Score'], color=colors)
        # Adding the text inside the bars
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval - 5, round(yval, 1), ha='center', va='bottom', color='black')
        
        ax.set_ylabel("Score")
        ax.set_xlabel("Name")
        ax.set_title("Scores by Name Sorted")
        st.pyplot(fig)

if __name__ == "__main__":
    main()
