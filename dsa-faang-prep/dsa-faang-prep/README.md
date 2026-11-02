# DSA for FAANG: Pattern-Based Prep

> Goal: crack any DSA problem by **recognizing the pattern**, using a **minimal, curated set of problems**, with a clear plan and visible progress.

| | |
|---|---|
| **Profile** | Software Engineer, 2.5 YoE (Go), preparing for FAANG-level interviews |
| **Language for DSA** | **C++** (see why below) |
| **Duration** | 16 weeks (~12-14 hrs/week) |
| **Problems** | 147 curated, of which **96 are core** |

---

## Progress dashboard

<!-- PROGRESS:START -->
**Overall: 0/147 solved** (0%)  |  **Core: 0/96** (0%)

`░░░░░░░░░░░░░░░░░░░░` core progress

| Pattern | Solved | Core | Progress |
|---|---|---|---|
| Arrays & Hashing | 0/8 | 0/8 | `░░░░░░░░░░` |
| Two Pointers | 0/8 | 0/5 | `░░░░░░░░░░` |
| Sliding Window | 0/8 | 0/6 | `░░░░░░░░░░` |
| Stack & Monotonic Stack | 0/7 | 0/5 | `░░░░░░░░░░` |
| Binary Search | 0/9 | 0/7 | `░░░░░░░░░░` |
| Linked List | 0/12 | 0/8 | `░░░░░░░░░░` |
| Trees & BST | 0/17 | 0/13 | `░░░░░░░░░░` |
| Heap / Priority Queue | 0/7 | 0/4 | `░░░░░░░░░░` |
| Backtracking | 0/10 | 0/6 | `░░░░░░░░░░` |
| Graphs | 0/16 | 0/10 | `░░░░░░░░░░` |
| Tries | 0/3 | 0/2 | `░░░░░░░░░░` |
| Dynamic Programming - 1D | 0/15 | 0/12 | `░░░░░░░░░░` |
| Dynamic Programming - 2D | 0/7 | 0/4 | `░░░░░░░░░░` |
| Greedy & Intervals | 0/7 | 0/3 | `░░░░░░░░░░` |
| Bit Manipulation, Math & Matrix | 0/11 | 0/3 | `░░░░░░░░░░` |
| Design (Data Structure Design) | 0/2 | 0/0 | `░░░░░░░░░░` |
<!-- PROGRESS:END -->

---

## Which language should I use? -> C++

You know basic C++ from college and work in Go. For interview DSA, **use C++**:

| | C++ | Go |
|---|---|---|
| Heap / priority queue | `priority_queue` built in | needs ~15 lines of `container/heap` interface boilerplate every time |
| Sorted map / set (`lower_bound`, floor/ceiling) | `map`, `set` built in | not in the standard library |
| Deque, stack, queue | built in | hand-rolled with slices |
| Sort with custom comparator, binary search | one-liners (`sort`, `lower_bound`) | OK, but more verbose |
| Typing speed in a 35-minute round | fast | noticeably slower on DS-heavy problems |
| Accepted by FAANG | yes | yes, but few interviewers know Go idioms well |

Go is **allowed** at every FAANG company. But in a timed round, every minute of boilerplate counts, and the STL gives you every data structure you need. You do not need "advanced C++". You need: `vector`, `string`, `unordered_map/set`, `map/set`, `stack/queue/deque`, `priority_queue`, `sort`, `lower_bound`, lambdas, structs, pointers (for linked lists/trees). That is roughly a weekend to refresh with `docs/CPP_CHEATSHEET.md`.

> If you really prefer Go or Python, the plan is identical. Just keep **one language for the whole 16 weeks**. Do not switch midway.

---

## How to work on each problem: the 6-step loop

This loop is what builds pattern recognition. Do **not** skip steps, even for Easy problems.

