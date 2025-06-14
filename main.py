from analysis.preprocess import *
from analysis.visualize import *

df = load_data('data/ednet/KT3kt3/123456.csv')
df = filter_video_only(df)
df = add_dropout_column(df)
df = add_time_features(df)

plot_watch_ratio(df)
plot_heatmap(df)