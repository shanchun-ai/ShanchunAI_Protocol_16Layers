"""
善春AI协议 · DNA溯源编码生成器
对应协议层：第11层 DNA溯源编码
版本：V1.0
DNA溯源编码：SCAI-CODE-ENCODER-V1.0-20260530-001
"""

from datetime import datetime


def generate_dna_code(
    product_code: str,
    version: str,
    date: str = None,
    sequence: int = 1
) -> str:
    """
    生成SCAI标准DNA溯源编码
    
    格式：SCAI-[产品代码]-[版本号]-[日期]-[序列号]
    示例：SCAI-DEV-TEAM-V2.3-20260530-001
    
    参数：
        product_code: 产品代码，如 DEV-TEAM
        version: 版本号，如 V2.3
        date: 日期，格式YYYYMMDD，默认为当天
        sequence: 当日序列号，从001开始，默认1
    
    返回：
        完整的DNA溯源编码字符串
    """
    if date is None:
        date = datetime.now().strftime("%Y%m%d")
    
    seq_str = str(sequence).zfill(3)
    
    dna_code = f"SCAI-{product_code}-{version}-{date}-{seq_str}"
    
    return dna_code


def validate_dna_code(code: str) -> dict:
    """
    校验DNA编码格式是否合法
    
    参数：
        code: 待校验的DNA编码字符串
    
    返回：
        校验结果字典，包含是否合法、各字段值、错误信息
    """
    result = {
        "valid": False,
        "prefix": None,
        "product_code": None,
        "version": None,
        "date": None,
        "sequence": None,
        "error": None
    }
    
    parts = code.split("-")
    
    if len(parts) < 5:
        result["error"] = f"编码段数不足：期望至少5段，实际{len(parts)}段"
        return result
    
    if parts[0] != "SCAI":
        result["error"] = f"前缀错误：期望SCAI，实际{parts[0]}"
        return result
    
    result["prefix"] = parts[0]
    result["product_code"] = "-".join(parts[1:-3])
    result["version"] = parts[-3]
    result["date"] = parts[-2]
    result["sequence"] = parts[-1]
    
    # 校验日期格式
    if len(result["date"]) != 8 or not result["date"].isdigit():
        result["error"] = f"日期格式错误：期望YYYYMMDD，实际{result['date']}"
        return result
    
    # 校验序列号格式
    if len(result["sequence"]) != 3 or not result["sequence"].isdigit():
        result["error"] = f"序列号格式错误：期望3位数字，实际{result['sequence']}"
        return result
    
    result["valid"] = True
    return result


# ===== 使用示例 =====
if __name__ == "__main__":
    # 示例1：生成编码
    code = generate_dna_code("DEV-TEAM", "V2.3", "20260530", 1)
    print(f"生成编码：{code}")
    
    # 示例2：校验编码
    check = validate_dna_code(code)
    print(f"校验结果：{'✅ 合法' if check['valid'] else '❌ 不合法'}")
    print(f"  产品代码：{check['product_code']}")
    print(f"  版本号：{check['version']}")
    print(f"  日期：{check['date']}")
    print(f"  序列号：{check['sequence']}")
    
    # 示例3：校验一个非法编码
    bad_code = "SCAI-XXX-20260530"
    check_bad = validate_dna_code(bad_code)
    print(f"\n非法编码校验：{check_bad['error']}")
