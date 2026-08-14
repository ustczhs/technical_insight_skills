# Application Domains（v1 词表）

**应用域** = 产品整机/行业品类线索，驱动 Phase 2 **行业加扫**，与 Silicon Class 叠加。  
Brief 元信息：`application_domains`（可多选 id，逗号分隔）；自定义未入表 → `needs_seed_extension=true`。

## 词表

| id | 标签 | 加扫焦点（摘要） |
|----|------|------------------|
| `motorcycle` | 摩托车 / 摩旅车机 | 摩托车仪表、车载表情/助手、两轮 HMI 主控方案 |
| `light_ev` | 轻型电动车 | 电动自行车/电摩仪表与中控、国产车规 MCU/SoC 方案 |
| `automotive_cabin` | 汽车座舱 | 座舱 SoC、车载仪表、NOMI 类交互参考主控 |
| `desktop_companion` | 桌面陪伴 | 桌面机器人 / 屏幕助手 AP·SoM |
| `indoor_mobile_robot` | 室内移动机器人 | 底盘+视觉常见 AP / 视觉 SoC |
| `ows_earbuds` | 开放式/OWS 耳机 | 音频 SiP、ANC、低功耗蓝牙 |
| `ai_glasses` | AI 眼镜 | 眼镜主控、轻量视觉、Wi‑Fi 传图 |
| `wrist_wearable` | 腕戴 | 手表/手环主控、低功耗显示 |
| `industrial_hmi` | 工业 HMI / 宽温屏 | 工业串口屏、宽温显示 MCU |
| `generic_iot` | 通用 IoT | 无强行业线索时的兜底 |

## Phase 1 用法

1. 开跑时从产品标题/概念推断 1～N 个域 → 产品确认（可多选 + 自定义）
2. 「优先摩托车/电动车芯片」须落成域 id，**不要**只写在 Soft 散文里
3. 自定义域：写入 Brief，并 `needs_seed_extension=true`

## 与 Soft 的关系

Domain 选择消化「行业优先」；其后 Soft 可建议加搜，但**不**单独挡 `shortlist_status=complete`（完成闸门看 Class∪Domain 必扫行）。
