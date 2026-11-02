# Pattern Recognition Guide

The goal is not to memorize 500 problems. It is to look at a new problem, spot **signals** in the statement, and map them to one of ~16 patterns. Re-read this file every week.

## Step 0: Read the constraints first (they tell you the target complexity)

| n (input size) | Target complexity | Typical approaches |
|---|---|---|
| n ≤ 10-12 | O(n!) | permutations, brute-force backtracking |
| n ≤ 20-25 | O(2ⁿ) | subsets, bitmask, backtracking |
| n ≤ 100 | O(n³) | 3 nested loops, Floyd-Warshall, DP with 3 dims |
| n ≤ 1,000-5,000 | O(n²) | 2D DP, pairs, nested loops |
| n ≤ 10⁵ - 10⁶ | O(n log n) or O(n) | sorting, heap, binary search, two pointers, sliding window, hashing |
| n ≤ 10⁹ or more | O(log n) or O(1) | binary search, math |

## Signal -> Pattern table

| If the problem says / looks like... | Think... |
|---|---|
| "find pair / complement / duplicates / count occurrences" | **HashMap / HashSet** |
| "subarray sum equals k", "range sum" | **Prefix sum + HashMap** |
| sorted array + pair/triplet, "palindrome", "in-place remove" | **Two pointers** |
| "longest/shortest **contiguous** subarray/substring with condition" | **Sliding window** |
| "next greater / smaller element", "histogram", "temperatures" | **Monotonic stack** |
| brackets, nesting, undo/evaluate expression | **Stack** |
| sorted input, "O(log n)", rotated array | **Binary search** |
| "minimize the maximum" / "maximize the minimum" / "smallest x such that feasible" | **Binary search on answer** |
| linked list: cycle, middle, nth from end | **Fast/slow pointers, dummy head** |
| linked list reversal / reorder | **In-place reversal** |
| tree: depth, diameter, path sum, validate, LCA | **DFS recursion (what do I return? what do I pass down?)** |
| tree: level order, right side view, min depth | **BFS with queue** |
| "top K", "K-th largest", "median of stream", "merge K sorted" | **Heap** |
| "all subsets / permutations / combinations / generate all valid ..." | **Backtracking** |
| grid + islands/regions/connected components | **DFS/BFS flood fill** |
| "shortest path / minimum steps" in unweighted graph or grid | **BFS** |
| "shortest path" with weights >= 0 | **Dijkstra** |
| "prerequisites / dependencies / order of tasks / detect cycle in directed graph" | **Topological sort** |
| "connected?", "merge groups", "redundant edge" | **Union-Find** |
| "prefix / dictionary of words / autocomplete" | **Trie** |
| "minimum/maximum/number of ways", overlapping subproblems, choices at each step | **Dynamic programming** |
| "two strings" (LCS, edit distance, interleave) | **2D DP** |
| "can you reach / jump / schedule / intervals" | **Greedy (+ sort)** |
| "merge / overlap / meeting rooms" | **Sort intervals by start (or end)** |
| "appears once while others twice", parity, powers of two | **Bit manipulation (XOR)** |
| "design a data structure with O(1) ..." | **HashMap + (list / array / DLL)** |

## The 5-minute pattern checklist (do this before writing any code)

1. What is the **input structure**? (array, string, tree, graph, intervals, matrix)
2. Is it **sorted** or can I sort it? (-> two pointers, binary search, greedy)
3. Do they want **contiguous** things? (-> sliding window, prefix sums, Kadane)
4. Do they want **all** solutions or **one best** value or **count**? (all -> backtracking, best/count -> DP/greedy)
5. Does the problem have a **graph hiding inside**? (cells = nodes, words = nodes, tasks = nodes)
6. Can I describe the answer for size n using the answer for size n-1 / smaller part? (-> recursion/DP)
7. State the brute force and its complexity, then ask: *what repeated work can I remove?*

---

# C++ Templates

Do not paste these blindly. Retype each one from memory until it is automatic.

