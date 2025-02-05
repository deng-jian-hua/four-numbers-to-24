import itertools

def generate_expressions(nums, operators):
    """生成所有可能的数字和运算符表达式"""
    # 生成所有数字的排列
    num_permutations = itertools.permutations(nums)
    # 生成所有运算符的组合（4个数字需要3个运算符）
    operator_combinations = itertools.product(operators, repeat=3)
    
    expressions = []
    # 遍历每一个数字排列
    for num_perm in num_permutations:
        # 遍历每一个运算符组合
        for op_combo in operator_combinations:
            # 形成表达式，例如: (num1 op1 num2) op2 (num3 op3 num4)
            expr = f"({num_perm[0]} {op_combo[0]} {num_perm[1]}) {op_combo[1]} ({num_perm[2]} {op_combo[2]} {num_perm[3]})"
            expressions.append(expr)
    return expressions

def evaluate_expression(expr):
    """计算表达式并返回结果"""
    try:
        # 计算表达式并返回结果
        result = eval(expr)
        return result
    except:
        # 如果计算出错，返回None
        return None

def main():
    # 示例输入数字
    numbers = [3, 4, 6, 8]
    # 表达式中使用的运算符
    operators = ['+', '-', '*', '/']
    
    # 生成所有可能的表达式
    expressions = generate_expressions(numbers, operators)
    
    # 检查是否有表达式的结果为24
    for expr in expressions:
        result = evaluate_expression(expr)
        if result == 24:
            print(f"成功！表达式: {expr} = 24")
            break
    else:
        print("没有找到结果为24的有效表达式。")

if __name__ == "__main__":
    main()
