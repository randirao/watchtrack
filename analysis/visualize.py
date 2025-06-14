import matplotlib.pyplot as plt
import seaborn as sns

def plot_watch_ratio(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['video_watch_ratio'], bins=30)
    plt.title("시청 비율 분포")
    plt.xlabel("Video Watch Ratio")
    plt.ylabel("빈도")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_time_heatmap(df):
    heatmap_data = df.pivot_table(index='weekday', columns='hour', values='user_id', aggfunc='count').fillna(0)
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='.0f')
    plt.title("요일-시간대별 시청 활동")
    plt.xlabel("시간대 (Hour)")
    plt.ylabel("요일")
    plt.tight_layout()
    plt.show()

def plot_dropout_pie(df):
    sizes = df['dropout'].value_counts().sort_index()
    labels = ['이탈', '완강']
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
    plt.title("이탈 vs 완강 비율")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
