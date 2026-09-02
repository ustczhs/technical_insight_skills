# Application Domains（词表 · 可扩展）

**应用域** = 产品整机/行业品类线索，驱动 Phase 2 **行业加扫**，与 Silicon Class 叠加。  
Brief 元信息：`application_domains`（可多选 id）；自定义未入表 → `needs_seed_extension=true`。  
门户推断时词表是**提示库不是上限**，可输出自定义 id。

## 词表

| id | 标签 | 加扫焦点（摘要） |
|----|------|------------------|
| `motorcycle` | 摩托车 / 摩旅车机 | 摩托车仪表、车载表情/助手、两轮 HMI |
| `light_ev` | 轻型电动车 | 电动自行车/电摩仪表与中控 |
| `automotive_cabin` | 汽车座舱 | 座舱 SoC、车载仪表、交互助手 |
| `desktop_companion` | 桌面陪伴 | 桌面机器人 / 屏幕助手 |
| `indoor_mobile_robot` | 室内移动机器人 | 底盘+视觉常见 AP / 视觉 SoC |
| `child_companion` | 儿童陪育 / 早教机器人 | 陪育内容、安全交互、儿童场景主控 |
| `ows_earbuds` | 开放式/OWS 耳机 | 音频 SiP、ANC、低功耗蓝牙 |
| `ai_glasses` | AI 眼镜 | 眼镜主控、轻量视觉、Wi‑Fi 传图 |
| `wrist_wearable` | 腕戴 | 手表/手环主控、低功耗显示 |
| `voice_recorder` | 录音豆 / 便携录音 / 会议麦 | 录音、转写、蓝牙回传 |
| `smart_speaker` | 智能音箱 / 桌面语音助手 | 远场拾音、扬声、联网主控 |
| `service_robot` | 服务机器人 / 导览接待 | 商用服务、移动底盘 |
| `outdoor_robot` | 户外 / 割草 / 配送机器人 | 户外环境、动力与定位 |
| `doorbell_camera` | 门铃 / 看护摄像头 | 低功耗摄像、推流 |
| `dashcam` | 行车记录仪 / 车载影像 | 录像编码、车规环境 |
| `drone` | 无人机 / 航拍 | 飞控协同、影像 SoC |
| `tablet_kiosk` | 平板 / 展陈 / 点餐屏 | 大屏 AP、触控 HMI |
| `smart_home_hub` | 智能家居中枢 / 网关 | 多协议联网、网关主控 |
| `pet_camera` | 宠物摄像头 / 宠物陪伴 | 看护摄像、语音 |
| `conference_av` | 会议音视频 / 拾音扬声 | 会议麦阵、音箱 |
| `ar_hud` | AR HUD / 抬头显示 | 投影显示、车载光学 |
| `medical_wearable` | 医疗健康穿戴 | 合规传感、低功耗 |
| `industrial_gateway` | 工业网关 / 边缘盒 | 工业协议、宽温 |
| `logistics_robot` | 仓储物流机器人 | AGV/AMR 主控 |
| `handheld_terminal` | 手持终端 / PDA | 扫码、手持 Linux/RTOS |
| `industrial_hmi` | 工业 HMI / 宽温屏 | 工业串口屏、宽温显示 MCU |
| `generic_iot` | 通用 IoT | 无强行业线索时的兜底 |

## Phase 1 用法

1. 推断检索范围：候选池 ∪ 本案选定 Domain  
2. 自定义域写入 Brief，并 `needs_seed_extension=true`  
3. Phase 2 只扫**最终确认**的 Domain，不以候选池为必扫矩阵
