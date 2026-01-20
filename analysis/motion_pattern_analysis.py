import pandas as pd
import matplotlib.pyplot as plt

# 1. Load emotion log data
data = pd.read_csv("data/sample_emotion_log.csv")

# 2. Convert time column
data["time"] = pd.to_datetime(data["time"])

# 3. Sort by time
data = data.sort_values("time")

# 4. Calculate emotional instability (absolute change)
data["instability"] = data["emotion_score"].diff().abs()

# 5. Basic statistics
mean_instability = data["instability"].mean()

print("Average Emotional Instability:", round(mean_instability, 3))

# 6. Visualization
plt.figure()
plt.plot(data["time"], data["emotion_score"])
plt.xlabel("Time")
plt.ylabel("Emotion Score")
plt.title("Temporal Emotion Pattern")
plt.show()