## 1. Prefix sum + hashmap (subarray sum = k)
```cpp
unordered_map<int,int> cnt{{0,1}};
int sum = 0, ans = 0;
for (int x : nums) {
    sum += x;
    if (cnt.count(sum - k)) ans += cnt[sum - k];
    cnt[sum]++;
}
```

## 2. Two pointers (sorted, pair sum)
```cpp
int l = 0, r = n - 1;
while (l < r) {
    int s = a[l] + a[r];
    if (s == target) { /* found */ l++; r--; }
    else if (s < target) l++;
    else r--;
}
```

## 3. Sliding window (variable size)
```cpp
int l = 0, ans = 0;
for (int r = 0; r < n; r++) {
    // add a[r] to window state
    while (/* window invalid */) {
        // remove a[l] from window state
        l++;
    }
    ans = max(ans, r - l + 1);
}
```

## 4. Monotonic stack (next greater element)
```cpp
vector<int> res(n, -1);
stack<int> st; // indices; values decreasing from bottom to top
for (int i = 0; i < n; i++) {
    while (!st.empty() && a[st.top()] < a[i]) {
        res[st.top()] = i;   // a[i] is the next greater for st.top()
        st.pop();
    }
    st.push(i);
}
```

## 5. Binary search: smallest x where ok(x) is true
```cpp
int lo = LOW, hi = HIGH;          // answer is guaranteed in [lo, hi]
while (lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if (ok(mid)) hi = mid;        // mid could be the answer
    else lo = mid + 1;
}
return lo;
```
Use the same shape for "binary search on answer" (Koko, ship packages): `ok(x)` = "is x feasible?".

## 6. Linked list: dummy head + fast/slow
```cpp
ListNode dummy(0, head);
ListNode* cur = &dummy;
// fast/slow
ListNode *slow = head, *fast = head;
while (fast && fast->next) { slow = slow->next; fast = fast->next->next; }
```
Reverse:
```cpp
ListNode *prev = nullptr, *cur = head;
while (cur) { auto nxt = cur->next; cur->next = prev; prev = cur; cur = nxt; }
return prev;
```

## 7. Tree DFS (return a value, update a global)
```cpp
int ans = 0;
int dfs(TreeNode* node) {
    if (!node) return 0;
    int l = dfs(node->left), r = dfs(node->right);
    ans = max(ans, l + r);        // best path THROUGH this node
    return 1 + max(l, r);         // best path going UP from this node
}
```

## 8. Tree BFS (level order)
```cpp
queue<TreeNode*> q;
if (root) q.push(root);
while (!q.empty()) {
    int sz = q.size();
    for (int i = 0; i < sz; i++) {
        auto* n = q.front(); q.pop();
        if (n->left) q.push(n->left);
        if (n->right) q.push(n->right);
    }
    // one level finished here
}
```

## 9. Heap: top K
```cpp
priority_queue<int, vector<int>, greater<int>> pq;  // min-heap
for (int x : nums) {
    pq.push(x);
    if ((int)pq.size() > k) pq.pop();               // keep K largest
}
// pq.top() is the K-th largest
```

## 10. Backtracking
```cpp
vector<vector<int>> res;
vector<int> path;
void dfs(int start) {
    res.push_back(path);                        // for subsets; for "complete" solutions check a condition
    for (int i = start; i < n; i++) {
        if (i > start && a[i] == a[i-1]) continue;  // skip duplicates (needs sorted a)
        path.push_back(a[i]);                   // choose
        dfs(i + 1);                             // explore (i, not i+1, if reuse is allowed)
        path.pop_back();                        // un-choose
    }
}
```

## 11. Grid DFS / BFS
```cpp
int dr[4] = {1, -1, 0, 0}, dc[4] = {0, 0, 1, -1};
void dfs(vector<vector<char>>& g, int r, int c) {
    if (r < 0 || c < 0 || r >= (int)g.size() || c >= (int)g[0].size() || g[r][c] != '1') return;
    g[r][c] = '0';                              // mark visited
    for (int d = 0; d < 4; d++) dfs(g, r + dr[d], c + dc[d]);
}
```
Multi-source BFS: push **all** sources into the queue first, then run BFS level by level.

