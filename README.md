# Adaptive Query Optimization (AOQ)

### Overview
Adaptive Query Optimization (AOQ) is a machine learning-based system designed to improve SQL query performance in dynamic database environments. The system predicts query execution time and dynamically selects an optimal execution strategy, overcoming the limitations of traditional static query optimization techniques.

---

### Key Features
- Query runtime prediction using machine learning  
- Adaptive optimization strategy (fast path vs optimized execution)  
- Feedback-based continuous learning mechanism  
- Performance monitoring and logging  
- Web-based interface using Flask  
- PostgreSQL integration for real query execution  

---

### System Architecture
User Query → Feature Extraction → ML Prediction → Strategy Selection → Query Execution → Logging → Model Retraining

---

### Technology Stack
- Backend: Python, Flask  
- Database: PostgreSQL  
- Machine Learning: Scikit-learn (Random Forest)  
- Data Processing: Pandas, NumPy  
- Frontend: HTML, CSS  
- Tools: Git, GitHub, Codespaces  

---

### Machine Learning Approach
The system extracts structured features from SQL queries, including:
- Query length  
- Number of joins  
- WHERE conditions  
- Aggregation functions  
- GROUP BY / ORDER BY clauses  
- Number of tables involved  

A Random Forest Regressor is used to predict query execution time based on these features.

---

### Results
- Achieved 75–80% prediction accuracy  
- Improved query execution performance by approximately 30–40%  
- Effective handling of complex queries  
- Performance improves over time through feedback-based learning  

---

### Project Structure
```bash
adaptive-query-optimizer/
│
├── app.py
├── database/
│   ├── db.py
│   ├── seed_data.py
│
├── services/
│   ├── executor_service.py
│   ├── feature_service.py
│
├── ml/
│   ├── train_model.py
│   ├── model.pkl
│
├── logs/
│   └── query_logs.csv
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── requirements.txt

```
Setup and Installation
1. Clone Repository

git clone https://github.com/prajwal-devaraj/adaptive-query-optimizer.git

cd adaptive-query-optimizer

2. Create Virtual Environment

python -m venv .venv

source .venv/bin/activate

For Windows:

.venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure PostgreSQL

CREATE DATABASE aqo_db;

Update credentials in database/db.py if required.

5. Seed Data

python database/seed_data.py

7. Train Model

python ml/train_model.py

9. Run Application

python app.py

11. Open in Browser

http://127.0.0.1:5000

### Workflow
1. User submits SQL query
2. System extracts features
3. Machine learning model predicts execution time
4. Optimization strategy is selected
5. Query is executed in PostgreSQL
6. Results are logged
7. Model retrained using new data

### Challenges
- Limited training data in initial stages
- Dependency on feature quality
- Database connectivity configuration

Future Work
- Distributed database support
- Real-time adaptive optimization
- Integration with query execution plans
- Advanced ML models (Deep Learning, Reinforcement Learning)
- Explainable AI integration

Author

Prajwal Devaraj

Note

This project was fully designed and implemented independently by Prajwal Devaraj. It was developed for academic purposes and later shared for submission use.

License

This project is intended for academic and research purposes.
