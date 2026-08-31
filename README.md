# CHOPS Protocol Planner

A simple web-based planner for generating a personalized schedule based on the **CHOP Modified Dallas POTS Exercise Program**.

The app converts the protocol's week/day schedule into actual calendar dates and combines the cardio and strength portions into one downloadable schedule.

## 🌐 Using the App

The planner runs entirely in your web browser through Streamlit.

**Live app:**
https://chops-automation-7rmrjebays3mjfpxantpl5.streamlit.app/

No installation, Python, or GitHub account is required to use the deployed app.

### How to Use

1. Select whether you have **gym access**.
2. Select whether you are taking a **beta blocker**.
3. Choose the date you want to begin the protocol.
4. Review the generated combined schedule.
5. Download the schedule as a **CSV file** if desired.

## 📅 What the Planner Generates

The planner combines the protocol's **cardio and strength schedules** into a single dated schedule.

### Cardio

Cardio sessions include the individual steps of each workout, such as warm-up, training intervals, recovery periods, and cool-down.

Cardio scheduling is the same regardless of whether you have gym access.

### Strength

Strength exercises are selected based on whether you indicate that you have access to a gym.

The resulting schedule includes information such as:

* Date
* Week and day
* Exercise
* Sets
* Hold time
* Duration
* Training mode, where applicable

## 💊 Beta Blockers

The planner asks whether you are taking a beta blocker so the appropriate protocol guidance can be used when interpreting training intensity.

Because beta blockers can affect heart-rate response to exercise, users should follow the guidance of their healthcare professional when determining appropriate exercise intensity.

## 📁 Project Structure

```text
CHOPS-Automation/
├── app.py
├── cardio_schedule_data.py
├── strength_schedule_data.py
├── requirements.txt
└── README.md
```

### `app.py`

The Streamlit application that generates and displays the schedule.

### `cardio_schedule_data.py`

Contains the structured cardio schedule used by the planner.

### `strength_schedule_data.py`

Contains the structured strength-training schedule used by the planner.

## 🏥 Original Protocol

This planner is based on the **CHOP Modified Dallas POTS Exercise Program** published by Dysautonomia International.

Original protocol:

https://dysautonomiainternational.org/pdf/CHOP_Modified_Dallas_POTS_Exercise_Program.pdf

Users are encouraged to read the original protocol in addition to using this scheduling tool.

## ⚠️ Medical Disclaimer

This project is an independent scheduling tool intended for educational and organizational purposes only.

It is **not medical advice**, does not replace the original CHOP Modified Dallas POTS Exercise Program, and is not a substitute for guidance from a physician, physical therapist, or other qualified healthcare professional.

Exercise programs may need to be modified based on an individual's medical conditions, medications, symptoms, and response to exercise.

Consult your healthcare professional before beginning or modifying an exercise program.

## 🛠️ Running Locally

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Then start the Streamlit application:

```bash
python3 -m streamlit run app.py
```

## Technology

* Python
* Streamlit
* pandas

## Contributing

Issues and improvements are welcome. If you notice a discrepancy between the planner and the original CHOP protocol, please refer to the original protocol as the authoritative source and report the issue through GitHub.
