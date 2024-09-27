import ctypes
from ctypes import *
import time  

# 加载 ControlCAN DLL
can_dll = ctypes.windll.LoadLibrary("./ControlCAN.dll")

# 定义必要的结构体
class VCI_CAN_OBJ(Structure):
    _fields_ = [("ID", c_uint),
                ("TimeStamp", c_uint),
                ("TimeFlag", c_byte),
                ("SendType", c_byte),
                ("RemoteFlag", c_byte),
                ("ExternFlag", c_byte),
                ("DataLen", c_byte),
                ("Data", c_ubyte * 8),
                ("Reserved", c_byte * 3)]

class VCI_INIT_CONFIG(Structure):
    _fields_ = [("AccCode", c_uint),
                ("AccMask", c_uint),
                ("Reserved", c_uint),
                ("Filter", c_byte),
                ("Timing0", c_byte),
                ("Timing1", c_byte),
                ("Mode", c_byte)]

# 打开设备
def open_device(device_type, device_index):
    result = can_dll.VCI_OpenDevice(device_type, device_index, 0)
    if result == 1:
        print(f"设备 {device_index} 打开成功")
    else:
        print(f"设备 {device_index} 打开失败")
    return result

# 初始化 CAN 通道
def init_can(device_type, device_index, can_index, baud_rate=250):
    init_config = VCI_INIT_CONFIG()
    init_config.AccCode = 0x80000000
    init_config.AccMask = 0xFFFFFFFF
    init_config.Filter = 0  # 接收所有类型的报文
    # 根据波特率设置 Timing0 和 Timing1
    if baud_rate == 250:  # 250kbps
        init_config.Timing0 = 0x01
        init_config.Timing1 = 0x1C
    elif baud_rate == 500:  # 500kbps
        init_config.Timing0 = 0x00
        init_config.Timing1 = 0x1C
    else:
        print("未支持的波特率")
        return 0
    init_config.Mode = 0  # 正常模式

    result = can_dll.VCI_InitCAN(device_type, device_index, can_index, byref(init_config))
    if result == 1:
        print(f"CAN 通道 {can_index} 初始化成功 (波特率: {baud_rate}kbps)")
    else:
        print(f"CAN 通道 {can_index} 初始化失败")
    return result

# 启动 CAN 通道
def start_can(device_type, device_index, can_index):
    result = can_dll.VCI_StartCAN(device_type, device_index, can_index)
    if result == 1:
        print(f"CAN 通道 {can_index} 启动成功")
    else:
        print(f"CAN 通道 {can_index} 启动失败")
    return result

# 接收 CAN 数据
def receive_can_data(device_type, device_index, can_index, max_frames=1000):
    can_obj = VCI_CAN_OBJ * max_frames  # 创建存储接收到数据的数组
    receive_buffer = can_obj()
    result = can_dll.VCI_Receive(device_type, device_index, can_index, byref(receive_buffer), max_frames, 100)
    
    if result > 0:
        print(f"通道 {can_index} 接收到 {result} 帧 CAN 数据")
        for i in range(result):
            frame = receive_buffer[i]
            print(f"帧ID: {hex(frame.ID)}, 数据: {[hex(x) for x in frame.Data[:frame.DataLen]]}")
    return result

def parse_can_message(can_id, data):
    result = {}
    
    # 解析 CAN ID 16#9C4 的报文
    if can_id == 0x9C4:
        result['引擎启动'] = (data[0] & 0x01)      # byte1, Bit0
        result['引擎熄火(保持)'] = (data[0] & 0x02) >> 1  # byte1, Bit1
        result['前进档'] = (data[0] & 0x04) >> 2   # byte1, Bit2
        result['空档'] = (data[0] & 0x08) >> 3     # byte1, Bit3
        result['后退档'] = (data[0] & 0x10) >> 4   # byte1, Bit4
        result['加档'] = (data[0] & 0x20) >> 5     # byte1, Bit5
        result['减档'] = (data[0] & 0x40) >> 6     # byte1, Bit6
        result['拖车'] = (data[0] & 0x80) >> 7     # byte1, Bit7
        result['驻车刹车'] = (data[1] & 0x01)      # byte2, Bit0
        result['急停开关'] = (data[1] & 0x02) >> 1  # byte2, Bit1
        result['前灯'] = (data[1] & 0x04) >> 2     # byte2, Bit2
        result['后灯'] = (data[1] & 0x08) >> 3     # byte2, Bit3
        result['喇叭'] = (data[1] & 0x10) >> 4     # byte2, Bit4
        result['心跳'] = data[7]                   # byte8, 心跳周期

    # 解析 CAN ID 16#9C5 的报文
    elif can_id == 0x9C5:
        result['油门'] = data[0]                   # byte1, 油门
        result['左转'] = data[1]                   # byte2, 左转
        result['右转'] = data[2]                   # byte3, 右转
        result['升臂'] = data[3]                   # byte4, 升臂
        result['降臂'] = data[4]                   # byte5, 降臂
        result['装料'] = data[5]                   # byte6, 装料
        result['卸料'] = data[6]                   # byte7, 卸料
        result['辅助刹车'] = data[7]               # byte8, 辅助刹车

    # 解析 CAN ID 16#5 的报文 (例如：工作压力，转向压力)
    elif can_id == 0x5:
        result['工作压力'] = (data[1] << 8) | data[0]  # byte2, byte3 合并为一个 word，工作压力
        result['转向压力'] = (data[4] << 8) | data[3]  # byte4, byte5 合并为一个 word，转向压力

    # 解析 CAN ID 16#5E0 的报文 (例如：液压油温度，车辆速度)
    elif can_id == 0x5E0:
        result['液压油温度'] = data[2] - 50           # byte3, 液压油温度，1℃/bit，-50偏移
        result['车辆速度'] = ((data[7] << 8) | data[6]) * 0.1  # byte7, byte8 合并为一个 word，0.1km/h/bit

    # 返回解析后的结果
    return result

# 示例调用
# can_id = 0x9C4
# data = [0x15, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01]  # 假设的CAN数据
# parsed_data = parse_can_message(can_id, data)
# print(parsed_data)


# 主函数
if __name__ == "__main__":
    device_type = 4  # 设备类型为 USBCAN-2A 或 CANalyst-II
    device_index = 0  # 设备索引

    if open_device(device_type, device_index):
        # 初始化和启动 CAN 通道 0 和通道 1
        for can_index in [0, 1]:  # 通道 0 和 通道 1
            if init_can(device_type, device_index, can_index, baud_rate=250):
                if not start_can(device_type, device_index, can_index):
                    print(f"通道 {can_index} 启动失败")
                    exit(1)  # 如果通道启动失败则退出

        # 主循环轮询通道
        while True:
            for can_index in [0, 1]:  # 轮询通道 0 和 1
                result = receive_can_data(device_type, device_index, can_index)
                if result == 0:
                    print(f"通道 {can_index} 没有接收到数据")
            time.sleep(0.5)  # 每次轮询两个通道后暂停0.5秒
