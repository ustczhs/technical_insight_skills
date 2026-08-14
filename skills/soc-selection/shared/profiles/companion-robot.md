# Dimension Profile: Companion Robot

**Product Family**: Companion Robot（**仅问卷**）  
**推荐 primary Silicon Class**: `ap_som`（可改；权威见 Brief 元信息与 [silicon-classes.md](../silicon-classes.md)）  
**相邻类**: 由 Hard 触发 + 产品确认写入 `adjacent_silicon_classes`；常见 `vision_soc` 等。

**厂商矩阵**：Phase 2 按 Brief 的 **Silicon Class 段 ∪ Application Domain 加扫**（见 [vendor-seeds.md](../vendor-seeds.md)），**不**再按本 Family 名选表。

## Core Dimensions

对每一维：用 Product Framing 提问与给档位 → 写入 Spec Field → 保留 Framing–Spec Mapping → Agent 推荐 Hard/Soft/Unconstrained → 产品确认。  
允许自定义输入；「无要求」须显式 Unconstrained。

| id | Product Framing（问法要点） | Spec Field（落盘要点） | 默认推荐等级 |
|----|------------------------------|------------------------|--------------|
| `sub_form` | 桌面固定 / 室内移动 / 车载等 | 形态标签；触发 Extension | Soft（除非明确排除某形态） |
| `compute_band` | 交互流畅度、多任务体感档位 | CPU 性能带（档位枚举） | Soft 或 Hard（看是否卡死体验） |
| `on_device_ai` | 无本地 AI / 轻 / 中 / 重 | NPU 算力带或「无 NPU」 | 常 Hard（若功能依赖本地模型） |
| `display` | 无屏 / 单屏分辨率档 / 多屏 | 显示接口与分辨率带 | Hard（有屏时） |
| `camera_video` | 路数、用途（导航/人脸/录像）、分辨率 | CSI/ISP/编解码需求带 | Hard（有视觉功能时） |
| `hs_io` | 是否要外扩存储/网口/高速外设 | USB / PCIe / Ethernet 档 | Soft 或 Hard |
| `power_thermal` | 电池/插电、可接受温升与噪声 | TDP/功耗带、散热约束 | Hard（移动/密闭舱） |
| `environment` | 消费室内 / 车载 / 工业温宽 | 工作温度与环境等级 | Hard（车载/工业） |
| `sw_stack` | Android / Linux / 其他 | 官方支持 OS/BSP 期望 | Hard |
| `delivery_form` | 裸片自行设计 / 买模组快速出样 | SoC vs SoM 偏好 | Soft |
| `cost_band` | BOM 敏感区间（档位） | 主控成本带 | Soft（极少作 Hard） |
| `supply_life` | 寿命、供货地区/品牌约束 | 生命周期与可获得性约束 | Soft 或 Hard |

## Extension packs（按 sub_form / 功能触发）

纳入后与 Core 同等对待（须答完或 Unconstrained）。

| 触发 | Extension 示例 |
|------|----------------|
| 移动底盘 | 实时控制接口（CAN/UART 数量档）、IMU/电机相关外设期望 |
| 车载 | 车规/电源波动、车载接口、认证相关约束 |
| 多麦对话 | 音频接口、DSP/回声消除是否要在主控侧 |
| 强本地视觉 | 多 CSI lane、独立 ISP/NPU 协同说明 |
