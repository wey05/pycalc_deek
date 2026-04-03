# 🧮 Python 计算器

一个使用 Tkinter 编写的桌面计算器，适合课程作业展示和基础运算演示。

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green.svg)

## ✨ 功能特性

- 🎨 现代化按钮界面，数字键、运算符键、清除键分区清晰
- 🧮 支持 `+`、`-`、`*`、`/`、`()` 和小数点输入
- ⚠️ 内置异常提示，错误表达式和除零都会弹窗提示
- 🪟 固定窗口大小，适合直接演示和截图

## 📸 界面说明

- 上方显示当前输入的表达式
- 下方为按键区，支持点击输入
- `C` 可快速清空，`=` 可直接计算结果

## 🚀 运行方式

### 环境要求

- Python 3.x
- Tkinter（通常随 Python 自带）

### 启动项目

```bash
python calculator.py
```

## 💡 使用示例

- `2 + 3` → `5`
- `(2 + 3) * 4` → `20`
- `10 / 4` → `2.5`

## 🛠 技术栈

- Python
- Tkinter
- `eval()` 表达式计算

## ⚠️ 注意事项

- 当前版本使用 `eval()` 计算表达式，请只输入合法数学表达式
- 如果输入错误或除数为 0，程序会弹出错误提示并清空当前表达式

## 📦 项目结构

- `calculator.py`：主程序
- `README.md`：项目说明

## 👨‍💻 作者

魏豫旭

## 🤝 贡献

欢迎继续提交 Issue 或 Pull Request 改进功能。
