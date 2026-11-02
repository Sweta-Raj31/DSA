# C++ for DSA: Cheat Sheet (for a Go developer)

## Go -> C++ mapping

| Go | C++ | Notes |
|---|---|---|
| `[]int` (slice) | `vector<int>` | `v.push_back(x)`, `v.pop_back()`, `v.size()`, `v.back()` |
| `[5]int` | `array<int,5>` or `int a[5]` | |
| `make([]int, n)` | `vector<int> v(n)` (zeros) / `vector<int> v(n, -1)` | |
| 2D slice | `vector<vector<int>> g(m, vector<int>(n, 0))` | |
| `map[int]int` | `unordered_map<int,int>` | avg O(1). `m[k]++` works (default 0) |
| ordered map (none in Go) | `map<int,int>` | sorted keys, O(log n); `lower_bound`, `begin()`, `rbegin()` |
| `map[int]struct{}` | `unordered_set<int>` / `set<int>` | `s.count(x)`, `s.insert(x)`, `s.erase(x)` |
| `container/heap` (boilerplate) | `priority_queue<int>` (max-heap) | min-heap: `priority_queue<int, vector<int>, greater<int>>` |
| slice as queue | `queue<int>` / `deque<int>` | `push`, `front`, `pop`; deque has `push_front`, `back` |
| slice as stack | `stack<int>` | `push`, `top`, `pop` (pop returns nothing!) |
| `sort.Ints(a)` | `sort(a.begin(), a.end())` | |
| `sort.Slice(a, less)` | `sort(a.begin(), a.end(), [](auto& x, auto& y){ return x[0] < y[0]; })` | |
| `sort.SearchInts` | `lower_bound(a.begin(), a.end(), x)` | returns iterator; index = `it - a.begin()` |
| `strings.Builder` | `string s; s += c;` | strings are mutable |
| `[]byte(s)` | `s[i]` is a `char` | `s.substr(pos, len)`, `s.find(t)` |
| `math.MaxInt64` | `LLONG_MAX` / `INT_MAX` | beware overflow: `INT_MAX + 1` is UB |
| `min(a,b)` | `min(a,b)` | both args must be same type |
| struct | `struct P { int x, y; };` | or `pair<int,int>`, `tuple<int,int,int>` |
| `nil` | `nullptr` | |
| garbage collection | **you manage memory** | for DSA problems, `new` without `delete` is fine |
| `for i, v := range a` | `for (int i = 0; i < a.size(); i++)` / `for (auto v : a)` | cast `a.size()` to `int` to avoid unsigned bugs |
| multiple return | `pair` / `tuple` / structured bindings: `auto [a, b] = f();` | |

## Include everything (practice and LeetCode)
```cpp
#include <bits/stdc++.h>
using namespace std;
```
(GCC-specific. In a real interview, using specific headers is also fine. Ask the interviewer.)

## Common gotchas
- `size()` is **unsigned**. `a.size() - 1` on an empty vector wraps around. Use `(int)a.size()`.
- `stack::pop()` / `queue::pop()` return nothing. Read `top()` / `front()` first.
- `unordered_map::operator[]` **inserts** a key if missing. Use `.count(k)` or `.find(k)` to check.
- `int` is 32-bit (about 2.1e9). Use `long long` when summing or multiplying.
- Passing a vector by value copies it. Use `vector<int>& v` (or `const vector<int>&`).
- `string + char` is fine, `char + char` is an int. `'a' + 1` is `98`, not `"b"`.
- `a[i] - '0'` converts a digit char to int; `'a' + k` builds a char.
- Integer division truncates toward zero; `%` with negatives can be negative.

## Handy snippets
```cpp
// swap, min/max
swap(a[i], a[j]);   *max_element(a.begin(), a.end());   accumulate(a.begin(), a.end(), 0LL);

// reverse, unique, fill, iota
reverse(a.begin(), a.end());
a.erase(unique(a.begin(), a.end()), a.end());     // after sort: remove duplicates
fill(dp.begin(), dp.end(), -1);
iota(p.begin(), p.end(), 0);                      // 0,1,2,...

// custom priority queue ordering (by second, smallest first)
auto cmp = [](const pair<int,int>& a, const pair<int,int>& b) { return a.second > b.second; };
priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(cmp)> pq(cmp);

// lower_bound / upper_bound on sorted vector
int idx = lower_bound(a.begin(), a.end(), x) - a.begin();   // first >= x
int idy = upper_bound(a.begin(), a.end(), x) - a.begin();   // first > x

// sort by multiple keys
sort(v.begin(), v.end(), [](auto& a, auto& b) { return a.first != b.first ? a.first < b.first : a.second > b.second; });

// string <-> number
int n = stoi("123");   string s = to_string(123);

// count set bits, check power of two
__builtin_popcount(x);   (x > 0 && (x & (x - 1)) == 0);

// compile & run
// g++ -std=c++17 -O2 -Wall -o sol solutions/arrays-hashing/0001-two-sum.cpp && ./sol
```

## Complexity of STL operations (memorize)
| Structure | Insert | Find | Erase | Notes |
|---|---|---|---|---|
| `vector` | O(1) amortized at end | O(n) | O(n) | random access O(1) |
| `deque` | O(1) both ends | O(n) | | random access O(1) |
| `unordered_map/set` | O(1) avg | O(1) avg | O(1) avg | worst O(n) |
| `map/set` | O(log n) | O(log n) | O(log n) | sorted, ordered iteration |
| `priority_queue` | O(log n) | top O(1) | pop O(log n) | no random removal |
| `sort` | O(n log n) | | | |
