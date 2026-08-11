# Selection Brief: 手表底座桌面机器人（办公桌助理）

## 0. 元信息

| 字段 | 值 |
|------|-----|
| schema_version | 1 |
| brief_status | brief_ready |
| product_name | 手表底座桌面机器人（办公桌助理） |
| product_slug | watch-dock-desk-robot |
| product_family | companion_robot |
| target_silicon_class | AP / SoM |
| created | 2026-08-11 |
| updated | 2026-08-11（修订：display → unconstrained） |

## 1. 产品概念（选型所需最小描述）

智能手表配合专用底座，上座后构成办公桌助理形态的桌面机器人。必须能力：语音对话、底座水平转动。屏幕表情由手表侧承担（上座后仍用表盘/手表显示），**底座主控可不带显示输出**（MIPI/SPI/HDMI 等均可不要求）。手表可独立佩戴使用；底座可待机。本 Brief 选型对象为**桌面机器人主控（底座侧 / 整机 AP·SoM）**，不覆盖手表腕上低功耗主控。

## 2. Product Family

| 项 | 内容 |
|------|------|
| 选定 | companion_robot |
| 推断理由 | 桌面固定、语音交互、屏幕表情、底座转动，属桌面陪伴/助理机器人；Target Silicon Class 为 AP/SoM |
| 产品确认 | 是 |

## 3. Target Silicon Class

本族默认：**AP / SoM 为主**。本 Brief 确认搜索桌面机器人应用处理器或系统模组；不将手表端音频 SoC/低功耗主控作为 Shortlist 主类。

## 4. Dimensions

### 4.1 维度总表

| id | phase | Product Framing（摘要） | Dimension Answer | Spec Field（摘要） | Framing–Spec Mapping | grade | 推荐等级 | 已确认 |
|----|-------|-------------------------|------------------|--------------------|----------------------|-------|----------|--------|
| sub_form | core | 桌面固定，底座可水平转动 | option:`desktop_fixed` 桌面固定 | 形态标签：desktop_fixed；排除移动底盘/车载 | 「办公桌底座」↔ sub_form=desktop_fixed | hard | hard | 是 |
| compute_band | core | 语音+表情+轻任务并行流畅 | option:`mid` 中端多任务 | CPU 性能带：mid | 「中端多任务」↔ cpu_band=mid | soft | soft | 是 |
| on_device_ai | core | 轻量本地：离线唤醒/关键词等 | option:`light` 轻量本地 AI | NPU/端侧 AI 带：light；非无 NPU、非重度本地大模型 | 「轻量本地」↔ on_device_ai=light | hard | hard | 是 |
| display | core | 底座主控无显示要求（表情在手表） | unconstrained | 不要求 MIPI/SPI/HDMI 等显示输出 | 「可不带显示」↔ display=unconstrained | unconstrained | hard | 是 |
| camera_video | core | 单路轻视觉：人在场/朝向 | option:`single_light` 单路约 720p 轻视觉 | CSI/ISP：单路轻视觉；约 720p 级；非多路/非录像刚需 | 「轻视觉」↔ camera=single_light_720p | soft | soft | 是 |
| hs_io | core | 基础 USB 调试/外设即可 | option:`usb2_basic` USB 2.0 级基础 | 高速互联：USB2 基础档；不强制 USB3/Eth/PCIe | 「基础 USB」↔ hs_io=usb2_basic | soft | soft | 是 |
| power_thermal | core | 插电、被动散热、安静不烫 | option:`plugged_passive` 插电被动散热 | 功耗/散热：插电；被动/极低噪声；低外壳温升；非电池主供 | 「插电被动」↔ power_thermal=plugged_passive | hard | hard | 是 |
| environment | core | 消费级室内办公环境 | option:`consumer_indoor` 消费室内 | 环境等级：consumer indoor；非车载/工业温宽 | 「办公室内」↔ env=consumer_indoor | hard | hard | 是 |
| sw_stack | core | 嵌入式 Linux | option:`linux` Linux | 目标 OS/BSP：Linux（Yocto/Buildroot/Debian 等） | 「Linux」↔ sw_stack=linux | soft | hard | 是 |
| delivery_form | core | SoM 或裸片均可 | option:`either` SoM 或裸片 | 交付形态：SoC 与 SoM 均可入选 | 「均可」↔ delivery=either | soft | soft | 是 |
| cost_band | core | 入门敏感，压主控成本 | option:`entry` 入门敏感 | 主控成本带：entry | 「入门敏感」↔ cost_band=entry | soft | soft | 是 |
| supply_life | core | 主流稳定供货 + 可维护 BSP | option:`mainstream_supply` 主流稳定供货 | 可获得性：主流量产路径与可维护 Linux BSP | 「主流供货」↔ supply=mainstream | soft | soft | 是 |
| audio_dialog | extension | 双麦 + 主控侧 AEC/降噪 | option:`dual_mic_aec` 双麦+主控 AEC | 音频：≥2 mic；主控侧 AEC/通话降噪能力或等价可落地链路；I2S/PDM 等接口 | 「双麦对话」↔ audio=dual_mic_soc_aec | hard | hard | 是 |
| base_pan | extension | 简单舵机/电机水平一轴 | option:`simple_pan` PWM/UART 一轴 | 运动接口：PWM 或 UART 控水平一轴舵机/电机即可 | 「底座水平转」↔ base_pan=pwm_or_uart | soft | soft | 是 |