## 12. Topological sort (Kahn's algorithm)
```cpp
vector<vector<int>> adj(n);
vector<int> indeg(n, 0);
for (auto& e : edges) { adj[e[1]].push_back(e[0]); indeg[e[0]]++; }   // e = {course, prereq}
queue<int> q;
for (int i = 0; i < n; i++) if (indeg[i] == 0) q.push(i);
vector<int> order;
while (!q.empty()) {
    int u = q.front(); q.pop();
    order.push_back(u);
    for (int v : adj[u]) if (--indeg[v] == 0) q.push(v);
}
bool possible = (int)order.size() == n;        // false => cycle
```

## 13. Union-Find
```cpp
vector<int> parent(n), rnk(n, 0);
iota(parent.begin(), parent.end(), 0);
function<int(int)> find = [&](int x) { return parent[x] == x ? x : parent[x] = find(parent[x]); };
auto unite = [&](int a, int b) {
    a = find(a); b = find(b);
    if (a == b) return false;                   // already connected
    if (rnk[a] < rnk[b]) swap(a, b);
    parent[b] = a;
    if (rnk[a] == rnk[b]) rnk[a]++;
    return true;
};
```

## 14. Dijkstra
```cpp
vector<vector<pair<int,int>>> adj(n);           // {neighbor, weight}
vector<int> dist(n, INT_MAX);
priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;   // {dist, node}
dist[src] = 0; pq.push({0, src});
while (!pq.empty()) {
    auto [d, u] = pq.top(); pq.pop();
    if (d > dist[u]) continue;                  // stale entry
    for (auto [v, w] : adj[u])
        if (dist[u] + w < dist[v]) { dist[v] = dist[u] + w; pq.push({dist[v], v}); }
}
```

## 15. Trie
```cpp
struct Trie {
    Trie* next[26] = {};
    bool end = false;
    void insert(const string& w) {
        Trie* p = this;
        for (char ch : w) {
            if (!p->next[ch - 'a']) p->next[ch - 'a'] = new Trie();
            p = p->next[ch - 'a'];
        }
        p->end = true;
    }
};
```

## 16. Dynamic programming (the 4 questions)
1. **State**: what does `dp[i]` / `dp[i][j]` mean in plain English?
2. **Transition**: how do I compute it from smaller states?
3. **Base case**: what is the smallest answer?
4. **Order & answer**: which direction do I fill, and where is the final answer?

```cpp
// 1D: Coin Change (min coins)
vector<int> dp(amount + 1, INT_MAX);
dp[0] = 0;
for (int a = 1; a <= amount; a++)
    for (int c : coins)
        if (a >= c && dp[a - c] != INT_MAX) dp[a] = min(dp[a], dp[a - c] + 1);

// 2D: Longest Common Subsequence
vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
for (int i = 1; i <= m; i++)
    for (int j = 1; j <= n; j++)
        dp[i][j] = (s[i-1] == t[j-1]) ? dp[i-1][j-1] + 1 : max(dp[i-1][j], dp[i][j-1]);
```
**DP families to recognize:** Fibonacci-like (climb stairs, rob), knapsack (0/1: partition subset; unbounded: coin change), grid paths, two-string (LCS, edit distance), LIS, palindromes (expand/interval), state machine (stocks).

## 17. Intervals
```cpp
sort(iv.begin(), iv.end());
vector<vector<int>> merged;
for (auto& x : iv) {
    if (merged.empty() || merged.back()[1] < x[0]) merged.push_back(x);
    else merged.back()[1] = max(merged.back()[1], x[1]);
}
```

---

## Common bug checklist (read before submitting)
- Integer overflow: use `long long` for sums/products; `lo + (hi - lo) / 2` for mid.
- Off-by-one on loop bounds, `<` vs `<=` in binary search.
- Empty input, single element, all equal, negative numbers, duplicates.
- Null pointers in linked lists and trees.
- Forgetting to mark visited **before** pushing to the BFS queue.
- Modifying a container while iterating over it.
- Forgetting to un-choose in backtracking.
