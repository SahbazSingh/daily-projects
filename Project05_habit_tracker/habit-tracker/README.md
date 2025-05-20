# 🚴‍♂️ Habit Tracker (Pixela API)

This project is a simple Python-based habit tracker that interacts with the [Pixela API](https://pixe.la/) to help you visualize your daily habits — in this case, tracking **cycling distance in kilometers**.

The script allows you to:
- ✅ Create a Pixela user account (first-time setup)
- 📈 Create a custom graph for your habit
- 📅 Log your daily progress (aka "add a pixel")
- ✏️ Update your entry for today
- ❌ Delete your entry for today

---

## 📦 Features

- Uses `requests` to make API calls
- Stores sensitive information securely using `.env`
- Organized with reusable functions
- Tracks daily input based on date
- Clean structure and customizable graph options

---

## 🛠 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/SahbazSingh/daily-projects.git
cd daily-projects/Project05_habit_tracker/habit-tracker