### 4.2 维度备注

#### sub_form

- 提供过的选项：桌面固定 / 室内移动 / 车载 / 自定义 / Unconstrained
- 等级：Hard（锁定桌面，排除移动/车载 Extension 路径）

#### compute_band

- 提供过的选项：入门流畅 / 中端多任务 / 高端重度
- 等级：Soft（体验档位，不卡死候选池）

#### on_device_ai

- 对话可云端；本地侧重离线唤醒、VAD/关键词等轻量能力
- 等级：Hard（依赖轻量本地 AI 时剔除无/过弱端侧加速路径）

#### display

- 原：单屏入门 Hard（屏幕表情）
- **2026-08-11 修订**：产品确认底座主控可不带显示（表情在手表）；`unconstrained`，Phase 2 不按显示接口筛选/排序
- 提供过的选项曾含：无屏 / 单屏入门 / 单屏高清 / 多屏

#### camera_video

- 非必须；偏好单路人在场/朝向，底座转动可不依赖视觉
- 等级：Soft

#### sw_stack

- 推荐等级曾为 Hard；产品确认为 Soft（Linux 偏好，不强制淘汰非 Linux）

#### audio_dialog

- 触发：必须语音对话
- 提供过的选项：单麦 / 双麦+主控 AEC / 多麦阵列 / 外挂 DSP / 自定义

#### base_pan

- 触发：必须底座水平转动
- 提供过的选项：简单舵机 / 带反馈伺服 / 外挂运动 MCU / 自定义

## 5. Hard Constraints（汇总）

- `sub_form`：形态 = desktop_fixed（桌面固定）
- `on_device_ai`：端侧 AI 带 = light（轻量本地）
- `power_thermal`：插电 + 被动/极低噪声散热、低外壳温升
- `environment`：消费级室内
- `audio_dialog`：≥2 mic + 主控侧 AEC/通话降噪（或等价可落地链路）

## 6. Soft Preferences（汇总）

- `compute_band`：cpu_band = mid
- `camera_video`：单路轻视觉约 720p
- `hs_io`：USB2 基础档
- `sw_stack`：Linux BSP 偏好
- `delivery_form`：SoM 或裸片均可
- `cost_band`：entry（入门敏感）
- `supply_life`：主流稳定供货 + 可维护 BSP
- `base_pan`：PWM/UART 水平一轴即可

## 7. Unconstrained

- `display`（底座主控无显示输出要求；MIPI/SPI/HDMI 均可不要求）

## 8. Brief Ready 检查

- [x] Product Family 已确认（或 Out-of-Family 已明示）
- [x] Profile 内全部 Core 均有 Dimension Answer
- [x] 已纳入的 Extension 均有 Dimension Answer
- [x] 每项等级已在 Dimension Turn 中确认
- [x] Framing–Spec Mapping 均已写明

全部勾选；`brief_status` = `brief_ready`。
