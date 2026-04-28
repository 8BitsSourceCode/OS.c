import pandas as pd
import math

# Dataset (in program)
data = {
    'Outlook':['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny'],
    'Humidity':['High','High','High','High','Normal','Normal','Normal','High'],
    'Wind':['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak'],
    'Play':['No','No','Yes','Yes','Yes','No','Yes','No']
}

df = pd.DataFrame(data)

# Entropy
def entropy(col):
    p = col.value_counts(normalize=True)
    return -sum(p * p.apply(lambda x: math.log2(x)))

# Information Gain
def gain(data, attr):
    return entropy(data['Play']) - sum(
        (len(data[data[attr]==v])/len(data)) * entropy(data[data[attr]==v]['Play'])
        for v in data[attr].unique()
    )

# ID3 (very short)
def id3(data, features):
    if len(data['Play'].unique()) == 1:
        return data['Play'].iloc[0]
    
    best = max(features, key=lambda x: gain(data, x))
    tree = {best:{}}
    
    for v in data[best].unique():
        sub = data[data[best]==v]
        if sub.empty:
            tree[best][v] = data['Play'].mode()[0]
        else:
            rem = [f for f in features if f != best]
            tree[best][v] = id3(sub, rem)
    
    return tree

# Build tree
tree = id3(df, list(df.columns[:-1]))
print("Tree:", tree)

# Prediction
def predict(q, tree):
    for k in tree:
        val = tree[k].get(q[k])
        return predict(q, val) if isinstance(val, dict) else val

# Test sample
sample = {'Outlook':'Sunny','Humidity':'High','Wind':'Strong'}
print("Prediction:", predict(sample, tree))