1. **Understand (3 min):** restate the problem. Write 2 examples + 1 edge case. Read the constraints and decide the target complexity (`PATTERNS.md`, Step 0).
2. **Pattern (5 min):** use the signal table in `PATTERNS.md`. Write down your guess: *"This looks like ___ because ___."*
3. **Brute force first (3 min):** state it and its complexity. Then ask: *what repeated work can I remove?*
4. **Code (15 min):** write it in C++, clean and compiling. Talk out loud as if in an interview.
5. **Test (5 min):** dry-run on the examples and your edge case by hand. State time and space.
6. **Log (3 min):** `python3 scripts/new.py <num> <slug> <folder>` scaffolds the file. Fill the header (pattern, signal, idea, mistakes). Add a row in `PROGRESS.md`. Tick the box in `PROBLEMS.md` **only when you can re-solve it without hints**.

**Stuck rule:** 25 minutes of real effort -> take a hint (not the solution) -> 15 more minutes -> read the editorial -> close it -> re-code from scratch the next day.

---

## Repo layout

```
.
├── README.md              <- you are here (+ auto-updated dashboard)
├── ROADMAP.md             <- 16-week plan, week by week, with checkpoints
├── PATTERNS.md            <- signal -> pattern table + C++ templates (re-read weekly)
├── PROBLEMS.md            <- 147 curated problems with checkboxes (the tracker)
├── PROGRESS.md            <- daily log, revision queue, mock interviews
├── docs/
│   └── CPP_CHEATSHEET.md  <- Go -> C++ mapping, STL gotchas
├── templates/
│   └── solution.cpp       <- header template for every solution file
├── scripts/
│   ├── progress.py        <- recomputes the dashboard from PROBLEMS.md
│   └── new.py             <- scaffolds solutions/<pattern>/NNNN-slug.cpp
└── solutions/             <- your code, grouped by pattern
    ├── arrays-hashing/
    ├── two-pointers/
    └── ... (16 folders)
```

---

## Quick start

```bash
# 1. Create an empty repo on GitHub named dsa-faang-prep (no README), then:
cd dsa-faang-prep
git init
git add .
git commit -m "Initial commit: DSA prep roadmap"
git branch -M main
git remote add origin https://github.com/Sweta-Raj31/dsa-faang-prep.git
git push -u origin main

# 2. Start a problem
python3 scripts/new.py 1 two-sum arrays-hashing
g++ -std=c++17 -O2 -Wall -o /tmp/sol solutions/arrays-hashing/0001-two-sum.cpp && /tmp/sol

# 3. Tick it in PROBLEMS.md, then refresh the dashboard and push
python3 scripts/progress.py
git add . && git commit -m "Solve 0001 two-sum" && git push
```

**Daily habit:** commit after every problem. Your GitHub contribution graph becomes visible proof of consistency, and recruiters do look at it.

---

## The patterns you will master (16)

1. Arrays & Hashing · 2. Two Pointers · 3. Sliding Window · 4. Stack / Monotonic Stack · 5. Binary Search · 6. Linked List · 7. Trees & BST · 8. Heap · 9. Backtracking · 10. Graphs (BFS/DFS, Topo, Union-Find, Dijkstra) · 11. Tries · 12. DP 1D · 13. DP 2D · 14. Greedy & Intervals · 15. Bit / Math / Matrix · 16. Design

Each has a 5-10 line template in `PATTERNS.md`.

---

## Resources (pick **one** per topic, don't hoard)

- **Problem order / explanations:** NeetCode roadmap and videos (his lists are the basis of this set)
- **Concepts, if you need a deeper dive:** Striver's A2Z sheet (C++), or the "Grokking the Coding Interview" patterns
- **Mock interviews:** Pramp, interviewing.io
- **Book (optional):** *Cracking the Coding Interview*, for the interview process and communication

---

## Mindset

- **Consistency > intensity.** 2 hours daily beats 14 hours on Sunday.
- **Struggle is the learning.** If every problem feels easy, you are reading editorials too early.
- **Re-solving is where learning happens.** A problem you solved once and never revisited is mostly forgotten in 2 weeks.
- **Talk out loud.** The interview tests communication as much as the code.
- **Track, don't compare.** Your only competitor is last month's you.
