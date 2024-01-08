import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

# Assuming you want to group by 'TAG' and 'DATE' and sum the 'POSTS'
grouped_df = df.groupby(['TAG', 'DATE']).sum().reset_index()

# Reshape the DataFrame for plotting
reshaped_df = grouped_df.pivot(index='DATE', columns='TAG', values='POSTS')

# Set a stylish seaborn theme
sns.set_theme(style="whitegrid")

# Plotting with enhanced styling
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14, rotation=45, ha='right')
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)

# Plot each column with a different color
palette = sns.color_palette("husl", n_colors=len(reshaped_df.columns))
for i, column in enumerate(reshaped_df.columns):
    plt.plot(reshaped_df.index, reshaped_df[column],
             linewidth=3, label=reshaped_df[column].name, color=palette[i])

# Add a legend with a fancy box
plt.legend(fontsize=16, loc='upper left', bbox_to_anchor=(1, 1))

# Title and grid
plt.title('Number of Posts Over Time by Tag', fontsize=18)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add a background color to the plot
plt.fill_between(reshaped_df.index, 0, 35000, color='#f0f0f0')

# Show the plot
plt.show()
