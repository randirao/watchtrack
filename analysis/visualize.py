import matplotlib.pyplot as plt
import seaborn as sns

def plot_watch_ratio(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['video_watch_ratio'], bins=30)
    plt.title('시청 비율 분포')
    plt.xlabel('Video Watch Ratio')
    plt.ylabel('Frequency')
    plt.show()

def plot_heatmap(df):
    heatmap_data = df.pivot_table(index='weekday', columns='hour', values='user_id', aggfunc='count').fillna(0)
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=False)
    plt.title('요일-시간대별 시청 히트맵')
    plt.xlabel('시간대')
    plt.ylabel('요일')
    plt.show()