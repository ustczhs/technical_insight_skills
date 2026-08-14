# Silicon Classes（v1 枚举）

Phase 2 **形态种子**与 **Spec Detail Probe** 的主键。Brief 元信息：

| 字段 | 含义 |
|------|------|
| `primary_silicon_class` | 恰好 1 个 id |
| `adjacent_silicon_classes` | 0～N 个 id（逗号分隔或列表） |
| `needs_seed_extension` | `true` / `false`：未登记类或自定义映射失败时 |

## 枚举

| id | 标签 | 典型用途 | 默认探针包 |
|----|------|----------|------------|
| `ap_som` | AP / SoM | 边缘 Linux/Android 主控、机器人算力板 | § robot_ap（原 companion AP 包） |
| `vision_soc` | 视觉 / IPC SoC | 多摄 ISP、录像、AI 视觉 | § vision |
| `audio_sip` | 音频 SoC / SiP | TWS/OWS、蓝牙音频 | § audio_sip |
| `display_mcu` | 显示控制 MCU | 表情屏、仪表小屏、LVDS/RGB + 外设 | § display_mcu |
| `industrial_mcu` | 工业 / 宽温 MCU | 温宽、多 UART/ADC、RTOS | § industrial_mcu |
| `vehicle_soc` | 车载 SoC | 座舱/仪表/两轮车机主控 | § vehicle |
| `lightweight_ap` | 轻量 AP | 带屏可穿戴、低功耗 Linux | § lightweight_ap |
| `wifi_bt_combo` | Wi‑Fi+BT 复合 | 传图耳机、联网外设主控 | § audio_sip（偏无线） |

未知形态：选最接近 id，并设 `needs_seed_extension=true`。

## Hard → 相邻 Class 触发（Ready 前复核）

| 触发条件（Brief Hard / 明确 Soft 能力） | 建议加入 adjacent |
|----------------------------------------|-------------------|
| 多路 CSI / 本地 ISP / 录像编码 | `vision_soc` |
| 单芯片蓝牙音频 / ANC / TWS SDK | `audio_sip` |
| LVDS/小分辨率表情屏 + RTOS/裸机 + 多 UART/ADC | `display_mcu`、`industrial_mcu` |
| 车规温宽或明确车载座舱/仪表 | `vehicle_soc` |
| 需 Linux/Android 应用生态且主类为 MCU | `ap_som` 或 `lightweight_ap` |
| 明确 Wi‑Fi 传图且主类为纯 BT 音频 | `wifi_bt_combo` 或含 Wi‑Fi 的 `audio_sip` 变体 |

规则是**建议加扫**；产品确认后写入 `adjacent_silicon_classes`。与 Application Domain **并存**（域管行业，本表管能力）。

## Family → 推荐主类（仅推荐，可改）

| Product Family | 推荐 primary（可覆盖） |
|----------------|------------------------|
| `companion_robot` | `ap_som` |
| `wearable_ai` | `audio_sip` |
| `out_of_family` | 无默认；必须由概念选定 |
