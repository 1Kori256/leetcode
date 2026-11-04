# LeetCode solutions

My LeetCode solutions, organized in numbered export folders. Most are Python;
many rely on judge-supplied types such as `ListNode`, `TreeNode`, and typing aliases.
The C++ file in `1028/` includes standalone examples.

## Local checks

Requires Python 3.13+, matching the project configuration. No dependencies are
needed to check syntax or regenerate the index.

```sh
python3 tools/update_index.py --check
python3 tools/update_index.py
```

The check compiles each Python solution without running it and verifies that the
index is current. Algorithm correctness is checked separately by LeetCode's judge.
To check the C++ file with a C++17 compiler:

```sh
c++ -std=c++17 -fsyntax-only 1028/solution.cpp
```

## Export setup

Poetry 2.x manages the optional export tool; this collection is configured in
non-package mode. Install the locked dependencies with:

```sh
poetry install
poetry run leetcode-export --help
poetry run leetcode-export --folder exports --only-accepted \
  --only-last-submission --no-problem-statement --language python,python3,cpp
```

See the [exporter's documentation](https://github.com/NeverMendel/leetcode-export)
for login and export options. Use its interactive login prompt for session cookies.
Exports go to the ignored `exports/` folder. Copy selected source files into
numbered folders as `solution.py` or `solution.cpp`, then regenerate the index.

## Solution index

Folder names are preserved export IDs, which can differ from LeetCode's displayed
problem numbers. Method names below come directly from the source files.

<!-- solutions:start -->

95 solutions (94 Python, 1 C++).

| Export folder | Language | Methods |
| --- | --- | --- |
| [0001](0001/solution.py) | Python | `Solution.twoSum` |
| [0002](0002/solution.py) | Python | `Solution.to_num`, `Solution.to_ll`, `Solution.addTwoNumbers` |
| [0003](0003/solution.py) | Python | `Solution.lengthOfLongestSubstring` |
| [0004](0004/solution.py) | Python | `Solution.findMedianSortedArrays` |
| [0005](0005/solution.py) | Python | `Solution.longestPalindrome` |
| [0006](0006/solution.py) | Python | `Solution.convert` |
| [0007](0007/solution.py) | Python | `Solution.reverse` |
| [0008](0008/solution.py) | Python | `Solution.myAtoi` |
| [0009](0009/solution.py) | Python | `Solution.isPalindrome` |
| [0010](0010/solution.py) | Python | `Solution.isMatch` |
| [0011](0011/solution.py) | Python | `Solution.maxArea` |
| [0012](0012/solution.py) | Python | `Solution.intToRoman` |
| [0013](0013/solution.py) | Python | `Solution.romanToInt` |
| [0014](0014/solution.py) | Python | `Solution.longestCommonPrefix` |
| [0015](0015/solution.py) | Python | `Solution.threeSum` |
| [0017](0017/solution.py) | Python | `Solution.letterCombinations` |
| [0019](0019/solution.py) | Python | `Solution.removeNthFromEnd` |
| [0020](0020/solution.py) | Python | `Solution.isValid` |
| [0021](0021/solution.py) | Python | `Solution.mergeTwoLists` |
| [0022](0022/solution.py) | Python | `Solution.generateParenthesis` |
| [0023](0023/solution.py) | Python | `Solution.mergeKLists` |
| [0024](0024/solution.py) | Python | `Solution.swapPairs` |
| [0026](0026/solution.py) | Python | `Solution.removeDuplicates` |
| [0027](0027/solution.py) | Python | `Solution.removeElement` |
| [0028](0028/solution.py) | Python | `Solution.strStr` |
| [0029](0029/solution.py) | Python | `Solution.divide` |
| [0031](0031/solution.py) | Python | `Solution.nextPermutation` |
| [0035](0035/solution.py) | Python | `Solution.searchInsert` |
| [0038](0038/solution.py) | Python | `Solution.countAndSay` |
| [0039](0039/solution.py) | Python | `Solution.combinationSum` |
| [0040](0040/solution.py) | Python | `Solution.combinationSum2` |
| [0041](0041/solution.py) | Python | `Solution.firstMissingPositive` |
| [0043](0043/solution.py) | Python | `Solution.multiply` |
| [0046](0046/solution.py) | Python | `Solution.permute` |
| [0047](0047/solution.py) | Python | `Solution.permuteUnique` |
| [0048](0048/solution.py) | Python | `Solution.rotate` |
| [0049](0049/solution.py) | Python | `Solution.groupAnagrams` |
| [0050](0050/solution.py) | Python | `Solution.myPow` |
| [0057](0057/solution.py) | Python | `Solution.insert` |
| [0058](0058/solution.py) | Python | `Solution.lengthOfLastWord` |
| [0066](0066/solution.py) | Python | `Solution.plusOne` |
| [0067](0067/solution.py) | Python | `Solution.addBinary` |
| [0069](0069/solution.py) | Python | `Solution.mySqrt` |
| [0070](0070/solution.py) | Python | `Solution.climbStairs` |
| [0083](0083/solution.py) | Python | `Solution.deleteDuplicates` |
| [0088](0088/solution.py) | Python | `Solution.merge` |
| [0094](0094/solution.py) | Python | `Solution.inorderTraversal` |
| [0100](0100/solution.py) | Python | `Solution.isSameTree` |
| [0101](0101/solution.py) | Python | `Solution.isSymmetric`, `Solution.h` |
| [0104](0104/solution.py) | Python | `Solution.maxDepth` |
| [0108](0108/solution.py) | Python | `Solution.sortedArrayToBST` |
| [0110](0110/solution.py) | Python | `Solution.isBalanced`, `Solution.search` |
| [0111](0111/solution.py) | Python | `Solution.minDepth` |
| [0112](0112/solution.py) | Python | `Solution.hasPathSum`, `Solution.dfs` |
| [0118](0118/solution.py) | Python | `Solution.generate` |
| [0119](0119/solution.py) | Python | `Solution.getRow` |
| [0121](0121/solution.py) | Python | `Solution.maxProfit` |
| [0125](0125/solution.py) | Python | `Solution.isPalindrome` |
| [0136](0136/solution.py) | Python | `Solution.singleNumber` |
| [0141](0141/solution.py) | Python | `Solution.hasCycle` |
| [0143](0143/solution.py) | Python | `Solution.reorderList` |
| [0144](0144/solution.py) | Python | `Solution.preorderTraversal`, `Solution.dns` |
| [0145](0145/solution.py) | Python | `Solution.postorderTraversal`, `Solution.dns` |
| [0168](0168/solution.py) | Python | `Solution.convertToTitle` |
| [0169](0169/solution.py) | Python | `Solution.majorityElement` |
| [0171](0171/solution.py) | Python | `Solution.titleToNumber` |
| [0190](0190/solution.py) | Python | `Solution.reverseBits` |
| [0191](0191/solution.py) | Python | `Solution.hammingWeight` |
| [0202](0202/solution.py) | Python | `Solution.isHappy`, `Solution.reduce` |
| [0205](0205/solution.py) | Python | `Solution.isIsomorphic` |
| [0206](0206/solution.py) | Python | `Solution.reverseList` |
| [0217](0217/solution.py) | Python | `Solution.containsDuplicate` |
| [0219](0219/solution.py) | Python | `Solution.containsNearbyDuplicate` |
| [0234](0234/solution.py) | Python | `Solution.isPalindrome` |
| [0238](0238/solution.py) | Python | `Solution.productExceptSelf` |
| [0242](0242/solution.py) | Python | `Solution.isAnagram` |
| [0287](0287/solution.py) | Python | `Solution.findDuplicate` |
| [0344](0344/solution.py) | Python | `Solution.reverseString` |
| [0349](0349/solution.py) | Python | `Solution.intersection` |
| [0442](0442/solution.py) | Python | `Solution.findDuplicates` |
| [0452](0452/solution.py) | Python | `Solution.findMinArrowShots` |
| [0525](0525/solution.py) | Python | `Solution.findMaxLength` |
| [0621](0621/solution.py) | Python | `Solution.leastInterval` |
| [0713](0713/solution.py) | Python | `Solution.numSubarrayProductLessThanK` |
| [0807](0807/solution.py) | Python | `Solution.customSortString` |
| [0966](0966/solution.py) | Python | `Solution.numSubarraysWithSum` |
| [1022](1022/solution.py) | Python | `Solution.uniquePathsIII` |
| [1028](1028/solution.cpp) | C++ | See source |
| [1267](1267/solution.py) | Python | `Solution.removeZeroSumSublists` |
| [1381](1381/solution.py) | Python | `Solution.maxScoreWords` |
| [1765](1765/solution.py) | Python | `Solution.mergeInBetween` |
| [2392](2392/solution.py) | Python | `Solution.buildMatrix`, `Solution.sort_with_constraints`, `Solution.build_matrix` |
| [2571](2571/solution.py) | Python | `Solution.pivotInteger` |
| [2634](2634/solution.py) | Python | `Solution.getCommon` |
| [3242](3242/solution.py) | Python | `Solution.maxFrequencyElements` |

<!-- solutions:end -->
