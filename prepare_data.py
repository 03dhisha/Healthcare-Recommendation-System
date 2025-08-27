
import pandas as pd

# Load data
df = pd.read_csv('data/symtoms_df.csv')

# Get unique symptoms
symptom_cols = [col for col in df.columns if col.startswith('Symptom')]
all_symptoms = sorted(set(s.strip() for s in df[symptom_cols].values.flatten() if pd.notna(s)))

# Create binary matrix
rows = []
for _, row in df.iterrows():
    entry = {sym: 0 for sym in all_symptoms}
    for col in symptom_cols:
        s = row[col]
        if pd.notna(s):
            entry[s.strip()] = 1
    entry['Disease'] = row['Disease']
    rows.append(entry)

final_df = pd.DataFrame(rows)
final_df.to_csv('data/Training.csv', index=False)
print('Training.csv created with shape:', final_df.shape)