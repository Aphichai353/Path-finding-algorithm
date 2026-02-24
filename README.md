# 🗺️ RBE — รวมอัลกอริทึมค้นหาเส้นทาง | Pathfinding Search Algorithms Collection

> **ภาษาไทย (Thai)** ด้านบน / **English** ด้านล่าง

---

## 📖 สารบัญ | Table of Contents

- [🇹🇭 ภาษาไทย (Thai Version)](#-ภาษาไทย-thai-version)
  - [ภาพรวมโครงการ](#-ภาพรวมโครงการ)
  - [โครงสร้างไฟล์](#-โครงสร้างไฟล์)
  - [รายละเอียดอัลกอริทึม](#-รายละเอียดอัลกอริทึม)
  - [ข้อมูลกราฟแผนที่](#-ข้อมูลกราฟแผนที่)
  - [วิธีการใช้งาน](#-วิธีการใช้งาน)
  - [ความต้องการของระบบ](#-ความต้องการของระบบ)
  - [ตัวอย่างผลลัพธ์](#-ตัวอย่างผลลัพธ์)
- [🇬🇧 English Version](#-english-version)
  - [Project Overview](#-project-overview)
  - [File Structure](#-file-structure)
  - [Algorithm Details](#-algorithm-details)
  - [Map Graph Data](#-map-graph-data)
  - [How to Use](#-how-to-use)
  - [System Requirements](#-system-requirements)
  - [Example Output](#-example-output)
- [อ้างอิง | References](#-อ้างอิง--references)

---

# 🇹🇭 ภาษาไทย (Thai Version)

## 🔍 ภาพรวมโครงการ

โครงการนี้เป็นการรวบรวม **อัลกอริทึมค้นหาเส้นทาง (Search Algorithms)** ที่สำคัญในวิชา **ปัญญาประดิษฐ์ (Artificial Intelligence)** จำนวน **7 อัลกอริทึม** โดยเขียนด้วยภาษา Python ทั้งหมด

อัลกอริทึมเหล่านี้ถูกนำมาประยุกต์ใช้กับปัญหาการค้นหาเส้นทางบน **แผนที่ถนนประเทศไทย** (14 จังหวัด) และ **แผนที่ถนนประเทศโรมาเนีย** (20 เมือง) ซึ่งเป็นตัวอย่างคลาสสิกจากตำรา *Artificial Intelligence: A Modern Approach* (AIMA)

### 🎯 จุดประสงค์

- เพื่อศึกษาและทำความเข้าใจอัลกอริทึมค้นหาเส้นทางแบบต่าง ๆ
- เพื่อเปรียบเทียบการทำงานระหว่าง **Uninformed Search** และ **Informed Search**
- เพื่อประยุกต์ใช้งานกับข้อมูลแผนที่จริง (ประเทศไทย & โรมาเนีย)

---

## 📁 โครงสร้างไฟล์

```
📦 งาน RBE/
├── 📄 Best-First Search.py          # Best-First Search — แผนที่โรมาเนีย (พร้อม verbose)
├── 📄 Best-First SearchThai.py      # Best-First Search — แผนที่ประเทศไทย
├── 📄 Depth-first search.py         # Depth-First Search (DFS) — แผนที่โรมาเนีย (พร้อม verbose)
├── 📄 Depth-First SearchThai.py     # Depth-First Search (DFS) — แผนที่ประเทศไทย
├── 📄 ฺBFS1.py                      # Breadth-First Search (BFS) — แผนที่ประเทศไทย
├── 📄 DLS.py                        # Depth-Limited Search (DLS) — แผนที่ประเทศไทย
├── 📄 IDS.py                        # Iterative Deepening Search (IDS) — แผนที่ประเทศไทย
├── 📄 UCS.py                        # Uniform Cost Search (UCS) — แผนที่ประเทศไทย
├── 📄 ฺBiBF.py                      # Bidirectional Best-First Search — แผนที่ประเทศไทย
└── 📄 README.md                     # ไฟล์เอกสารนี้
```

---

## 🧠 รายละเอียดอัลกอริทึม

### 1. Breadth-First Search (BFS) — `ฺBFS1.py`

| หัวข้อ | รายละเอียด |
|---|---|
| **ประเภท** | Uninformed Search (ค้นหาแบบไม่มีข้อมูลเพิ่มเติม) |
| **โครงสร้างข้อมูล** | FIFO Queue (`collections.deque`) |
| **หลักการ** | สำรวจทุกโหนดในระดับเดียวกันก่อน แล้วค่อยลงลึกไปในระดับถัดไป |
| **ความสมบูรณ์ (Complete)** | ✅ ใช่ — รับประกันว่าจะหาคำตอบเจอ (ถ้ามีคำตอบ) |
| **ความเหมาะสม (Optimal)** | ✅ ใช่ — หาเส้นทางที่มีจำนวนก้าวน้อยที่สุด (ไม่ใช่ระยะทางน้อยที่สุด) |
| **แผนที่** | ประเทศไทย |

---

### 2. Depth-First Search (DFS) — `Depth-first search.py` & `Depth-First SearchThai.py`

| หัวข้อ | รายละเอียด |
|---|---|
| **ประเภท** | Uninformed Search |
| **โครงสร้างข้อมูล** | Stack (LIFO) |
| **หลักการ** | ดิ่งลงลึกสุดในสาขาหนึ่งก่อน แล้วจึงย้อนกลับ (Backtracking) ไปสำรวจสาขาอื่น |
| **ความสมบูรณ์** | ❌ ไม่ — อาจวนลูปไม่สิ้นสุดในกราฟที่มี cycle (โค้ดนี้ใช้ `reached` set ป้องกัน) |
| **ความเหมาะสม** | ❌ ไม่ — ไม่รับประกันเส้นทางที่สั้นที่สุด |
| **แผนที่** | โรมาเนีย (`Depth-first search.py`) และ ไทย (`Depth-First SearchThai.py`) |

**ไฟล์เวอร์ชันโรมาเนีย** ใช้โครงสร้างคลาส `RomaniaProblem` อย่างเป็นระบบ พร้อมโหมด `verbose` แสดงขั้นตอนการทำงาน

---

### 3. Depth-Limited Search (DLS) — `DLS.py`

| หัวข้อ | รายละเอียด |
|---|---|
| **ประเภท** | Uninformed Search |
| **โครงสร้างข้อมูล** | Stack (LIFO) |
| **หลักการ** | เหมือน DFS แต่จำกัดความลึกสูงสุด (Depth Limit) เพื่อป้องกันการค้นหาลึกเกินไป |
| **ความสมบูรณ์** | ❌ ไม่ — หาไม่เจอถ้าคำตอบอยู่ลึกกว่า limit |
| **ความเหมาะสม** | ❌ ไม่ |
| **ผลลัพธ์พิเศษ** | คืนค่า `"cutoff"` หากถูกตัดที่ depth limit หรือ `"failure"` หากไม่มีเส้นทาง |
| **แผนที่** | ประเทศไทย |

---

### 4. Iterative Deepening Search (IDS) — `IDS.py`

| หัวข้อ | รายละเอียด |
|---|---|
| **ประเภท** | Uninformed Search |
| **โครงสร้างข้อมูล** | Stack + DLS แบบวนซ้ำ |
| **หลักการ** | เรียก DLS ซ้ำโดยเพิ่ม depth limit ขึ้นทีละ 1 (depth = 0, 1, 2, …) จนกว่าจะเจอคำตอบ |
| **ความสมบูรณ์** | ✅ ใช่ |
| **ความเหมาะสม** | ✅ ใช่ — หาเส้นทางที่มีจำนวนก้าวน้อยที่สุด |
| **จุดเด่น** | รวมข้อดีของ BFS (สมบูรณ์) กับ DFS (ใช้หน่วยความจำน้อย) |
| **แผนที่** | ประเทศไทย |

---

### 5. Uniform Cost Search (UCS) — `UCS.py`

| หัวข้อ | รายละเอียด |
|---|---|
| **ประเภท** | Uninformed Search |
| **โครงสร้างข้อมูล** | Priority Queue (`heapq`) |
| **หลักการ** | ขยายโหนดที่มี **ต้นทุนสะสม (g(n))** ต่ำที่สุดก่อน |
| **ความสมบูรณ์** | ✅ ใช่ |
| **ความเหมาะสม** | ✅ ใช่ — รับประกันเส้นทางที่มี **ระยะทางรวมน้อยที่สุด** |
| **แผนที่** | ประเทศไทย |

---

### 6. Best-First Search — `Best-First Search.py` & `Best-First SearchThai.py`

| หัวข้อ | รายละเอียด |
|---|---|
| **ประเภท** | Informed Search (ค้นหาแบบมีข้อมูลนำทาง) |
| **โครงสร้างข้อมูล** | Priority Queue (`heapq`) |
| **หลักการ** | ขยายโหนดตามฟังก์ชัน **f(n)** ที่กำหนด สามารถปรับเปลี่ยนได้ (เช่น `f(n) = path_cost` ก็จะทำงานเหมือน UCS) |
| **ความสมบูรณ์** | ✅ ใช่ |
| **ความเหมาะสม** | ขึ้นอยู่กับฟังก์ชัน f(n) ที่ใช้ |
| **โหมด Verbose** | ✅ มี — แสดงขั้นตอนการทำงานแบบละเอียด (Frontier, โหนดที่ขยาย, ฯลฯ) |
| **แผนที่** | โรมาเนีย (`Best-First Search.py`) และ ไทย (`Best-First SearchThai.py`) |

---

### 7. Bidirectional Best-First Search — `ฺBiBF.py`

| หัวข้อ | รายละเอียด |
|---|---|
| **ประเภท** | Informed / Uninformed Search (ใช้ UCS แบบสองทิศทาง) |
| **โครงสร้างข้อมูล** | Priority Queue สองตัว (Forward & Backward) |
| **หลักการ** | ค้นหาพร้อมกันจากทั้ง **จุดเริ่มต้น** และ **จุดหมาย** เมื่อทั้งสองฝ่ายพบกัน → สร้างเส้นทางรวม |
| **ความสมบูรณ์** | ✅ ใช่ |
| **ความเหมาะสม** | ✅ ใช่ |
| **จุดเด่น** | ลดจำนวนโหนดที่ต้องสำรวจอย่างมาก เนื่องจาก search space ลดลงแบบเลขชี้กำลัง |
| **แผนที่** | ประเทศไทย |

---

## 🗺️ ข้อมูลกราฟแผนที่

### 🇹🇭 แผนที่ประเทศไทย (14 จังหวัด)

กราฟแบบถ่วงน้ำหนัก (Weighted Graph) แสดงระยะทางโดยประมาณ (กิโลเมตร):

```
                        ChiangMai
                           |
                        (370 กม.)
                           |
                       Phitsanulok
                           |
                        (330 กม.)
                           |
          NakhonPathom---Bangkok---Ayutthaya---Saraburi---NakhonRatchasima---KhonKaen---UdonThani
            (60 กม.)    / |  \      (80 กม.)   (75 กม.)     (170 กม.)       (200 กม.)  (110 กม.)
               |      /   |   \
         Kanchanaburi /    |    Chonburi
          (130 กม.) /   (200)    (85 กม.)
              |   /    กม.  \      |
         (95 กม.)       |    Pattaya---Rayong
                      HuaHin  (50 กม.)  (65 กม.)
```

**จังหวัดทั้งหมด:** Bangkok, Ayutthaya, NakhonPathom, Kanchanaburi, Chonburi, Pattaya, Rayong, HuaHin, Saraburi, NakhonRatchasima, KhonKaen, UdonThani, Phitsanulok, ChiangMai

---

### 🇷🇴 แผนที่ประเทศโรมาเนีย (20 เมือง)

กราฟคลาสสิกจากตำรา AIMA แสดงระยะทาง (ไมล์):

**เมืองทั้งหมด:** Oradea, Zerind, Arad, Timisoara, Lugoj, Mehadia, Drobeta, Craiova, Sibiu, Rimnicu Vilcea, Fagaras, Pitesti, Bucharest, Giurgiu, Urziceni, Hirsova, Eforie, Vaslui, Iasi, Neamt

---

## 🚀 วิธีการใช้งาน

### ขั้นตอนที่ 1: ตรวจสอบ Python

```bash
python --version
# ต้องใช้ Python 3.6 ขึ้นไป
```

### ขั้นตอนที่ 2: รันอัลกอริทึมที่ต้องการ

```bash
# Breadth-First Search
python ฺBFS1.py

# Depth-First Search (แผนที่ไทย)
python "Depth-First SearchThai.py"

# Depth-First Search (แผนที่โรมาเนีย)
python "Depth-first search.py"

# Depth-Limited Search
python DLS.py

# Iterative Deepening Search
python IDS.py

# Uniform Cost Search
python UCS.py

# Best-First Search (แผนที่ไทย)
python "Best-First SearchThai.py"

# Best-First Search (แผนที่โรมาเนีย พร้อม verbose)
python "Best-First Search.py"

# Bidirectional Best-First Search
python ฺBiBF.py
```

### ขั้นตอนที่ 3: ปรับแต่งจุดเริ่มต้นและจุดหมาย

แก้ไขตัวแปรที่ส่วนท้ายของแต่ละไฟล์:

```python
# ตัวอย่างการปรับเปลี่ยน
START = "Bangkok"       # เปลี่ยนจุดเริ่มต้น
GOAL  = "ChiangMai"    # เปลี่ยนจุดหมาย
```

สำหรับ `DLS.py` สามารถปรับค่า depth limit ได้:

```python
limit = 6  # ปรับความลึกสูงสุดในการค้นหา
```

---

## ⚙️ ความต้องการของระบบ

| รายการ | รายละเอียด |
|---|---|
| **Python** | เวอร์ชัน 3.6 ขึ้นไป |
| **ไลบรารีที่ใช้** | `heapq` (built-in), `collections.deque` (built-in) |
| **ไลบรารีเพิ่มเติม** | ไม่จำเป็น — ใช้ไลบรารีมาตรฐานทั้งหมด |
| **ระบบปฏิบัติการ** | Windows, macOS, Linux |

---

## 📊 ตัวอย่างผลลัพธ์

### BFS: Bangkok → ChiangMai
```
🎯 เส้นทางที่สั้นที่สุด (จำนวนก้าวน้อยสุด) จาก Bangkok ไป ChiangMai:
Bangkok -> Ayutthaya -> Phitsanulok -> ChiangMai
🛣️ ระยะทางรวม: 780 กม.
```

### UCS: NakhonPathom → Ayutthaya
```
Path: NakhonPathom -> Bangkok -> Ayutthaya
Total distance: 140 km
```

### IDS: Pattaya → UdonThani
```
Depth = 0 -> cutoff
Depth = 1 -> cutoff
Depth = 2 -> cutoff
Depth = 3 -> cutoff
Depth = 4 -> cutoff
Depth = 5 -> ['Pattaya', 'Chonburi', 'Bangkok', 'Saraburi', 'NakhonRatchasima', 'KhonKaen', 'UdonThani']

Final Path: ['Pattaya', 'Chonburi', 'Bangkok', 'Saraburi', 'NakhonRatchasima', 'KhonKaen', 'UdonThani']
```

### Bidirectional: Saraburi → ChiangMai
```
Path: Saraburi -> Ayutthaya -> Phitsanulok -> ChiangMai
Total distance: 775 km
```

---

## 📋 ตารางเปรียบเทียบอัลกอริทึม

| อัลกอริทึม | ประเภท | สมบูรณ์ | เหมาะสม | โครงสร้างข้อมูล | Time Complexity | Space Complexity |
|---|---|---|---|---|---|---|
| **BFS** | Uninformed | ✅ | ✅ (ก้าว) | FIFO Queue | O(b^d) | O(b^d) |
| **DFS** | Uninformed | ❌* | ❌ | Stack (LIFO) | O(b^m) | O(bm) |
| **DLS** | Uninformed | ❌ | ❌ | Stack (LIFO) | O(b^l) | O(bl) |
| **IDS** | Uninformed | ✅ | ✅ (ก้าว) | Stack + DLS | O(b^d) | O(bd) |
| **UCS** | Uninformed | ✅ | ✅ (ต้นทุน) | Priority Queue | O(b^(1+⌊C*/ε⌋)) | O(b^(1+⌊C*/ε⌋)) |
| **Best-First** | Informed | ✅ | ขึ้นกับ f(n) | Priority Queue | ขึ้นกับ f(n) | ขึ้นกับ f(n) |
| **Bidirectional** | Both | ✅ | ✅ (ต้นทุน) | 2× Priority Queue | O(b^(d/2)) | O(b^(d/2)) |

> **b** = branching factor, **d** = ความลึกของคำตอบ, **m** = ความลึกสูงสุดของกราฟ, **l** = depth limit  
> **\*** DFS สมบูรณ์เมื่อใช้ reached set ป้องกัน cycle ในกราฟจำกัด

---
---

# 🇬🇧 English Version

## 🔍 Project Overview

This project is a collection of **7 pathfinding search algorithms** commonly studied in **Artificial Intelligence (AI)** courses, all implemented in Python.

These algorithms are applied to route-finding problems on two real-world-inspired road maps:
- **Thailand Road Map** — 14 provinces with distances in kilometers
- **Romania Road Map** — 20 cities with distances in miles (classic example from *Artificial Intelligence: A Modern Approach* by Stuart Russell & Peter Norvig)

### 🎯 Objectives

- Study and understand various graph search algorithms
- Compare the behavior of **Uninformed Search** vs. **Informed Search** strategies
- Apply them to realistic map data (Thailand & Romania)

---

## 📁 File Structure

```
📦 งาน RBE/
├── 📄 Best-First Search.py          # Best-First Search — Romania map (with verbose mode)
├── 📄 Best-First SearchThai.py      # Best-First Search — Thailand map
├── 📄 Depth-first search.py         # Depth-First Search (DFS) — Romania map (with verbose mode)
├── 📄 Depth-First SearchThai.py     # Depth-First Search (DFS) — Thailand map
├── 📄 ฺBFS1.py                      # Breadth-First Search (BFS) — Thailand map
├── 📄 DLS.py                        # Depth-Limited Search (DLS) — Thailand map
├── 📄 IDS.py                        # Iterative Deepening Search (IDS) — Thailand map
├── 📄 UCS.py                        # Uniform Cost Search (UCS) — Thailand map
├── 📄 ฺBiBF.py                      # Bidirectional Best-First Search — Thailand map
└── 📄 README.md                     # This documentation file
```

---

## 🧠 Algorithm Details

### 1. Breadth-First Search (BFS) — `ฺBFS1.py`

| Property | Details |
|---|---|
| **Type** | Uninformed Search |
| **Data Structure** | FIFO Queue (`collections.deque`) |
| **Principle** | Explores all nodes at the current depth level before moving to the next level |
| **Complete** | ✅ Yes — Guaranteed to find a solution if one exists |
| **Optimal** | ✅ Yes — Finds the path with the fewest steps (not necessarily shortest distance) |
| **Map** | Thailand |

---

### 2. Depth-First Search (DFS) — `Depth-first search.py` & `Depth-First SearchThai.py`

| Property | Details |
|---|---|
| **Type** | Uninformed Search |
| **Data Structure** | Stack (LIFO) |
| **Principle** | Explores as deep as possible along one branch before backtracking |
| **Complete** | ❌ No — May loop infinitely in cyclic graphs (mitigated with a `reached` set in this implementation) |
| **Optimal** | ❌ No — Does not guarantee the shortest path |
| **Map** | Romania (`Depth-first search.py`) and Thailand (`Depth-First SearchThai.py`) |

The Romania version uses a structured `RomaniaProblem` class with a `verbose` mode for step-by-step execution display.

---

### 3. Depth-Limited Search (DLS) — `DLS.py`

| Property | Details |
|---|---|
| **Type** | Uninformed Search |
| **Data Structure** | Stack (LIFO) |
| **Principle** | Same as DFS but with a maximum depth limit to prevent infinite exploration |
| **Complete** | ❌ No — Cannot find solutions deeper than the limit |
| **Optimal** | ❌ No |
| **Special Returns** | Returns `"cutoff"` when the depth limit is reached, or `"failure"` when no path exists |
| **Map** | Thailand |

---

### 4. Iterative Deepening Search (IDS) — `IDS.py`

| Property | Details |
|---|---|
| **Type** | Uninformed Search |
| **Data Structure** | Stack + iterative DLS calls |
| **Principle** | Repeatedly runs DLS with increasing depth limits (depth = 0, 1, 2, …) until a solution is found |
| **Complete** | ✅ Yes |
| **Optimal** | ✅ Yes — Finds the path with the fewest steps |
| **Key Advantage** | Combines the completeness of BFS with the low memory usage of DFS |
| **Map** | Thailand |

---

### 5. Uniform Cost Search (UCS) — `UCS.py`

| Property | Details |
|---|---|
| **Type** | Uninformed Search |
| **Data Structure** | Priority Queue (`heapq`) |
| **Principle** | Always expands the node with the **lowest cumulative path cost g(n)** |
| **Complete** | ✅ Yes |
| **Optimal** | ✅ Yes — Guaranteed to find the **least-cost** path |
| **Map** | Thailand |

---

### 6. Best-First Search — `Best-First Search.py` & `Best-First SearchThai.py`

| Property | Details |
|---|---|
| **Type** | Informed Search |
| **Data Structure** | Priority Queue (`heapq`) |
| **Principle** | Expands nodes based on an evaluation function **f(n)** (configurable; using `f(n) = path_cost` makes it behave like UCS) |
| **Complete** | ✅ Yes |
| **Optimal** | Depends on the chosen f(n) function |
| **Verbose Mode** | ✅ Available — Displays detailed step-by-step execution (frontier state, expanded nodes, etc.) |
| **Map** | Romania (`Best-First Search.py`) and Thailand (`Best-First SearchThai.py`) |

---

### 7. Bidirectional Best-First Search — `ฺBiBF.py`

| Property | Details |
|---|---|
| **Type** | Informed / Uninformed (uses UCS-style in both directions) |
| **Data Structure** | Two Priority Queues (Forward & Backward) |
| **Principle** | Simultaneously searches from the **start** and the **goal**; when both frontiers meet, the path is reconstructed |
| **Complete** | ✅ Yes |
| **Optimal** | ✅ Yes |
| **Key Advantage** | Dramatically reduces the number of explored nodes — search space decreases exponentially |
| **Map** | Thailand |

---

## 🗺️ Map Graph Data

### 🇹🇭 Thailand Map (14 Provinces)

A weighted undirected graph representing approximate road distances (in kilometers):

```
                        ChiangMai
                           |
                        (370 km)
                           |
                       Phitsanulok
                           |
                        (330 km)
                           |
          NakhonPathom---Bangkok---Ayutthaya---Saraburi---NakhonRatchasima---KhonKaen---UdonThani
            (60 km)     / |  \      (80 km)    (75 km)      (170 km)        (200 km)   (110 km)
               |      /   |   \
         Kanchanaburi /    |    Chonburi
          (130 km)  /   (200)    (85 km)
              |   /     km  \      |
         (95 km)        |    Pattaya---Rayong
                      HuaHin  (50 km)  (65 km)
```

**All 14 provinces:** Bangkok, Ayutthaya, NakhonPathom, Kanchanaburi, Chonburi, Pattaya, Rayong, HuaHin, Saraburi, NakhonRatchasima, KhonKaen, UdonThani, Phitsanulok, ChiangMai

---

### 🇷🇴 Romania Map (20 Cities)

The classic AIMA textbook graph with road distances in miles:

**All 20 cities:** Oradea, Zerind, Arad, Timisoara, Lugoj, Mehadia, Drobeta, Craiova, Sibiu, Rimnicu Vilcea, Fagaras, Pitesti, Bucharest, Giurgiu, Urziceni, Hirsova, Eforie, Vaslui, Iasi, Neamt

---

## 🚀 How to Use

### Step 1: Verify Python Installation

```bash
python --version
# Requires Python 3.6 or later
```

### Step 2: Run the Desired Algorithm

```bash
# Breadth-First Search
python ฺBFS1.py

# Depth-First Search (Thailand map)
python "Depth-First SearchThai.py"

# Depth-First Search (Romania map)
python "Depth-first search.py"

# Depth-Limited Search
python DLS.py

# Iterative Deepening Search
python IDS.py

# Uniform Cost Search
python UCS.py

# Best-First Search (Thailand map)
python "Best-First SearchThai.py"

# Best-First Search (Romania map, with verbose output)
python "Best-First Search.py"

# Bidirectional Best-First Search
python ฺBiBF.py
```

### Step 3: Customize Start & Goal

Edit the variables at the bottom of each file:

```python
# Example customization
START = "Bangkok"       # Change start city
GOAL  = "ChiangMai"    # Change goal city
```

For `DLS.py`, you can also adjust the depth limit:

```python
limit = 6  # Adjust maximum search depth
```

---

## ⚙️ System Requirements

| Item | Details |
|---|---|
| **Python** | Version 3.6 or later |
| **Libraries Used** | `heapq` (built-in), `collections.deque` (built-in) |
| **External Dependencies** | None — uses only Python standard library |
| **Operating System** | Windows, macOS, Linux |

---

## 📊 Example Output

### BFS: Bangkok → ChiangMai
```
🎯 เส้นทางที่สั้นที่สุด (จำนวนก้าวน้อยสุด) จาก Bangkok ไป ChiangMai:
Bangkok -> Ayutthaya -> Phitsanulok -> ChiangMai
🛣️ ระยะทางรวม: 780 กม.
```

### UCS: NakhonPathom → Ayutthaya
```
Path: NakhonPathom -> Bangkok -> Ayutthaya
Total distance: 140 km
```

### IDS: Pattaya → UdonThani
```
Depth = 0 -> cutoff
Depth = 1 -> cutoff
Depth = 2 -> cutoff
Depth = 3 -> cutoff
Depth = 4 -> cutoff
Depth = 5 -> ['Pattaya', 'Chonburi', 'Bangkok', 'Saraburi', 'NakhonRatchasima', 'KhonKaen', 'UdonThani']

Final Path: ['Pattaya', 'Chonburi', 'Bangkok', 'Saraburi', 'NakhonRatchasima', 'KhonKaen', 'UdonThani']
```

### Bidirectional: Saraburi → ChiangMai
```
Path: Saraburi -> Ayutthaya -> Phitsanulok -> ChiangMai
Total distance: 775 km
```

---

## 📋 Algorithm Comparison Table

| Algorithm | Type | Complete | Optimal | Data Structure | Time Complexity | Space Complexity |
|---|---|---|---|---|---|---|
| **BFS** | Uninformed | ✅ | ✅ (steps) | FIFO Queue | O(b^d) | O(b^d) |
| **DFS** | Uninformed | ❌* | ❌ | Stack (LIFO) | O(b^m) | O(bm) |
| **DLS** | Uninformed | ❌ | ❌ | Stack (LIFO) | O(b^l) | O(bl) |
| **IDS** | Uninformed | ✅ | ✅ (steps) | Stack + DLS | O(b^d) | O(bd) |
| **UCS** | Uninformed | ✅ | ✅ (cost) | Priority Queue | O(b^(1+⌊C*/ε⌋)) | O(b^(1+⌊C*/ε⌋)) |
| **Best-First** | Informed | ✅ | Depends on f(n) | Priority Queue | Depends on f(n) | Depends on f(n) |
| **Bidirectional** | Both | ✅ | ✅ (cost) | 2× Priority Queue | O(b^(d/2)) | O(b^(d/2)) |

> **b** = branching factor, **d** = depth of solution, **m** = maximum depth of graph, **l** = depth limit  
> **\*** DFS is complete when using a `reached` set to prevent cycles in finite graphs

---

## 📚 อ้างอิง | References

1. **Russell, S. & Norvig, P.** (2021). *Artificial Intelligence: A Modern Approach* (4th Edition). Pearson.
2. **Romania Map Problem** — Classic AI textbook example for pathfinding algorithms.
3. **Python Documentation** — [`heapq`](https://docs.python.org/3/library/heapq.html) | [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque)

---

<p align="center">
  <strong>Made with ❤️ for AI & Search Algorithms Study</strong><br>
  <em>สร้างด้วย ❤️ เพื่อการศึกษาอัลกอริทึมค้นหาทาง AI</em>
</p>
