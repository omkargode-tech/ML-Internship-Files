# Student Instructions: Deploy Your Machine Learning App Locally with Streamlit

## Objective

By the end of this exercise, you should be able to:

* [ ] Take a trained machine learning model.
* [ ] Save the model to a file.
* [ ] Create a Streamlit user interface.
* [ ] Accept user input through the browser.
* [ ] Pass the input to your ML model.
* [ ] Display the prediction.
* [ ] Display prediction probability when supported.
* [ ] Handle preprocessing correctly.
* [ ] Run the application locally.
* [ ] Organize the project for future cloud deployment.

---

# 1. Understand What You Are Building

Your final application will follow this flow:

```text
                USER
                  │
                  ▼
          ┌───────────────┐
          │   Streamlit   │
          │      UI       │
          └───────┬───────┘
                  │
                  ▼
            User Inputs
                  │
                  ▼
          ┌───────────────┐
          │ Preprocessing │
          │  / Pipeline   │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │   ML Model    │
          └───────┬───────┘
                  │
                  ▼
             Prediction
                  │
                  ▼
          ┌───────────────┐
          │ Streamlit UI  │
          │    Result     │
          └───────────────┘
```

The important mental model is:

> **Streamlit is the user interface around your Python ML model.**

You are not rebuilding your ML model in Streamlit. Your job is to connect the trained model to a simple web interface.

---

# 2. Prerequisites

Before starting, make sure you have:

* Python installed.
* A trained ML model.
* Your training code or knowledge of the features used by the model.
* A code editor such as VS Code.
* A terminal/command prompt.
* Basic Python knowledge.
* Basic knowledge of pandas and scikit-learn if your model uses them.

Your trained model might be saved as:

```text
model.pkl
```

or:

```text
model.joblib
```

For this exercise, we will use:

```text
model.pkl
```

---

# 3. Create Your Project Folder

Create a new folder for your application.

For example:

```text
customer_prediction/
```

Open this folder in your code editor.

Initially, your project can look like:

```text
customer_prediction/
│
├── app.py
└── model.pkl
```

Later, we will add:

```text
requirements.txt
README.md
.gitignore
```

---

# 4. Create a Python Virtual Environment

Using a virtual environment is strongly recommended because it keeps your project's packages separate from other Python projects.

Open a terminal inside your project folder.

## Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

If that does not work in PowerShell, try:

```powershell
.\venv\Scripts\Activate.ps1
```

## macOS/Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

After activation, your terminal should indicate that the virtual environment is active.

---

# 5. Install the Required Libraries

Install Streamlit:

```bash
pip install streamlit
```

For a typical scikit-learn application, also install:

```bash
pip install scikit-learn pandas numpy joblib
```

You can install everything together:

```bash
pip install streamlit scikit-learn pandas numpy joblib
```

Verify Streamlit:

```bash
streamlit --version
```

If a Streamlit version is displayed, the installation was successful.

---

# 6. Create Your First Streamlit Application

Create a file called:

```text
app.py
```

Start with:

```python
import streamlit as st

st.title("My First ML Application")

st.write("Welcome to my machine learning application.")
```

Save the file.

Run:

```bash
streamlit run app.py
```

Streamlit will start a local web server.

Your application will normally be available at:

```text
http://localhost:8501
```

Open the address in your browser if it does not open automatically.

---

# 7. Understand What Just Happened

You wrote Python:

```python
st.title("My First ML Application")
```

Streamlit converted it into a web interface.

You did not have to write:

```text
HTML
CSS
JavaScript
```

This is the basic idea behind Streamlit:

```text
Python code
     ↓
Streamlit
     ↓
Web interface
```

---

# 8. Learn the Important Streamlit Functions

You do not need to memorize the entire Streamlit API.

Start with these:

| Function             | Purpose             |
| -------------------- | ------------------- |
| `st.title()`         | Main page title     |
| `st.header()`        | Section heading     |
| `st.subheader()`     | Smaller heading     |
| `st.write()`         | Display information |
| `st.text()`          | Display text        |
| `st.number_input()`  | Numeric input       |
| `st.text_input()`    | Text input          |
| `st.selectbox()`     | Dropdown            |
| `st.radio()`         | Radio buttons       |
| `st.checkbox()`      | Checkbox            |
| `st.button()`        | Button              |
| `st.slider()`        | Slider              |
| `st.file_uploader()` | Upload files        |
| `st.success()`       | Success message     |
| `st.error()`         | Error message       |
| `st.warning()`       | Warning message     |
| `st.dataframe()`     | Display a DataFrame |

