# 16-Week Roadmap (Beginner -> FAANG-ready)

**Assumptions:** ~2 hours on weekdays + ~4-5 hours on weekends ≈ 12-14 hours/week. If you have less time, stretch each phase (the order matters more than the speed). If you have more, compress.

**Rule of thumb:** quality over quantity. ~100 core problems solved *properly* (understood, re-solved, pattern named) beat 400 problems skimmed.

---

## Phase 0: Setup (Week 0, 2-3 days)

- [ ] Create this repo on GitHub, push it, read `README.md`
- [ ] Install a C++ compiler (g++ / clang), verify with `g++ --version`
- [ ] Read `docs/CPP_CHEATSHEET.md` (Go -> C++ mapping) and write 5 tiny programs using `vector`, `unordered_map`, `set`, `priority_queue`, `sort` with a lambda
- [ ] Learn Big-O: loops, nested loops, recursion, sorting = O(n log n), hashing = O(1) average. You must be able to state time and space for every solution
- [ ] Create a LeetCode account. Set a fixed daily slot on your calendar (same time every day)

---

## Phase 1: Foundations (Weeks 1-4)

### Week 1: Arrays & Hashing
- **Learn:** HashMap/HashSet, frequency counting, prefix sums
- **Do:** all of section 1 in `PROBLEMS.md` (8 problems)
- **Goal:** solve Two Sum / Group Anagrams without looking at anything

### Week 2: Two Pointers + Sliding Window
- **Learn:** opposite-end pointers, slow/fast pointers, fixed vs variable window
- **Do:** sections 2 and 3 (core first: ~10 problems), the rest if time allows
- **Goal:** explain *why* a window is valid/invalid in one sentence

### Week 3: Stack + Binary Search
- **Learn:** monotonic stack, binary search on index and on answer
- **Do:** sections 4 and 5 (core ~14 problems)
- **Goal:** write binary search without off-by-one bugs, using the template in `PATTERNS.md`

### Week 4: Linked List + **Checkpoint 1**
- **Learn:** dummy node, reversal, fast/slow, Floyd cycle detection
- **Do:** section 6 (core 8 problems). Implement LRU Cache from memory
- **Checkpoint 1 (weekend):** pick 4 random Easy/Medium problems from weeks 1-4 you have *not* solved. 45 minutes each. Score yourself: how many did you solve alone? Log it in `PROGRESS.md`

---

## Phase 2: Core Data Structures (Weeks 5-8)

### Week 5: Trees I
- **Learn:** recursion on trees, DFS vs BFS, pre/in/post-order
- **Do:** section 7, first 10-11 problems (depth, diameter, same tree, level order, right side view, good nodes)

### Week 6: Trees II + Heap
- **Learn:** BST properties, "what do I return vs pass down", priority_queue
- **Do:** rest of section 7 (validate BST, kth smallest, construct tree, LCA, max path sum) and section 8 (core)

### Week 7: Backtracking
- **Learn:** the choose/explore/un-choose template, pruning, duplicate skipping
- **Do:** section 9 (core 6 problems). Draw the recursion tree on paper for Subsets and Permutations

### Week 8: Graphs I + **Checkpoint 2**
- **Learn:** adjacency list, BFS vs DFS, grid as graph, multi-source BFS
- **Do:** section 10 problems: Number of Islands, Clone Graph, Pacific Atlantic, Rotting Oranges, Number of Provinces
- **Checkpoint 2 (weekend):** 3 random Mediums, 40 min each, timed, no hints. Target: 2 of 3

---

## Phase 3: Advanced Patterns (Weeks 9-12)

### Week 9: Graphs II
- **Learn:** topological sort (Kahn), Union-Find, Dijkstra
- **Do:** rest of section 10 (Course Schedule I/II, Redundant Connection, Word Ladder, Network Delay Time)

### Week 10: Tries + Greedy + Intervals
- **Learn:** trie node design, sort-then-greedy, exchange arguments
- **Do:** section 11 (core 2) and section 14 (core 3)

