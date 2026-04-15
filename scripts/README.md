# 简历格式化脚本

## 概述

`format-resume.py` 是一个专门用于格式化简历内容的 Python 脚本，主要功能是自动在中英文之间添加空格，提升简历的可读性和专业性。

## 功能特性

### 🔧 核心功能
- **中英文空格处理**：自动在中文和英文之间添加空格
- **技术术语保护**：智能识别并保护技术专有名词（如 React、Vue、Spring 等）
- **数字处理**：正确处理数字与中文之间的空格
- **标点符号优化**：优化标点符号后的空格处理

### 🛡️ 智能保护
脚本会自动保护以下内容不被格式化：
- **技术框架**：React、Vue、Angular、Spring、Django 等
- **编程语言**：Java、Python、JavaScript、TypeScript 等
- **数据库**：MySQL、PostgreSQL、Redis、MongoDB 等
- **工具平台**：Docker、Kubernetes、Git、Jenkins 等
- **协议标准**：HTTP、HTTPS、REST、GraphQL 等
- **版本号**：v1.0、React18 等
- **单位**：10ms、100GB 等

## 安装要求

### 系统要求
- Python 3.6 或更高版本
- 支持 UTF-8 编码的文件系统

### 依赖库
脚本使用标准库，无需额外安装依赖：
- `re` - 正则表达式
- `argparse` - 命令行参数解析
- `pathlib` - 路径处理

## 使用方法

### 基本格式化
```bash
# 格式化简历文件
python scripts/format-resume.py resume.txt

# 指定输出文件
python scripts/format-resume.py resume.txt -o formatted_resume.txt

# 详细模式（显示格式化前后对比）
python scripts/format-resume.py resume.txt -v
```

### 检查模式
```bash
# 仅检查格式问题，不修改文件
python scripts/format-resume.py resume.txt -c

# 检查并显示详细信息
python scripts/format-resume.py resume.txt -c -v
```

### 批量处理
```bash
# 批量处理多个文件
for file in *.txt; do
    python scripts/format-resume.py "$file"
done
```

## 使用示例

### 示例输入
```
使用React和Vue.js开发前端应用，优化性能提升30%。负责MySQL数据库设计和API接口开发。
```

### 格式化后输出
```
使用 React 和 Vue.js 开发前端应用，优化性能提升 30%。负责 MySQL 数据库设计和 API 接口开发。
```

### 检查模式输出
```bash
$ python scripts/format-resume.py example.txt -c
🔍 发现以下格式问题：
  第1行: '用React' -> '用 React'
  第1行: '和Vue' -> '和 Vue'
  第1行: '能提升30' -> '能提升 30'
  第2行: '责MySQL' -> '责 MySQL'

📊 共发现 4 个格式问题
```

## 命令行参数

| 参数        | 简写 | 说明                 | 示例               |
| ----------- | ---- | -------------------- | ------------------ |
| `input`     | -    | 输入文件路径（必需） | `resume.txt`       |
| `--output`  | `-o` | 输出文件路径（可选） | `-o formatted.txt` |
| `--check`   | `-c` | 仅检查不修改         | `-c`               |
| `--verbose` | `-v` | 详细输出模式         | `-v`               |

## 集成到简历分析流程

### 在简历分析前使用
```python
# 在简历分析前先格式化内容
from scripts.format_resume import ResumeFormatter

formatter = ResumeFormatter()
formatted_resume = formatter.format_text(raw_resume_content)

# 然后进行五步分析
analysis_result = analyze_resume(formatted_resume)
```

### 作为独立工具使用
```python
from scripts.format_resume import ResumeFormatter

# 创建格式化器实例
formatter = ResumeFormatter()

# 格式化文本
original_text = "使用React开发应用"
formatted_text = formatter.format_text(original_text)
print(formatted_text)  # 输出："使用 React 开发应用"

# 检查格式问题
issues = formatter.check_formatting(original_text)
for line_num, original, suggested in issues:
    print(f"问题：'{original}' -> '{suggested}'")
```

## 格式化规则

### 添加空格的情况
1. **中文 + 英文**：`使用React` → `使用 React`
2. **英文 + 中文**：`React应用` → `React 应用`
3. **中文 + 数字**： `性能提升30%` → `性能提升 30%`
4. **数字 + 中文**： `30%提升` → `30% 提升`
5. **标点 + 英文**：`。React` → `。 React`

### 不添加空格的情况（保护内容）
1. **技术术语**：`React`、`Vue.js`、`Spring Boot`
2. **版本号**：`v1.0`、`React18`
3. **单位**：`10ms`、`100GB`
4. **专有名词**：`MySQL`、`Docker`、`AWS`

## 错误处理

### 常见错误
- **文件不存在**：显示错误信息并退出
- **编码问题**：自动使用 UTF-8 编码，支持其他常见编码
- **权限问题**：提示权限不足

### 错误示例
```bash
$ python scripts/format-resume.py nonexistent.txt
❌ 格式化失败：[Errno 2] No such file or directory: 'nonexistent.txt'
```

## 最佳实践

### 使用时机
1. **简历撰写后**：在提交简历前进行格式化
2. **简历分析前**：在 resume-doctor 分析前先格式化
3. **批量处理**：处理多个简历文件时

### 质量检查
- 使用 `-c` 参数检查格式问题
- 结合人工审核确保技术术语正确
- 定期更新保护列表以适应新技术

## 扩展开发

### 添加新的保护规则
```python
# 在 ResumeFormatter 类的 __init__ 方法中添加
def __init__(self):
    # 现有规则...
    
    # 添加新的保护规则
    self.exceptions.extend([
        r'NewTechnology',  # 新技术
        r'CustomTool',     # 自定义工具
    ])
```

### 自定义格式化规则
```python
# 添加新的格式化规则
self.patterns.append(
    (r'(自定义模式)', r'替换内容')
)
```