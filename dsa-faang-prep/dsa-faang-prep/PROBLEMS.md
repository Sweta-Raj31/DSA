# Problem Tracker

Tick a box (`- [ ]` -> `- [x]`) when you can **re-solve the problem from scratch without hints**. Then run `python3 scripts/progress.py` to refresh the dashboard in the README.

- ⭐ = **core** problem (do these first; they cover every pattern with minimum effort)
- No star = extra practice for when you want more reps on a pattern
- Difficulty: Easy / Medium / Hard


## 1. Arrays & Hashing

> Trade space for time. HashMap/HashSet for O(1) lookup, prefix sums for range queries.

> Solutions folder: `solutions/arrays-hashing/`

- [ ] ⭐ [1. Two Sum](https://leetcode.com/problems/two-sum/) - Easy - _store complement in hashmap_
- [ ] ⭐ [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) - Easy - _hashset_
- [ ] ⭐ [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/) - Easy - _frequency array of 26_
- [ ] ⭐ [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/) - Medium - _sorted string / count signature as key_
- [ ] ⭐ [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) - Medium - _freq map + heap or bucket sort_
- [ ] ⭐ [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) - Medium - _prefix * suffix products_
- [ ] ⭐ [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) - Medium - _set + only start from sequence beginnings_
- [ ] ⭐ [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) - Medium - _prefix sum + hashmap of counts_

## 2. Two Pointers

> Sorted array / pair search / in-place partition. Move pointers based on a comparison.

> Solutions folder: `solutions/two-pointers/`

- [ ] ⭐ [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) - Easy - _opposite ends_
- [ ] ⭐ [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) - Medium - _opposite ends on sorted_
- [ ] ⭐ [15. 3Sum](https://leetcode.com/problems/3sum/) - Medium - _sort + fix one + two pointers, skip duplicates_
- [ ] ⭐ [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/) - Medium - _move the shorter side_
- [ ] ⭐ [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) - Hard - _left max / right max, two pointers_
- [ ] [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) - Easy - _slow/fast write pointer_
- [ ] [75. Sort Colors](https://leetcode.com/problems/sort-colors/) - Medium - _Dutch national flag (3 pointers)_
- [ ] [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) - Easy - _slow/fast write pointer_

## 3. Sliding Window

> Contiguous subarray/substring with a condition. Expand right, shrink left while invalid.

> Solutions folder: `solutions/sliding-window/`

- [ ] ⭐ [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) - Easy - _track min so far_
- [ ] ⭐ [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) - Medium - _window + last-seen index_
- [ ] ⭐ [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) - Medium - _window size - maxFreq <= k_
- [ ] ⭐ [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/) - Medium - _fixed window + freq compare_
- [ ] ⭐ [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) - Hard - _need/have counters, shrink when valid_
- [ ] ⭐ [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) - Hard - _monotonic deque_
- [ ] [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) - Easy - _fixed-size window_
- [ ] [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) - Medium - _variable window, positives only_

## 4. Stack & Monotonic Stack

> Matching/nesting problems, and 'next greater/smaller element' (monotonic stack).

> Solutions folder: `solutions/stack/`

- [ ] ⭐ [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) - Easy - _stack of openers_
- [ ] ⭐ [155. Min Stack](https://leetcode.com/problems/min-stack/) - Medium - _pair (val, min so far)_
- [ ] ⭐ [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) - Medium - _monotonic decreasing stack of indices_
- [ ] [150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) - Medium - _operand stack_
- [ ] ⭐ [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) - Hard - _monotonic increasing stack_
- [ ] [853. Car Fleet](https://leetcode.com/problems/car-fleet/) - Medium - _sort by position, compare arrival times_
- [ ] ⭐ [394. Decode String](https://leetcode.com/problems/decode-string/) - Medium - _stack of (count, prefix string)_

## 5. Binary Search

> Sorted/monotonic structure -> O(log n). Also 'binary search on the answer' when feasibility is monotonic.

> Solutions folder: `solutions/binary-search/`

- [ ] ⭐ [704. Binary Search](https://leetcode.com/problems/binary-search/) - Easy - _template_
- [ ] ⭐ [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) - Medium - _lower_bound / upper_bound_
- [ ] ⭐ [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/) - Medium - _treat as flattened array_
- [ ] ⭐ [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) - Medium - _one half is always sorted_
- [ ] ⭐ [153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) - Medium - _compare mid with right_
- [ ] ⭐ [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) - Medium - _binary search on answer_
- [ ] ⭐ [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) - Medium - _binary search on answer_
- [ ] [981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) - Medium - _map of vectors + upper_bound_
- [ ] [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) - Hard - _partition binary search on smaller array_

## 6. Linked List

> Dummy head, fast/slow pointers, in-place reversal.

> Solutions folder: `solutions/linked-list/`

- [ ] ⭐ [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) - Easy - _iterative prev/curr/next_
- [ ] ⭐ [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) - Easy - _dummy head_
- [ ] ⭐ [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) - Easy - _fast/slow_
- [ ] [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) - Medium - _Floyd phase 2_
- [ ] ⭐ [143. Reorder List](https://leetcode.com/problems/reorder-list/) - Medium - _find mid + reverse second half + merge_
- [ ] ⭐ [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) - Medium - _gap of n between two pointers_
- [ ] ⭐ [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) - Medium - _carry + dummy head_
- [ ] [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) - Medium - _hashmap old->new or interleave_
- [ ] ⭐ [146. LRU Cache](https://leetcode.com/problems/lru-cache/) - Medium - _hashmap + doubly linked list_
- [ ] ⭐ [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) - Hard - _min-heap of heads_
- [ ] [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) - Hard - _reverse in chunks_
- [ ] [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) - Medium - _cycle detection on index graph_

## 7. Trees & BST

> Recursion: decide what to return from each node and what to pass down. BFS = queue per level.

> Solutions folder: `solutions/trees/`

- [ ] ⭐ [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) - Easy - _swap children recursively_
- [ ] ⭐ [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) - Easy - _1 + max(left, right)_
- [ ] ⭐ [100. Same Tree](https://leetcode.com/problems/same-tree/) - Easy - _parallel DFS_
- [ ] [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/) - Easy - _same-tree at every node_
- [ ] ⭐ [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) - Easy - _global answer, return height_
- [ ] [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) - Easy - _return height or -1_
- [ ] [112. Path Sum](https://leetcode.com/problems/path-sum/) - Easy - _subtract along the path_
- [ ] ⭐ [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) - Medium - _BFS with level size_
- [ ] ⭐ [199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) - Medium - _BFS last node per level_
- [ ] ⭐ [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) - Medium - _pass max so far down_
- [ ] ⭐ [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) - Medium - _use BST ordering_
- [ ] ⭐ [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) - Medium - _return node if found in subtree_
- [ ] ⭐ [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) - Medium - _pass (low, high) bounds down_
- [ ] ⭐ [230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) - Medium - _inorder traversal_
- [ ] ⭐ [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) - Medium - _preorder root + inorder split_
- [ ] ⭐ [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) - Hard - _return one-sided gain, update global_
- [ ] [297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) - Hard - _preorder with null markers_

## 8. Heap / Priority Queue

> Top-K, running median, 'always need the min/max next'. O(log n) per op.

> Solutions folder: `solutions/heap/`

- [ ] [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) - Easy - _max-heap simulation_
- [ ] ⭐ [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) - Medium - _min-heap of size k (or quickselect)_
- [ ] ⭐ [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) - Medium - _max-heap of size k_
- [ ] ⭐ [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/) - Medium - _max-heap + cooldown queue (or math)_
- [ ] [692. Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/) - Medium - _heap with custom comparator_
- [ ] [767. Reorganize String](https://leetcode.com/problems/reorganize-string/) - Medium - _greedy with max-heap_
- [ ] ⭐ [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) - Hard - _two heaps_

## 9. Backtracking

> Choose -> explore -> un-choose. Enumerate all subsets/permutations/combinations with pruning.

> Solutions folder: `solutions/backtracking/`

- [ ] ⭐ [78. Subsets](https://leetcode.com/problems/subsets/) - Medium - _include/exclude or start index_
- [ ] [90. Subsets II](https://leetcode.com/problems/subsets-ii/) - Medium - _sort + skip duplicates at same depth_
- [ ] ⭐ [46. Permutations](https://leetcode.com/problems/permutations/) - Medium - _used[] array_
- [ ] ⭐ [39. Combination Sum](https://leetcode.com/problems/combination-sum/) - Medium - _reuse allowed, start index_
- [ ] [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/) - Medium - _sort + skip duplicates_
- [ ] ⭐ [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) - Medium - _index + mapping_
- [ ] ⭐ [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) - Medium - _open/close counters_
- [ ] ⭐ [79. Word Search](https://leetcode.com/problems/word-search/) - Medium - _DFS on grid with visited_
- [ ] [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/) - Medium - _partition + palindrome check_
- [ ] [51. N-Queens](https://leetcode.com/problems/n-queens/) - Hard - _column/diagonal sets_

## 10. Graphs

> BFS = shortest path (unweighted). DFS = connectivity/components/cycles. Topo sort = dependencies. Union-Find = merging sets. Dijkstra = weighted shortest path.

> Solutions folder: `solutions/graphs/`

- [ ] ⭐ [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) - Medium - _grid DFS/BFS_
- [ ] [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/) - Medium - _grid DFS returning size_
- [ ] ⭐ [133. Clone Graph](https://leetcode.com/problems/clone-graph/) - Medium - _DFS + old->new map_
- [ ] ⭐ [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) - Medium - _multi-source DFS from the borders_
- [ ] ⭐ [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) - Medium - _multi-source BFS by levels_
- [ ] [130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/) - Medium - _DFS from border 'O's_
- [ ] ⭐ [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/) - Medium - _DFS or union-find_
- [ ] ⭐ [207. Course Schedule](https://leetcode.com/problems/course-schedule/) - Medium - _cycle detection / Kahn's topo sort_
- [ ] ⭐ [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) - Medium - _topo order_
- [ ] ⭐ [684. Redundant Connection](https://leetcode.com/problems/redundant-connection/) - Medium - _union-find, edge that joins same set_
- [ ] [785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) - Medium - _BFS/DFS 2-coloring_
- [ ] ⭐ [127. Word Ladder](https://leetcode.com/problems/word-ladder/) - Hard - _BFS over word transformations_
- [ ] ⭐ [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/) - Medium - _Dijkstra_
- [ ] [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/) - Medium - _Bellman-Ford k rounds / BFS levels_
- [ ] [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) - Medium - _MST (Prim/Kruskal)_
- [ ] [1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/) - Medium - _Dijkstra on grid_

## 11. Tries

> Prefix lookups on strings. Node = array/map of children + end flag.

> Solutions folder: `solutions/tries/`

- [ ] ⭐ [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) - Medium - _children[26] + isEnd_
- [ ] ⭐ [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) - Medium - _DFS on '.' wildcard_
- [ ] [212. Word Search II](https://leetcode.com/problems/word-search-ii/) - Hard - _trie + grid backtracking_

## 12. Dynamic Programming - 1D

> Define state, recurrence, base case. Start from recursion + memo, then convert to bottom-up.

> Solutions folder: `solutions/dp-1d/`

- [ ] ⭐ [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) - Easy - _fib_
- [ ] [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) - Easy - _dp[i] = cost + min(prev two)_
- [ ] ⭐ [198. House Robber](https://leetcode.com/problems/house-robber/) - Medium - _take/skip_
- [ ] ⭐ [213. House Robber II](https://leetcode.com/problems/house-robber-ii/) - Medium - _circular -> two runs_
- [ ] ⭐ [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) - Medium - _Kadane_
- [ ] ⭐ [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) - Medium - _track max and min_
- [ ] ⭐ [55. Jump Game](https://leetcode.com/problems/jump-game/) - Medium - _greedy farthest reach_
- [ ] [45. Jump Game II](https://leetcode.com/problems/jump-game-ii/) - Medium - _greedy BFS-like levels_
- [ ] ⭐ [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/) - Medium - _expand around center_
- [ ] [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) - Medium - _expand around center_
- [ ] ⭐ [91. Decode Ways](https://leetcode.com/problems/decode-ways/) - Medium - _dp over prefix, 1 or 2 digits_
- [ ] ⭐ [322. Coin Change](https://leetcode.com/problems/coin-change/) - Medium - _unbounded knapsack min_
- [ ] ⭐ [139. Word Break](https://leetcode.com/problems/word-break/) - Medium - _dp[i] = any dp[j] && word(j,i)_
- [ ] ⭐ [300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) - Medium - _O(n^2) dp then O(n log n) tails_
- [ ] ⭐ [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) - Medium - _0/1 knapsack boolean_

## 13. Dynamic Programming - 2D

> Grids and two-sequence problems: dp[i][j]. Knapsack variants. State machines.

> Solutions folder: `solutions/dp-2d/`

- [ ] ⭐ [62. Unique Paths](https://leetcode.com/problems/unique-paths/) - Medium - _grid dp_
- [ ] [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/) - Medium - _grid dp_
- [ ] ⭐ [1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) - Medium - _dp[i][j] on two strings_
- [ ] ⭐ [72. Edit Distance](https://leetcode.com/problems/edit-distance/) - Medium - _insert/delete/replace_
- [ ] ⭐ [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/) - Medium - _count combinations (loop coins outer)_
- [ ] [494. Target Sum](https://leetcode.com/problems/target-sum/) - Medium - _subset sum transform_
- [ ] [309. Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) - Medium - _state machine dp_

## 14. Greedy & Intervals

> Sort first. Then make the locally optimal choice and prove it with an exchange argument.

> Solutions folder: `solutions/greedy-intervals/`

- [ ] ⭐ [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/) - Medium - _sort by start_
- [ ] ⭐ [57. Insert Interval](https://leetcode.com/problems/insert-interval/) - Medium - _three phases: before / overlap / after_
- [ ] ⭐ [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) - Medium - _sort by end, keep earliest finish_
- [ ] [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) - Medium - _sort by end_
- [ ] [134. Gas Station](https://leetcode.com/problems/gas-station/) - Medium - _running tank + reset start_
- [ ] [846. Hand of Straights](https://leetcode.com/problems/hand-of-straights/) - Medium - _ordered map / min-heap_
- [ ] [763. Partition Labels](https://leetcode.com/problems/partition-labels/) - Medium - _last occurrence of each char_

## 15. Bit Manipulation, Math & Matrix

> XOR tricks, bit counting, matrix traversal/in-place tricks.

> Solutions folder: `solutions/bit-math-matrix/`

- [ ] ⭐ [136. Single Number](https://leetcode.com/problems/single-number/) - Easy - _XOR everything_
- [ ] [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) - Easy - _n & (n-1)_
- [ ] [338. Counting Bits](https://leetcode.com/problems/counting-bits/) - Easy - _dp[i] = dp[i>>1] + (i&1)_
- [ ] [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/) - Easy - _shift loop_
- [ ] [268. Missing Number](https://leetcode.com/problems/missing-number/) - Easy - _XOR or sum formula_
- [ ] [371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/) - Medium - _XOR + carry shifts_
- [ ] ⭐ [48. Rotate Image](https://leetcode.com/problems/rotate-image/) - Medium - _transpose + reverse rows_
- [ ] ⭐ [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) - Medium - _four boundaries_
- [ ] [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) - Medium - _use first row/col as markers_
- [ ] [50. Pow(x, n)](https://leetcode.com/problems/powx-n/) - Medium - _fast exponentiation_
- [ ] [202. Happy Number](https://leetcode.com/problems/happy-number/) - Easy - _cycle detection_

## 16. Design (Data Structure Design)

> Combine 2-3 basic structures to hit O(1) operations.

> Solutions folder: `solutions/design/`

- [ ] [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) - Easy - _two stacks, amortized O(1)_
- [ ] [380. Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) - Medium - _vector + hashmap index_

---
Total: **147** problems, **96** core.

