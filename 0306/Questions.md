# Homework

### Question1 检查两个字符串数组是否相等
给你两个字符串数组 word1 和 word2 。如果两个数组表示的字符串相同，返回 true ；否则，返回 false 。

数组表示的字符串 是由数组中的所有元素 按顺序 连接形成的字符串。

示例 1：
```
输入：word1 = ["ab", "c"], word2 = ["a", "bc"]
输出：true
解释：
word1 表示的字符串为 "ab" + "c" -> "abc"
word2 表示的字符串为 "a" + "bc" -> "abc"
两个字符串相同，返回 true
```
示例 2：
```
输入：word1 = ["a", "cb"], word2 = ["ab", "c"]
输出：false
```
示例 3：
```
输入：word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
输出：true
```

提示：
```
1 <= word1.length, word2.length <= 103  
1 <= word1[i].length, word2[i].length <= 103  
1 <= sum(word1[i].length), sum(word2[i].length) <= 103  
word1[i] 和 word2[i] 由小写字母组成
```
### Question2 
计算1+2+3+⋯+(n−1)+n 的值，其中正整数n不大于 10000。

示例：
```
输入：100
输出：5050
```
### Question3  

小玉开心的在游泳，可是她很快难过的发现，自己的力气不够，游泳好累哦。已知小玉第一步能游2米，可是随着越来越累，力气越来越小，她接下来的每一步都只能游出上一步距离的98%。现在小玉想知道，如果要游到距离x米的地方，她需要游多少步呢。请你编程解决这个问题。

输入格式

```
输入一个数字（不一定是整数，小于100m），表示要游的目标距离。  
例：4.3
```

输出格式

```
输出一个整数，表示小玉一共需要游多少步。
例：3
```


