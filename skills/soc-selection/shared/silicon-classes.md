# Silicon Classes（词表 · 可扩展）

Phase 2 **形态种子**与 **Spec Detail Probe** 的主键。Brief 元信息：

| 字段 | 含义 |
|------|------|
| `primary_silicon_class` | 恰好 1 个 id |
| `adjacent_silicon_classes` | 0～N 个 id |
| `needs_seed_extension` | 未登记类或自定义时为 true |

门户推断时词表是**提示库不是上限**。

## 枚举

| id | 标签 | 典型用途 | 默认探针包 |
|----|------|----------|------------|
| `ap_som` | AP / SoM | 边缘 Linux/Android 主控、机器人算力板 | robot_ap |
| `vision_soc` | 视觉 / IPC SoC | 多摄 ISP、录像、AI 视觉 | vision |
| `audio_sip` | 音频 SoC / SiP | TWS/OWS、蓝牙音频 | audio_sip |
| `display_mcu` | 显示控制 MCU | 表情屏、仪表小屏 | display_mcu |
| `industrial_mcu` | 工业 / 宽温 MCU | 温宽、多 UART/ADC、RTOS | industrial_mcu |
| `vehicle_soc` | 车载 SoC | 座舱/仪表/两轮车机 | vehicle |
| `lightweight_ap` | 轻量 AP | 带屏可穿戴、低功耗 Linux | lightweight_ap |
| `wifi_bt_combo` | Wi‑Fi+BT 复合 | 传图耳机、联网外设 | audio_sip |
| `general_mcu` | 通用 MCU / 低功耗 MCU | 简单控制、传感器节点 | industrial_mcu |
| `npu_accelerator` | NPU / AI 加速芯片 | 外挂/协处理 AI | vision |
| `cellular_module` | 蜂窝模组 / 4G·5G | 模组当主控或主联网 | lightweight_ap |
| `dsp_audio` | 音频 DSP / 语音前端 | 远场/降噪 DSP | audio_sip |
| `fpga_som` | FPGA / 可编程 SoM | 特殊接口、加速 | robot_ap |
| `sensor_hub` | Sensor Hub / 协处理 MCU | 传感融合协芯 | industrial_mcu |
| `power_pmic_mcu` | 电源 / 充电管理 MCU | 充电、PMIC 侧控 | industrial_mcu |
| `ethernet_industrial` | 工业以太网 / 网关主控 | 网关、TSN/工业协议 | industrial_mcu |

未知形态：自定义 id + `needs_seed_extension=true`，或选最接近 id。

## Family → 推荐主类（仅推荐，可改）

| Product Family | 推荐 primary（可覆盖） |
|----------------|------------------------|
| `companion_robot` | `ap_som` |
| `wearable_ai` | `audio_sip` |
| `out_of_family` | 无默认；必须由概念选定 |
