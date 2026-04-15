#!/usr/bin/env python3
"""
简历格式化脚本 - 中英文空格处理工具

功能：自动在简历内容的中英文之间添加空格，提升可读性
"""

import re
import sys
import argparse
from pathlib import Path
from typing import List, Tuple


class ResumeFormatter:
    """简历格式化器类"""
    
    def __init__(self):
        # 中英文之间需要添加空格的正则模式
        self.patterns = [
            # 中文后跟英文（需要添加空格）
            (r'([\u4e00-\u9fff])([a-zA-Z])', r'\1 \2'),
            # 英文后跟中文（需要添加空格）
            (r'([a-zA-Z])([\u4e00-\u9fff])', r'\1 \2'),
            # 中文后跟数字（需要添加空格）
            (r'([\u4e00-\u9fff])(\d)', r'\1 \2'),
            # 数字后跟中文（需要添加空格）
            (r'(\d)([\u4e00-\u9fff])', r'\1 \2'),
            # 处理标点符号后的空格
            (r'([。，；：！？])([a-zA-Z])', r'\1 \2'),
            (r'([a-zA-Z])([。，；：！？])', r'\1 \2'),
        ]
        
        # 不需要添加空格的特殊情况（技术术语、专有名词等）
        self.exceptions = [
            # 技术框架和库
            r'React', r'Vue', r'Angular', r'Spring', r'Django', r'TensorFlow', r'PyTorch',
            # 编程语言
            r'Java', r'Python', r'JavaScript', r'TypeScript', r'Go', r'C\+\+', r'C#',
            # 数据库
            r'MySQL', r'PostgreSQL', r'Redis', r'MongoDB', r'Elasticsearch',
            # 工具和平台
            r'Docker', r'Kubernetes', r'Git', r'Jenkins', r'AWS', r'Azure', r'GCP',
            # 协议和标准
            r'HTTP', r'HTTPS', r'REST', r'GraphQL', r'WebSocket',
            # 版本号（如 v1.0, React18）
            r'v\d+\.\d+', r'[A-Za-z]+\d+',
            # 单位（如 10ms, 100GB）
            r'\d+[a-zA-Z]+',
        ]
    
    def format_text(self, text: str) -> str:
        """格式化文本，在中英文之间添加空格"""
        if not text:
            return text
        
        # 先处理特殊情况（保护技术术语）
        protected_text = self._protect_exceptions(text)
        
        # 应用格式化规则
        formatted_text = protected_text
        for pattern, replacement in self.patterns:
            formatted_text = re.sub(pattern, replacement, formatted_text)
        
        # 恢复被保护的内容
        formatted_text = self._restore_exceptions(formatted_text)
        
        return formatted_text
    
    def _protect_exceptions(self, text: str) -> str:
        """保护特殊内容不被格式化"""
        self.protected_items = {}
        
        for i, pattern in enumerate(self.exceptions):
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                placeholder = f'__PROTECTED_{i}_{match.start()}__'
                self.protected_items[placeholder] = match.group()
                text = text[:match.start()] + placeholder + text[match.end():]
        
        return text
    
    def _restore_exceptions(self, text: str) -> str:
        """恢复被保护的内容"""
        for placeholder, original in self.protected_items.items():
            text = text.replace(placeholder, original)
        
        return text
    
    def format_file(self, input_file: str, output_file: str = None) -> bool:
        """格式化文件"""
        try:
            # 读取文件
            with open(input_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 格式化内容
            formatted_content = self.format_text(content)
            
            # 输出文件
            if output_file:
                output_path = output_file
            else:
                # 在原文件名后添加 _formatted
                input_path = Path(input_file)
                output_path = input_path.parent / f"{input_path.stem}_formatted{input_path.suffix}"
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(formatted_content)
            
            print(f"✅ 格式化完成：{input_file} -> {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ 格式化失败：{e}")
            return False
    
    def check_formatting(self, text: str) -> List[Tuple[int, str, str]]:
        """检查文本中的格式问题"""
        issues = []
        lines = text.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            # 检查中英文之间缺少空格的问题
            issues.extend(self._check_line_formatting(line, line_num))
        
        return issues
    
    def _check_line_formatting(self, line: str, line_num: int) -> List[Tuple[int, str, str]]:
        """检查单行的格式问题"""
        issues = []
        
        # 检查中英文之间缺少空格
        chinese_english_pattern = r'([\u4e00-\u9fff])([a-zA-Z])'
        english_chinese_pattern = r'([a-zA-Z])([\u4e00-\u9fff])'
        
        for match in re.finditer(chinese_english_pattern, line):
            original = match.group()
            suggested = f"{match.group(1)} {match.group(2)}"
            issues.append((line_num, original, suggested))
        
        for match in re.finditer(english_chinese_pattern, line):
            original = match.group()
            suggested = f"{match.group(1)} {match.group(2)}"
            issues.append((line_num, original, suggested))
        
        return issues


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='简历格式化工具 - 中英文空格处理')
    parser.add_argument('input', help='输入文件路径')
    parser.add_argument('-o', '--output', help='输出文件路径（可选）')
    parser.add_argument('-c', '--check', action='store_true', help='仅检查不修改')
    parser.add_argument('-v', '--verbose', action='store_true', help='详细输出')
    
    args = parser.parse_args()
    
    formatter = ResumeFormatter()
    
    if args.check:
        # 检查模式
        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                content = f.read()
            
            issues = formatter.check_formatting(content)
            
            if issues:
                print("🔍 发现以下格式问题：")
                for line_num, original, suggested in issues:
                    print(f"  第{line_num}行: '{original}' -> '{suggested}'")
                print(f"\n📊 共发现 {len(issues)} 个格式问题")
            else:
                print("✅ 未发现格式问题")
                
        except Exception as e:
            print(f"❌ 检查失败：{e}")
    
    else:
        # 格式化模式
        success = formatter.format_file(args.input, args.output)
        
        if success and args.verbose:
            # 显示格式化前后的对比
            try:
                with open(args.input, 'r', encoding='utf-8') as f:
                    original_content = f.read()
                
                output_file = args.output if args.output else f"{Path(args.input).stem}_formatted{Path(args.input).suffix}"
                with open(output_file, 'r', encoding='utf-8') as f:
                    formatted_content = f.read()
                
                print("\n📋 格式化前后对比：")
                print("=" * 50)
                print("原始内容（片段）：")
                print(original_content[:200] + "..." if len(original_content) > 200 else original_content)
                print("\n格式化后内容（片段）：")
                print(formatted_content[:200] + "..." if len(formatted_content) > 200 else formatted_content)
                print("=" * 50)
                
            except Exception as e:
                print(f"⚠️  无法显示对比：{e}")


if __name__ == "__main__":
    main()