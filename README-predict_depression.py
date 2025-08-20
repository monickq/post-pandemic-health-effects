What the script does:
1. Loads the dataset from post_pandemic_remote_work_health_impact_2025.csv.
2. Transforms columns:
  Burnout_Level → maps Low = 1, Medium = 2, High = 3
  Mental_Health_Status → fills missing values with "none"
  Creates a binary variable Depression (1 = has depression, 0 = no depression)
  Inverts Work_Life_Balance_Score so that 1 = best, 5 = worst.

3. Trains a Random Forest model to predict depression based on:
- Social_Isolation_Score
- Burnout_Level
- Work_Life_Balance_Score_inv

4. Evaluates the model – prints overall accuracy and a classification report.

5. Predicts new data – for example, a person with:

Social_Isolation_Score = 1

Burnout_Level = 3

Work_Life_Balance_Score_inv = 4

📊 Output:

Accuracy (0.67)

classification_report (precision, recall, F1-score per class)

Text interpretation of the prediction result, e.g.:

Score: 1 -> Is at risk of depression

Score: 0 -> Probably won't experience depression