You can build a surprisingly useful ML application using only these concepts.

---

# 9. Create User Input Fields

Assume your model predicts customer subscription.

The model expects these five features:

```text
Age
Income
Tenure
Monthly Spend
Support Calls
```

Add the following to `app.py`:

```python
age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

income = st.number_input(
    "Annual Income",
    min_value=0,
    value=50000
)

tenure = st.number_input(
    "Tenure (years)",
    min_value=0,
    value=2
)

monthly_spend = st.number_input(
    "Monthly Spend",
    min_value=0.0,
    value=1000.0
)

support_calls = st.number_input(
    "Support Calls",
    min_value=0,
    value=2
)
```

Streamlit displays input controls in the browser.

The important concept is:

```text
Browser input
     ↓
Python variable
```

For example:

```python
age = st.number_input("Age")
```

means that the value entered by the user becomes available through:

```python
age
```

---

# 10. Load Your Trained Model

If your model was saved using joblib:

```python
import joblib

model = joblib.load("model.pkl")
```

Your application now has access to the trained model.

The flow is:

```text
model.pkl
    ↓
joblib.load()
    ↓
Python model object
```

Place `model.pkl` in the same folder as `app.py`:

```text
customer_prediction/
│
├── app.py
└── model.pkl
```

---

# 11. Connect the Inputs to the Model

The model needs its inputs in the correct format.

Create:

```python
features = [[
    age,
    income,
    tenure,
    monthly_spend,
    support_calls
]]
```

Notice the double brackets:

```python
[[...]]
```

Scikit-learn generally expects input in the form:

```text
(number of samples, number of features)
```

Here we have:

```text
1 sample
5 features
```

Therefore:

```python
[
    [age, income, tenure, monthly_spend, support_calls]
]
```

represents:

```text
1 × 5
```

---

# 12. Make the Prediction

Use:

```python
prediction = model.predict(features)
```

The result may look like:

```python
[1]
```

or:

```python
[0]
```

The first value is accessed using:

```python
prediction[0]
```

For example:

```python
if prediction[0] == 1:
    st.success("Customer is likely to subscribe.")
else:
    st.error("Customer is unlikely to subscribe.")
```

---

# 13. Build the Complete First Version

Your `app.py` should now look similar to:

```python
import streamlit as st
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Page title
st.title("Customer Subscription Prediction")

st.write(
    "Enter customer information to predict subscription status."
)

# Inputs
age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

income = st.number_input(
    "Annual Income",
    min_value=0,
    value=50000
)

tenure = st.number_input(
    "Tenure (years)",
    min_value=0,
    value=2
)

monthly_spend = st.number_input(
    "Monthly Spend",
    min_value=0.0,
    value=1000.0
)

support_calls = st.number_input(
    "Support Calls",
    min_value=0,
    value=2
)

# Prediction button
if st.button("Predict"):

    features = [[
        age,
        income,
        tenure,
        monthly_spend,
        support_calls
    ]]

    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Customer is likely to subscribe.")
    else:
        st.error("Customer is unlikely to subscribe.")
```

Run:

```bash
streamlit run app.py
```

Test different values in the browser.

---

# 14. Add Prediction Probability

If your classification model supports `predict_proba()`, you can show the probability.

Add:

```python
probability = model.predict_proba(features)

prob = probability[0][1]

st.write(f"Subscription probability: {prob:.2%}")
```

You can combine this with the prediction:

```python
prediction = model.predict(features)
probability = model.predict_proba(features)

prob = probability[0][1]

if prediction[0] == 1:
    st.success(
        f"Customer is likely to subscribe. "
        f"Probability: {prob:.2%}"
    )
else:
    st.error(
        f"Customer is unlikely to subscribe. "
        f"Probability: {prob:.2%}"
    )
```

Important:

> `predict_proba()` is available only for models/classifiers that support probability estimates.

Do not assume every ML model has this method.

---

# 15. Very Important: Preprocessing Consistency

This is one of the most important parts of the entire project.

Suppose your training process used:

```text
Missing-value handling
       ↓
Encoding
       ↓
Scaling
       ↓
Feature engineering
       ↓
Model
```

Your Streamlit application must use the same preprocessing.

Do not train with:

```text
Input → Preprocessing → Model
```

and deploy with:

```text
Input → Model
```

That can produce incorrect predictions or errors.

Your production flow should be:

```text
User Input
    ↓
Same Preprocessing
    ↓
Same Feature Format
    ↓
Trained Model
    ↓
Prediction
```

---

# 16. Recommended Solution: Save the Complete Pipeline

A better approach with scikit-learn is to combine preprocessing and the model into one pipeline.

For example:

```python
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", LogisticRegression())
])
```

Train it:

```python
pipeline.fit(X_train, y_train)
```

Save it:

```python
import joblib

joblib.dump(pipeline, "model.pkl")
```

Then Streamlit only needs:

```python
model = joblib.load("model.pkl")
```

and:

```python
prediction = model.predict(features)
```

The saved pipeline handles the preprocessing.

Think of it as:

```text
User Input
    ↓
Saved Pipeline
    ↓
Preprocessing
    ↓
Model
    ↓
Prediction
```

This is safer and easier to deploy.

---

# 17. Improve the User Interface with Columns

Instead of putting every input underneath the previous input, use columns.

Example:

```python
col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    income = st.number_input(
        "Annual Income",
        min_value=0,
        value=50000
    )

with col2:
    tenure = st.number_input(
        "Tenure",
        min_value=0,
        value=2
    )

    monthly_spend = st.number_input(
        "Monthly Spend",
        min_value=0.0,
        value=1000.0
    )
```

This creates a cleaner interface.

---

# 18. Use a Sidebar

You can also place inputs in the sidebar:

```python
st.sidebar.title("Customer Information")

age = st.sidebar.number_input("Age")

income = st.sidebar.number_input("Annual Income")

tenure = st.sidebar.number_input("Tenure")
```

The application can then use:

```text
┌────────────────┬─────────────────────────────┐
│    SIDEBAR     │          MAIN APP           │
│                │                             │
│ Age            │ Customer Prediction         │
│ Income         │                             │
│ Tenure         │ Prediction Result           │
│ Spend          │                             │
│                │                             │
└────────────────┴─────────────────────────────┘
```

---

# 19. Cache the Model

Streamlit normally reruns your Python script when the user interacts with the application.

For example:

```text
User changes input
       ↓
Streamlit reruns app.py
       ↓
Python executes
       ↓
UI updates
```

Loading a large ML model every time is unnecessary.

Use Streamlit's resource caching:

```python
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")
```

Then:

```python
model = load_model()
```

Your application now becomes:

```python
import streamlit as st
import joblib

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()
```

This is the preferred pattern for reusable resources such as loaded ML models.

---

# 20. Add Error Handling

Your application should not crash unnecessarily when something goes wrong.

For example:

```python
if st.button("Predict"):

    try:
        features = [[
            age,
            income,
            tenure,
            monthly_spend,
            support_calls
        ]]

        prediction = model.predict(features)

        if prediction[0] == 1:
            st.success("Customer is likely to subscribe.")
        else:
            st.error("Customer is unlikely to subscribe.")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
```

During development, this can help you identify problems with:

* Incorrect feature order.
* Missing columns.
* Incorrect data types.
* Model loading.
* Preprocessing.
* Input shapes.

---

# 21. Optional: Add CSV File Upload

A useful extension is batch prediction.

Add:

```python
uploaded_file = st.file_uploader(
    "Upload CSV",
    type=["csv"]
)
```

Then:

```python
import pandas as pd

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.dataframe(df)
```

You can then make predictions:

```python
predictions = model.predict(df)

df["Prediction"] = predictions

st.dataframe(df)
```

This turns your application into a batch prediction tool.

However, make sure the uploaded CSV contains exactly the features expected by your model and preprocessing pipeline.

---

# 22. Create `requirements.txt`

Once your application works, create:

```text
requirements.txt
```

For a basic scikit-learn Streamlit application:

```text
streamlit
scikit-learn
pandas
numpy
joblib
```

This file tells another machine which Python packages are required to run your application.

A better practice for a real project is to ensure the versions are compatible with the environment in which the model was trained and tested.

---

# 23. Final Project Structure

Your beginner project should look like:

```text
customer_prediction/
│
├── app.py
├── model.pkl
└── requirements.txt
```

A more organized project can look like:

