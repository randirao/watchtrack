def load_data(filepath):
    return pd.read_csv(filepath)

def filter_video_only(df):
    return df[(df['content_type_id'] == 1) & (df['elapsed_time'] > 10000)]

def add_dropout_column(df):
    df['dropout'] = (df['video_watch_ratio'] < 0.5).astype(int)
    return df

def add_time_features(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df['hour'] = df['timestamp'].dt.hour
    df['weekday'] = df['timestamp'].dt.day_name()
    return df