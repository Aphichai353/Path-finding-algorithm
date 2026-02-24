# AI Search Algorithms: Romania & Thailand Map Problems
# โปรแกรมค้นหาเส้นทาง: อัลกอริทึมการค้นหาในแผนที่โรมาเนียและประเทศไทย

This project contains several search algorithm implementations in Python, designed to find paths between cities using two different graph data sets: the classic **Romania Map** from "Artificial Intelligence: A Modern Approach" and a custom **Thailand Roads** map.

โปรเจกต์นี้รวบรวมการอ้างอิงอัลกอริทึมการค้นหาที่เขียนด้วยภาษา Python เพื่อหาเส้นทางระหว่างเมือง โดยใช้ข้อมูลกราฟ 2 ชุด คือ **แผนที่ประเทศโรมาเนีย (Romania Map)** จากหนังสือ AI ยอดนิยม และ **แผนที่ถนนในประเทศไทย (Thailand Roads)** ที่กำหนดขึ้นเอง

---

## 🚀 Algorithms Implemented (อัลกอริทึมที่รองรับ)

1.  **Breadth-First Search (BFS)**
    *   Finds the shortest path in terms of the number of steps (unweighted shortest path).
    *   ค้นหาเส้นทางที่สั้นที่สุดในแง่ของจำนวนขั้นตอน (ก้าว)
2.  **Depth-First Search (DFS)**
    *   Explores as deep as possible before backtracking.
    *   ค้นหาโดยการเจาะลึกลงไปในกิ่งหนึ่งจนสุดก่อนที่จะย้อนกลับ
3.  **Uniform Cost Search (UCS)**
    *   Finds the cheapest path by expanding nodes with the lowest path cost.
    *   ค้นหาเส้นทางที่ประหยัดหรือสั้นที่สุดโดยพิจารณาจากระยะทางสะสม (Path Cost)
4.  **Best-First Search**
    *   Expands nodes based on an evaluation function $f(n)$. In this implementation, it is configured to use path cost (equivalent to UCS).
    *   ค้นหาโดยเลือกโหนดที่ดีที่สุดตามฟังก์ชันประเมิน $f(n)$ ในที่นี้กำหนดให้ใช้ระยะทางสะสม (ซึ่งจะมีผลเหมือนกับ UCS)

---

## 📂 Project Structure (โครงสร้างโปรเจกต์)

-   `ฺBFS1.py`: Breadth-First Search implementation using the **Thailand map**.
-   `UCS.py`: Uniform Cost Search implementation using the **Thailand map**.
-   `Depth-first search.py`: Depth-First Search implementation using the **Romania map**.
-   `Depth-First SearchThai.py`: Thai version of DFS for the **Romania map**.
-   `Best-First Search.py`: Best-First Search (configured as UCS) for the **Romania map**.
-   `Best-First SearchThai.py`: Thai version of Best-First Search for the **Romania map**.

---

## 🛠️ Requirements (สิ่งที่ต้องมี)

-   Python 3.x
-   No external libraries required (uses standard libraries like `collections` and `heapq`).

-   Python 3.x
-   ไม่ต้องติดตั้งไลบรารีเพิ่มเติม (ใช้ไลบรารีมาตรฐานเช่น `collections` และ `heapq`)

---

## 📖 How to Run (วิธีเรียกใช้งาน)

You can run any script directly using the Python interpreter:
คุณสามารถรันไฟล์คริปต์ใดก็ได้ผ่าน Python:

```bash
python "Best-First Search.py"
python "UCS.py"
python "ฺBFS1.py"
```

Each script is pre-configured with a start and goal city and will output the resulting path and total distance (if applicable).

แต่ละสคริปต์ได้กำหนดเมืองเริ่มต้นและเป้าหมายไว้แล้ว โดยจะแสดงผลลัพธ์เป็นเส้นทางและระยะทางรวม

---

## 🗺️ Maps Data (ข้อมูลแผนที่)

### Romania Map (แผนที่โรมาเนีย)
Includes cities such as Arad, Bucharest, Craiova, Drobeta, Eforie, Fagaras, Giurgiu, Hirsova, Iasi, Lugoj, Mehadia, Neamt, Oradea, Pitesti, Rimnicu Vilcea, Sibiu, Timisoara, Urziceni, Vaslui, and Zerind.

### Thailand map (แผนที่ประเทศไทย)
Includes cities such as Bangkok, Ayutthaya, Nakhon Pathom, Kanchanaburi, Chonburi, Pattaya, Rayong, Hua Hin, Saraburi, Nakhon Ratchasima, Khon Kaen, Udon Thani, Phitsanulok, and Chiang Mai.

---

## ✨ Features (คุณสมบัติ)
-   **Step-by-step output (Verbose mode):** Most scripts include a `verbose=True` option to see how the algorithm behaves at each step.
-   **Path Reconstruction:** Rebuilds the path from the goal node back to the start.
-   **Thai Comments:** Several versions include explanation and comments in Thai for educational purposes.

-   **การแสดงผลทีละขั้นตอน (Verbose):** สคริปต์ส่วนใหญ่มีโหมด `verbose=True` เพื่อดูการทำงานของอัลกอริทึมในแต่ละรอบ
-   **การย้อนรอยเส้นทาง (Path Reconstruction):** สร้างเส้นทางจากจุดเป้าหมายกลับมายังจุดเริ่มต้น
-   **คำอธิบายภาษาไทย:** มีไฟล์เวอร์ชันภาษาไทยเพื่อความสะดวกในการเรียนรู้และศึกษาโค้ด
