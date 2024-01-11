# 子序列问题通用思路


&lt;!--more--&gt;

# 什么是子序列
子序列定义为：**不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。**

一旦涉及到子序列和最值，那几乎可以肯定，考察的是**动态规划** 技巧，时间复杂度一般都是 **O(n^2)**。

# 思路
## 1. 一维DP数组

```java
int n = array.length;
int[] dp = new int[n];

for(int i = 1; i &lt; n; i&#43;&#43;){
    for(int j = 0; j &lt; n; j&#43;&#43;){
        dp[i] = 最值(dp[i],dp[j]&#43;...)
    }
}
```

{{&lt; admonition example &gt;}}
e.g.「[最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)」
{{&lt; /admonition  &gt;}}

```markdown
找到一个给定序列的最长子序列的长度，使得子序列中的所有元素单调递增。

例如：{ 3，5，7，1，2，8 } 的 LIS 是 { 3，5，7，8 }，长度为 4。
```

```java
class Solution {
    public int lengthOfLIS(int[] nums){
        // dp[i] 表示以第i个元素为结尾时，最长上升子序列的长度
        // 状态转移方程
        // dp[i] = max(dp[j])&#43;1,其中0&lt;=j&lt;i且num[i]&gt;num[j]
        if(nums.length == 0){
            return 0;
        }
        int n = nums.length;
        int[] dp = new int[n];
        dp[0] = 1;
        int max = 1;
        for(int i = 1;i &lt; n;i&#43;&#43;){
            dp[i] = 1;
            for(int j = 0;j &lt; i;j&#43;&#43;){
                if(nums[i] &gt; nums[j]){
                    dp[i] = Math.max(dp[i],dp[j]&#43;1);
                }
            }
            max = Math.max(max,dp[i]);
        }
        return max;
    }
}
```

## 2. 二维dp数组

```java
int n = arr.length;
int[][] dp = new dp[n][n];

for(int i = 0; i &lt; n; i&#43;&#43;){
    for(int j =  0; j &lt; n; j&#43;&#43;){
        if(arr[i] == arr[j]){
            dp[i][j] = dp[i][j] &#43; ...
        }else{
            dp[i][j] = 最值(...)
        }
    }
}
```

分两种情况

- 只涉及一个字符串
- 涉及两个字符串

### 2.1 **涉及两个字符串/数组**

{{&lt; admonition example &gt;}}
e.g. 「[最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/)」
{{&lt; /admonition &gt;}}

dp数组的含义：**在子数组 arr1[0..i] 和子数组 arr2[0..j] 中，我们要求的子序列（最长公共子序列）长度为 dp[i][j]**

```markdown
给定两个字符串 text1 和 text2，
返回这两个字符串的最长公共子序列的长度。
如果不存在公共子序列 ，返回 0 。

输入：text1 = &#34;abcde&#34;, text2 = &#34;ace&#34; 
输出：3  
解释：最长公共子序列是 &#34;ace&#34; ，它的长度为 3 。
```

```java
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        char[] t1 = text1.toCharArray();
        char[] t2 = text2.toCharArray();
        int m = t1.length;
        int n = t2.length;
        // 创建 m&#43;1行 n&#43;1列的二维数组
        // dp[i][j]表示 t1[0-i]和t2[0-j]的最长公共子序列长度
        // 当i=0 时 ，t1[0:i] 为空对于任意j,dp[0][j] == 0
        // 当j=0 时 , t2[0:j] 为空 对于任意i,dp[i][0] == 0
        // 回归方程
        // t1[i-1] = t2[j-1] 时，dp[i][j] = dp[i-1][j-1] &#43; 1
        // t1[i-1] != t2[j-1] 时，dp[i][j] = max(dp[i-1][j],dp[i][j-1]) 
        int[][] dp = new int[m&#43;1][n&#43;1];
        for(int i = 0;i &lt;= m;i&#43;&#43;){
            dp[i][0] = 0; 
        }
        for(int i = 0;i &lt;= n;i&#43;&#43;){
            dp[0][i] = 0;
        }
        
        for(int i = 1;i &lt;= m;i&#43;&#43;){
            for(int j = 1;j &lt;= n;j&#43;&#43;){
                if(t1[i-1] == t2[j-1]){
                    dp[i][j] = dp[i-1][j-1] &#43; 1;
                }else{
                    dp[i][j] = Math.max(dp[i][j-1],dp[i-1][j]);
                }
            }
        }
        return dp[m][n];
    }
}
```

### 2.2 只涉及一个字符串/数组

{{&lt; admonition example &gt;}}
e.g.「[最长回文子序列](https://leetcode.cn/problems/longest-palindromic-subsequence/)」
{{&lt; /admonition &gt;}}

dp数组的含义：**在子数组 array[i..j] 中，我们要求的子序列（最长回文子序列）的长度为 dp[i][j]**

```markdown
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

输入：s = &#34;bbbab&#34;
输出：4
解释：一个可能的最长回文子序列为 &#34;bbbb&#34; 。

输入：s = &#34;cbbd&#34;
输出：2
解释：一个可能的最长回文子序列为 &#34;bb&#34; 。
```

```java
class Solution {
    public int longestPalindromeSubseq(String s) {
    	if(s == null || s.length() == 0){
            return 0;
        }
        int n = s.length();
        char[] chars = s.toCharArray();
        // dp[i][j] 表示字符串 chars[i:j] 存在最长子序列的长度
        // 当且仅当 0&lt;=i&lt;=j&lt;n时, dp[i][j]&gt;0;
        // 初始状态
        // dp[i][j] = 1 , i = j;
        // 转移方程
        // 1. chars[i] == chars[j] , dp[i][j] = dp[i&#43;1]dp[j-1]&#43;2;
        // 2. chars[i] != chars[j] , dp[i][j] = max(dp[i&#43;1][j],dp[i][j-1])
        int[][] dp = new int[n][n];
        for(int i = n-1;i&gt;=0;i--){
            dp[i][i] = 1;
            for(int j = i&#43;1; j&lt;n;j&#43;&#43;){
                if(chars[i] == chars[j]){
                    dp[i][j] = dp[i&#43;1][j-1] &#43; 2;
                }else{
                    dp[i][j] = Math.max(dp[i&#43;1][j],dp[i][j-1]);
                }
            }
        }
        return dp[0][n-1];
    }
}
```

# 参考

- [最长回文子序列：子序列问题通用思路 —— labuladong](https://zhuanlan.zhihu.com/p/100994146)

---

> 作者: [uyaki](https://www.github.com/uyaki)  
> URL: http://uyaki.github.io/posts/algorithm/%E5%AD%90%E5%BA%8F%E5%88%97%E9%97%AE%E9%A2%98%E9%80%9A%E7%94%A8%E6%80%9D%E8%B7%AF/  

