from typing import List

from entity.function import get_all_function, get_all_function_param


def get_tools():
    functions = get_all_function()
    params = get_all_function_param()
    parameters_dict = {}
    required_dict = {}
    generator_parameters(params, parameters_dict, required_dict)

    tools = []
    for function in functions:
        function_json = {
            "type": "function",
            "function": {
                "name": function.name,
                "description": function.description,
                "parameters": {
                    "type": "object",
                    "properties": parameters_dict.get(function.id),
                    "required": required_dict.get(function.id)
                }
            }
        }
        tools.append(function_json)
    return tools


def generator_parameters(params, parameters_dict, required_dict):
    """
    根据List[FunctionParameters] 生成参数字典和必填字段字典

    :param params:方法参数列表
    :type params: FunctionParameters
    :param parameters_dict: 参数字典
    :type parameters_dict: dict[int,List[dict]]
    :param required_dict: 必填字段字典
    :type required_dict: dict[int,List[str]]
    :return: None
    :rtype:None
    """

    for param in params:
        if parameters_dict.get(param.function_id) is None:
            parameters_dict[param.function_id] = {}
            required_dict[param.function_id] = []
        parameters_dict[param.function_id][param.name] = create_param_dict(param)
        required_dict[param.function_id].append(param.name) if param.required else None


def create_param_dict(param):
    param_info = {
        "type": param.type,
        "description": param.description,
    }
    if param.enum:
        param_info['enum'] = enum1 = param.enum.split("|")

    return param_info
