# AI-Driven Personal Fitness Trainer: A Search Algorithm Approach

## 📌 Project Overview
As part of the **Fundamentals of AI and ML** course at **VIT Bhopal**, this project implements and compares **Un-informed** and **Informed Search** algorithms to solve a real-world problem: **Optimizing Gym Workouts.**

The project treats a fitness session as a **State Space Search** problem. It compares how a "blind" search (BFS) and an "intelligent" search (A*) find the most efficient sequence of exercises to reach a goal (e.g., burning 400 calories in under 45 minutes).

---

## 🚀 Features
- **State Space Representation:** Gym exercises represented as nodes in a graph.
- **Un-informed Search (BFS):** Finds a valid workout sequence by exploring all possible exercise combinations.
- **Informed Search (A*):** Uses a **Heuristic Function** (Calorie Burn Rate + Muscle Priority) to find the optimal path.
- **Performance Comparison:** Visualizes the difference in "nodes explored" and "path efficiency" between the two algorithms.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** - `NumPy` / `Tensors` (Data representation)
  - `Matplotlib` (For performance visualization)
  - `Heapq` (Priority queue for A* implementation)

---

## 🧠 Core Concepts Applied
This project directly implements the following topics from our course syllabus:
1. **Search Algorithms:** BFS vs. A*.
2. **Heuristic Search:** Defining an admissible heuristic $h(n)$ for exercise efficiency.
3. **Goal-Based Agents:** The agent makes decisions based on the final target (The Goal State).
4. **Production Rules:** Logic-based constraints (e.g., *IF* Chest was worked, *THEN* prioritize Triceps).

---
### Customization

- You can freely modify priorities, change color codes, or customize task fields by editing `task_manager.py`.

---

### License

This project is distributed for educational and personal use. Modify and share freely.

---

### Author

Created by [Name- Harsh Vardhan Rai REGISTRATION NUMBER- 25BAI10401].
For feedback or suggestions, open an issue or contact directly.

## 📂 Repository Structure
```text
├── src/
│   ├── fitness_agent.py   # Main Python logic
│   ├── algorithms.py      # Implementation of BFS and A*
│   └── data_loader.py     # Exercise MET values and durations
├── docs/
│   └── Project_Report.pdf # Detailed academic report
├── README.md              # Project documentation
└── requirements.txt       # Necessary Python libraries 

