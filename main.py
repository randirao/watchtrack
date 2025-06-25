from analysis.preprocess import *
from analysis.visualize import *

df = load_csv('data/sample.csv')
df = filter_lectures(df)
df = add_dropout_flag(df)
df = add_time_features(df)

plot_watch_ratio(df)
plot_time_heatmap(df)
plot_dropout_pie(df)