```text
customer_prediction/
│
├── app.py
│
├── model/
│   └── model.pkl
│
├── data/
│   └── sample.csv
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

For a larger project:

```text
customer_prediction/
│
├── app.py
│
├── model/
│   └── model.pkl
│
├── src/
│   ├── preprocessing.py
│   └── prediction.py
│
├── data/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 24. Run Your Application Locally

Open the terminal in the project directory.

Make sure your virtual environment is activated.

For example:

```bash
cd customer_prediction
```

Activate the environment.

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Then run:

```bash
streamlit run app.py
```

You should see a message indicating that the Streamlit application is running.

Open:

```text
http://localhost:8501
```

Your ML application is now running locally.

---

# 25. How to Stop the Application

Go back to the terminal where Streamlit is running.

Press:

```text
Ctrl + C
```

The local Streamlit server will stop.

To run it again:

```bash
streamlit run app.py
```

---

# 26. Local Deployment Checklist

Before considering the project complete, verify every item below.

* [ ] Python is installed.
* [ ] A virtual environment has been created.
* [ ] The virtual environment is activated.
* [ ] Streamlit is installed.
* [ ] scikit-learn is installed if required.
* [ ] pandas is installed if required.
* [ ] numpy is installed if required.
* [ ] joblib is installed if required.
* [ ] `app.py` exists.
* [ ] The trained model file exists.
* [ ] The model loads successfully.
* [ ] All required input fields are present.
* [ ] Input feature order matches training.
* [ ] Input data types are correct.
* [ ] Preprocessing is identical to training.
* [ ] The prediction works.
* [ ] The prediction result is displayed.
* [ ] Probability is displayed only if supported.
* [ ] Error handling has been tested.
* [ ] `requirements.txt` has been created.
* [ ] The application works at `localhost:8501`.

---

# 27. Test Your Application Properly

Do not test only one input.

Try several different combinations.

For example:

```text
Test 1
Age: 25
Income: 30000
Tenure: 1
Monthly Spend: 500
Support Calls: 1
```

Then:

```text
Test 2
Age: 60
Income: 100000
Tenure: 10
Monthly Spend: 3000
Support Calls: 5
```

Then try boundary values such as:

```text
Minimum age
Maximum age
Zero income
Zero tenure
Zero support calls
```

Check whether:

1. The application accepts the input.
2. The model produces a prediction.
3. The result is displayed correctly.
4. No Python error appears in the terminal.

---

# 28. Common Problems and Solutions

## Problem 1: `streamlit` is not recognized

Try:

```bash
python -m streamlit run app.py
```

This can help when the Streamlit executable is not available directly in your terminal PATH.

---

## Problem 2: `ModuleNotFoundError`

For example:

```text
ModuleNotFoundError: No module named 'joblib'
```

Install the missing package:

```bash
pip install joblib
```

Or install all project dependencies:

```bash
pip install -r requirements.txt
```

---

## Problem 3: Model file not found

You may see an error similar to:

```text
FileNotFoundError
```

Check that:

```text
app.py
model.pkl
```

are in the expected locations.

If your model is inside a folder:

```text
model/
    model.pkl
```

then load it using the correct path:

```python
model = joblib.load("model/model.pkl")
```

---

## Problem 4: Wrong number of features

You might see an error indicating that the model expected a different number of features.

For example:

```text
X has 4 features, but the model is expecting 5 features
```

Check:

* The features used during training.
* The features collected in Streamlit.
* The number of features.
* The order of features.
* Any preprocessing steps.

---

## Problem 5: Predictions look incorrect

Check preprocessing first.

Ask:

> Did I process the Streamlit inputs exactly the same way as the training data?

If you trained with scaling, encoding, imputation, or feature engineering, those steps must also happen during prediction.

A saved scikit-learn pipeline is usually the cleanest solution.

---

## Problem 6: `predict_proba` does not exist

Not every model supports:

```python
model.predict_proba()
```

If your model does not support it, do not use that method.

You can simply display:

```python
prediction = model.predict(features)
```

and show the predicted class.

---

## Problem 7: The app keeps rerunning

This is normal Streamlit behavior.

Streamlit generally reruns the script when the user interacts with widgets.

For expensive resources such as ML models, use:

```python
@st.cache_resource
```

to avoid unnecessarily reloading them.

---

# 29. Recommended Final `app.py`

Once you understand the basic version, aim for something like this:

