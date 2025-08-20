import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

def load_data():
    try:
        data = pd.read_csv("post_pandemic_remote_work_health_impact_2025.csv")
        return data
    except FileNotFoundError:
        print("Dataset file not found. Please ensure the file is in the correct directory.")
        exit(1)

def transform_data(data):
    # Change "Low", "Medium", "High" to 1, 2, 3
    data["Burnout_Level"] = data["Burnout_Level"].map({"Low": 1, "Medium": 2, "High": 3})

    # Change None values to strings "none"
    data['Mental_Health_Status'] = data['Mental_Health_Status'].fillna("none")

    # Create a binary column for "Depression"
    data["Depression"] = data["Mental_Health_Status"].apply(lambda x: 1 if x.lower() == "depression" else 0) # 1 - does have, 0 - does not have

    # Now we invert Work_Life_Balance_Score, so that 1=best and 5=worst
    data["Work_Life_Balance_Score_inv"] = 6 - data["Work_Life_Balance_Score"]

    return data 

def make_model(data):
    # Define input features and output label
    x = data[["Social_Isolation_Score", "Burnout_Level", "Work_Life_Balance_Score_inv"]]
    y = data["Depression"]

    # Split the dataset into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

    # Train the Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    model.fit(x_train, y_train)

    # Evaluate the model
    y_pred = model.predict(x_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))    

    return model

def main():
    data = load_data()
    data = transform_data(data)
    model = make_model(data)

    new_data = pd.DataFrame({
    "Social_Isolation_Score": [1],
    "Burnout_Level": [3],
    "Work_Life_Balance_Score_inv": [4],
    })
    
    predict_new_data(model, new_data)

# Create new data for prediction
# Social_Isolation_Score ranges from 1 to 3.5 -> 3.5 being the highest level of isolation.
# Burnout _Level ranges from 1 to 3 -> 1 being the lowest level of burnout, 3 being the highest.
# Work_Life_Balance_Score ranges from 1 to 5 -> 5 being the worst work-life balance, 1 being the best.


def predict_new_data(model, new_data):
    new_prediction = model.predict(new_data)
    print("Score: 1 -> Is at risk of depression" if new_prediction[0] == 1 else "Score: 0 -> Probably won't experience depression")
    return new_prediction

if __name__ == "__main__":
    main()