
# 20. Valid Parentheses

Link: [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

## Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

## Examples

Example 1:

```bash
Input: s = "()"
Output: true
```

Example 2:

```bash
Input: s = "()[]{}"
Output: true
```

Example 3:

```bash
Input: s = "(]"
Output: false
```

## Constraints

- `1 <= s.length <= 10^4`

- `s` consists of parentheses only `'()[]{}'`.

## Solution

[![Python](https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python)](./solution.py)