```python
import streamlit as st
import joblib


# --------------------------------------------------
# Load Model
# --------------------------------------------------

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")


model = load_model()


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Customer Subscription Prediction",
    page_icon="🤖"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("Customer Subscription Prediction")

st.write(
    "Enter customer information to predict "
    "subscription status."
)


# --------------------------------------------------
# Input Section
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

    income = st.number_input(
        "Annual Income",
        min_value=0,
        value=50000
    )

    tenure = st.number_input(
        "Tenure (years)",
        min_value=0,
        value=2
    )


with col2:

    monthly_spend = st.number_input(
        "Monthly Spend",
        min_value=0.0,
        value=1000.0
    )

    support_calls = st.number_input(
        "Support Calls",
        min_value=0,
        value=2
    )


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict"):

    try:

        features = [[
            age,
            income,
            tenure,
            monthly_spend,
            support_calls
        ]]

        prediction = model.predict(features)

        if prediction[0] == 1:

            st.success(
                "Customer is likely to subscribe."
            )

        else:

            st.error(
                "Customer is unlikely to subscribe."
            )

        # Probability if supported
        if hasattr(model, "predict_proba"):

            probability = model.predict_proba(features)

            prob = probability[0][1]

            st.write(
                f"Subscription probability: {prob:.2%}"
            )

    except Exception as e:

        st.error(
            f"Prediction failed: {e}"
        )
```

Run it with:

```bash
streamlit run app.py
```

---

# 30. Final Architecture

At this stage, your project should work like this:

```text
                   BROWSER
                      │
                      ▼
              ┌───────────────┐
              │   Streamlit   │
              │      UI       │
              └───────┬───────┘
                      │
                      ▼
                User Inputs
                      │
                      ▼
              ┌───────────────┐
              │ Input Format  │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Saved Pipeline│
              │  / ML Model   │
              └───────┬───────┘
                      │
                      ▼
                 Prediction
                      │
                      ▼
              ┌───────────────┐
              │ Result in UI  │
              └───────────────┘
```

---

# 31. The Complete Workflow to Remember

Whenever you deploy an ML model with Streamlit, remember:

```text
TRAIN
  ↓
SAVE
  ↓
LOAD
  ↓
INPUT
  ↓
FORMAT
  ↓
PREPROCESS
  ↓
PREDICT
  ↓
DISPLAY
  ↓
TEST
  ↓
DEPLOY
```

A shorter version is:

> **MODEL → LOAD → INPUT → FORMAT → PREDICT → DISPLAY → DEPLOY**

Or remember:

> **“Load it, ask for it, format it, predict it, show it, deploy it.”**

---

# 32. Student Assignment

Build a Streamlit application for **your own trained ML model**.

Your application must contain:

* [ ] A project folder.
* [ ] A Python virtual environment.
* [ ] `app.py`.
* [ ] Your trained model/pipeline.
* [ ] `requirements.txt`.
* [ ] At least three user input fields.
* [ ] A **Predict** button.
* [ ] Correct feature formatting.
* [ ] Correct preprocessing.
* [ ] Model prediction.
* [ ] A visible prediction result.
* [ ] Appropriate success/error output.
* [ ] Model caching using `st.cache_resource` where appropriate.
* [ ] A clean and readable UI.
* [ ] Successful execution at `http://localhost:8501`.

## Submission

Submit the following:

```text
your_ml_app/
│
├── app.py
├── model.pkl
├── requirements.txt
└── README.md
```

Your `README.md` should explain:

1. What your ML model predicts.
2. Which features the user enters.
3. How to install dependencies.
4. How to run the Streamlit application.
5. What the prediction means.

The main command your instructor should be able to run is:

```bash
streamlit run app.py
```

---

# 33. What You Should Learn Next

Once your first local Streamlit application works, continue with these concepts in this order:

```text
1. st.form
      ↓
2. Model/Pipeline Loading
      ↓
3. Preprocessing Consistency
      ↓
4. st.session_state
      ↓
5. Caching
      ↓
6. File Uploads
      ↓
7. Charts and Visualizations
      ↓
8. Error Handling
      ↓
9. Project Organization
      ↓
10. Cloud Deployment
```

Do **not** try to learn every Streamlit feature before building your first application.

Your immediate goal is simple:

> **Take your trained ML model, connect it to a Streamlit interface, run it successfully on `localhost:8501`, and verify that real user inputs produce predictions.**

Once you can do that, you have successfully converted a machine learning model into a working local web application.
