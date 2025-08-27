import pandas as pd
import ast
import os
from pathlib import Path

DATA_DIR = Path(__file__).parent / 'data'

# Load CSV data
def load_csv(name):
    return pd.read_csv(DATA_DIR / name)

# Load all reference data
_description = load_csv('description.csv')
_diets = load_csv('diets.csv')
_medications = load_csv('medications.csv')
_precautions = load_csv('precautions_df.csv')
_workouts = load_csv('workout_df.csv')
_severity = load_csv('Symptom-severity.csv')

# Utility: convert string list to Python list
def parse_list(value):
    if isinstance(value, str) and value.startswith('['):
        return ast.literal_eval(value)
    return [value]

# Lookup functions
def lookup_description(disease):
    row = _description[_description['Disease'].str.lower() == disease.lower()]
    return row['Description'].values[0] if not row.empty else 'No description found.'

def lookup_diets(disease):
    row = _diets[_diets['Disease'].str.lower() == disease.lower()]
    return parse_list(row['Diet'].values[0]) if not row.empty else []

def lookup_medications(disease):
    row = _medications[_medications['Disease'].str.lower() == disease.lower()]
    return parse_list(row['Medication'].values[0]) if not row.empty else []

def lookup_precautions(disease):
    row = _precautions[_precautions['Disease'].str.lower() == disease.lower()]
    if row.empty:
        return []
    return [row[f'Precaution_{i}'].values[0] for i in range(1,5) if f'Precaution_{i}' in row.columns and not pd.isna(row[f'Precaution_{i}'].values[0])]

def lookup_workouts(disease):
    rows = _workouts[_workouts['disease'].str.lower() == disease.lower()]
    return rows['workout'].tolist()

def get_all_recos(disease):
    return {
        'description': lookup_description(disease),
        'diets': lookup_diets(disease),
        'medications': lookup_medications(disease),
        'precautions': lookup_precautions(disease),
        'workouts': lookup_workouts(disease),
    }

# Symptom severity map
def symptom_severity_map():
    return dict(zip(_severity['Symptom'], _severity['weight']))