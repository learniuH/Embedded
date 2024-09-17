import socket

# 创建UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('192.168.10.10', 9002))  # 监听电脑的IP和端口

print("Listening for UDP packets on 192.168.10.10:9002...")

# 保存上一条接收到的报文的数据域
previous_data_field = None

# 定义每个字节的bit描述
bit_definitions = {
    11: {
        1: "急停",
        2: "喇叭",
        3: "灯光",
        5: "驻刹",
        7: "卷盘正转"
    },
    12: {
        0: "卷盘反转",
        1: "打孔",
        2: "行走",
        3: "油泵启动",
        4: "油泵停止",
        5: "顶棚升",
        6: "顶棚降",
        7: "回转右"
    },
    13: {
        0: "回转左",
        1: "开孔冲击",
        2: "全速冲击",
        3: "推进高",
        4: "推进低",
        5: "后支腿升",
        6: "后支腿降",
        7: "水汽控制"
    },
    14: {
        1: "顶部按键",
        2: "发动机启",
        3: "发动机停"
    }
}

# 对第15到42字节，若字节值不为0则视为触发
bytes_definition = {
    15: "反转油缸正转",
    16: "反转油缸反转",
    17: "左前支腿升",
    18: "左前支腿降",
    19: "靠帮角伸",
    20: "靠帮角缩",
    21: "左前支腿伸",
    22: "左前支腿缩",
    23: "钻臂左摆",
    24: "钻臂右摆",
    25: "推进梁左摆",
    26: "推进梁右摆",
    27: "整车左转",
    28: "整车右转",
    29: "钻臂升",
    30: "钻臂降",
    31: "推进梁上",
    32: "推进梁下",
    33: "整车前进",
    34: "整车后退",
    35: "大臂伸",
    36: "大臂缩",
    37: "右前支腿伸",
    38: "右前支腿缩",
    39: "推进梁伸",
    40: "推进梁缩",
    41: "右前支腿升",
    42: "右前支腿降"
}

def parse_bits(byte, bit_definitions):
    """
    解析一个字节的bit位并返回触发的状态
    @ byte : 原始报文的某一字节
    @ bit_definitions : 协议中对该字节的定义
    return : 例如 {"发动机启" : "Triggered", "开孔冲击" : "Triggered"}
    
    """
    bit_status = {}
    for bit_position, label in bit_definitions.items():
        if (byte >> bit_position) & 1:  # 只在bit位为1时触发
            bit_status[label] = "Triggered"
    return bit_status

def process_byte(byte_number, data):
    """
    处理指定的字节，解析并打印触发的状态
    @ byte_number : 第几个字节的数据
    @ data : 原始的报文数据

    """
    if byte_number in bit_definitions:
        byte = data[byte_number - 1]  # 获取指定字节
        status = parse_bits(byte, bit_definitions[byte_number])
        if status:
            print(f"\nByte{byte_number} Status (Triggered):")
            print(status)
    elif byte_number in bytes_definition:
        byte = data[byte_number - 1]
        if byte != 0:  # 只要字节不为0就认为触发
            print(f"\nByte{byte_number} ({bytes_definition[byte_number]}) Triggered")

while True:
    try:
        # 接收UDP数据包
        data, addr = sock.recvfrom(1024)
        
        # 确保报文长度为53字节
        if len(data) == 53:
            # 提取中间部分数据（第11个字节到倒数第二个字节）
            current_data_field = data[10:-1]

            # 如果当前中间部分报文和上一个不一样，打印出来
            if current_data_field != previous_data_field:
                print(f"\nReceived packet from {addr}")

                # 将数据打印为十六进制格式
                hex_data = ' '.join(f'{byte:02X}' for byte in data)
                print(f"Data (hex): {hex_data}")

                # 处理字节11到42的触发状态
                for byte_number in range(11, 43):
                    process_byte(byte_number, data)

                # 更新保存的中间部分报文
                previous_data_field = current_data_field
        else:
            print("Received packet too short to process.")

    except KeyboardInterrupt:
        print("\nStopped by user")
        break
    except Exception as e:
        print(f"Error receiving packet: {e}")

# 关闭Socket
sock.close()