### Week 11: Dynamic Programming I (1D)
- **Learn:** the 4 DP questions (state, transition, base case, order). Always write recursion + memo **first**, then convert to bottom-up
- **Do:** section 12 (core 12 problems). This is the hardest week; do not rush it

### Week 12: Dynamic Programming II (2D) + **Checkpoint 3**
- **Learn:** grid DP, two-string DP, knapsack variants
- **Do:** section 13 (core 4). Redo 3 problems from week 11 without notes
- **Checkpoint 3 (weekend):** 2 Mediums + 1 Hard, 90 minutes total, timed

---

## Phase 4: Polish and Interview Simulation (Weeks 13-16)

### Week 13: Bit / Math / Matrix + Design + Revision
- **Do:** section 15 core (Single Number, Rotate Image, Spiral Matrix), section 16 (Insert Delete GetRandom)
- **Revise:** every problem you marked "struggled" in `PROGRESS.md`. Re-solve from a blank file

### Week 14: Mixed Practice (pattern *recognition* training)
- Pick random unsolved Mediums (LeetCode "Random" / company tag lists). **Before coding, write the pattern name and why** (30 sec). Then solve
- 1 problem/day timed at 35 min + 1 problem/day untimed review of mistakes
- 2 mock interviews this weekend (see "Mock interviews" below)

### Week 15: Company-style Practice + System Design Basics
- 5 days: 1-2 Mediums/day from the company-tagged lists (Amazon, Google, Meta, Microsoft) for the company you are targeting
- Spend ~4 hours this week on the non-DSA rounds (see below)
- 2 mock interviews

### Week 16: Final Revision + Rest
- Re-solve the 20 problems you found hardest (from `PROGRESS.md`)
- Re-read `PATTERNS.md` fully, retype 8 templates from memory
- 2 mock interviews, then **rest the day before** any real interview

---

## Weekly routine (follow it every week)

| Day | What |
|---|---|
| Mon-Thu | 2-3 new problems with the 6-step loop (see README). Log each in `PROGRESS.md` |
| Fri | Re-solve 2 problems from earlier weeks that you struggled with (spaced repetition) |
| Sat | Longer session: harder problems of the current pattern, or the checkpoint |
| Sun | Review: update checkboxes, run `python3 scripts/progress.py`, commit + push, plan the next week (30-45 min) |

## Spaced repetition (this is what makes patterns stick)
For every problem you struggled with, re-solve from a blank file after **1 day -> 7 days -> 30 days**. If you solve it cleanly without hints, you can retire it. Put the due dates in `PROGRESS.md` -> *Revision Queue*.

## Mock interviews
Talk out loud, as in a real interview: clarify -> examples -> brute force -> optimize -> code -> dry run -> complexity. Use Pramp (free peer mocks), interviewing.io, or a friend. Do your first mock around Week 8, and then one a week from Week 13.

## Beyond DSA (important for 2.5 YoE roles, SDE-2 / L4 / SDE II)
Even if your plan is DSA-first, don't ignore these. Start in Week 12:
- **Low-level design / machine coding:** design a parking lot, LRU cache, rate limiter, elevator, tic-tac-toe. You work in Go, so you may already have an edge here
- **System design (basics):** load balancers, caching, DB indexing/sharding, queues, rate limiting. Start with the standard "design a URL shortener / news feed / chat" walkthroughs
- **Behavioral:** prepare 6-8 stories (conflict, failure, ownership, deadline, leading a feature, disagreeing with a manager) using STAR. Amazon is especially strict about this
- **Your resume:** be ready to explain every line of your Go projects in depth

## When you get stuck
1. Time-box: **25 minutes** of real effort (pen and paper first)
2. Take only a **hint** (the pattern name or one key observation), not the solution
3. Still stuck after another 15 minutes -> read the editorial/video **fully**, understand it, close it
4. Re-code it from scratch **without looking**, and add it to the revision queue
5. Write 2 lines in the solution file header: *what was the signal I missed?*

## Success metrics (how you know you are ready)
- You can solve a *new* Medium in ~25-30 minutes about 60-70% of the time
- You can name the pattern in under 2 minutes
- You can state time/space complexity without thinking
- You can solve Easy problems in ~10 min and explain your approach clearly out loud
