import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('PPBEmo_Emotion_label.xlsx')
data.set_index("PPB_Emo_dataset@Physiological_data", inplace=True)

dataframe_item = data.iloc[0]
image_id = dataframe_item[12]

intensity = dataframe_item["intensity"]

print(dataframe_item)
print(image_id)
print(intensity)


