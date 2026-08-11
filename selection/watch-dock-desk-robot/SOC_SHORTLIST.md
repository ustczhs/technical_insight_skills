# SoC Shortlist: 手表底座桌面机器人（办公桌助理）

## 0. 元信息

| 字段 | 值 |
|------|-----|
| schema_version | 1 |
| product_slug | watch-dock-desk-robot |
| product_family | companion_robot |
| target_silicon_class | AP / SoM |
| brief_path | ./SELECTION_BRIEF.md |
| info_cutoff | 2026-08-11 |
| probe_pack | companion_robot/desktop_fixed |

**Phase 2 Clarification 记录**

| 类型 | 结论 |
|------|------|
| Spec Detail Probe | 见 §1b（3 条）；`display_channels` 在 Brief 修订后对本轮筛选失效 |
| Brief 修订 | 2026-08-11：`display` → `unconstrained`（底座主控可不带 MIPI/SPI/HDMI；表情在手表） |
| Uncertainty | 渠道价≠ BOM；AEC 多为「接口 + 软件/DSP 算法」可落地，非整芯硬 IP 清单 |
| 归属确认 | 修订后重排；维持下方 Shortlist / Near-Miss |

## 1. 筛选摘要

- Hard Constraint 条数：**5**（Brief；已去掉 `display`）
- Shortlist 数量：**5**
- Near-Miss 数量：**2**
- 主要不确定点：入门 BOM 价依赖渠道；被动散热与整机热设计相关（SoC TDP ≠ 整机壳温）
- Phase 2 Clarification：Probe×3；Brief 显示维修订后重筛一轮

本轮相对上一稿变化：

- **不再**因缺 MIPI/SPI/HDMI 淘汰或降权
- 排序更看重：**轻量 NPU + 入门成本 + 被动散热 + 双麦 AEC 可落地 + Linux**
- 音频链路强、显示冗余的料（如 i.MX 8M Plus）相对上一稿略升；仍受 entry Soft 压制

## 1b. Spec Detail Probe 记录

| 字段 | 值 |
|------|-----|
| probe_pack | `companion_robot/desktop_fixed` |

| probe_id | answer | grade | 影响 |
|----------|--------|-------|------|
| display_channels | SPI/RGB 小屏即可（历史答） | soft | **本轮失效**：Brief 已将 `display` 标为 unconstrained；不筛不排 |
| uart_count | ≥2 | soft | UART&lt;2 降 Match Band（桌面极少见） |
| npu_tops | 有专用 NPU 即可 | soft | 不设 TOPS 下限；有 NPU 即满足该 Soft |

跳过：`eth_required`（Brief `hs_io` 已 USB2 Soft）；`csi_lanes_cams`（摄像仅为 Soft，候选无 Hard 分叉）；硬 DSP AEC vs 软件 AEC（Brief 已写「等价可落地链路」）。

## 2. Hard Constraints 应用表

| id | Spec 摘要 | 结果策略 |
|----|-----------|----------|
| sub_form | desktop_fixed | 桌面固定 AP/SoM；排除底盘/车规专向门槛 |
| on_device_ai | light 端侧 AI | 须有专用 NPU（轻量即可） |
| power_thermal | 插电 + 被动/极低噪声 | 典型负载下可被动散热；持续需风扇的高功耗料 Near-Miss |
| environment | consumer indoor | 消费室内即可 |
| audio_dialog | ≥2 mic + 主控侧 AEC/降噪或等价 | I2S/PDM 等多麦通路 + 可落地 AEC（软/DSP） |
| display | （已移除 Hard） | unconstrained |

## 3. SoC Shortlist

按 Match Band：**高匹配 → 中匹配 → 低匹配**。

### 高匹配

#### Rockchip RK3566

| 字段 | 值 |
|------|-----|
| part | RK3566 |
| vendor | Rockchip（瑞芯微） |
| silicon_class | ap_som |
| match_band | high |

**Hard 判定**

| id | verdict | 证据 |
|----|---------|------|
| sub_form | pass | [A] 消费/嵌入式多媒体 AP，广泛 SoM/SBC（信息时效：2021–2024，https://rockchip.fr/RK3566%20datasheet%20V1.1.pdf）；[B] 桌面/HMI 类应用常见（信息时效：2024+，https://www.rocktech.com.hk/rocktech-blog/rockchip-sbc-for-industrial-hmi/） |
| on_device_ai | pass | [A] 内置 NPU 约 0.8–1 TOPS（datasheet / Geniatech）；[B] RKNN Linux 部署（https://wiki.t-firefly.com/en/ROC-RK3566-PC/usage_npu.html） |
| power_thermal | pass | [B] Firefly ROC-RK3566-PC 标称 Normal ~2.5W / Max ~5.25W（信息时效：厂商规格，https://download.t-firefly.com/Spec/Mainboards/ROC-RK3566-PC_Specification_EN.pdf）；[B] 工业 HMI 文称成本与功耗平衡、被动方案常见（rocktech 对比文） |
| environment | pass | 消费/商业室内 SoC，非车规专向 |
| audio_dialog | pass | [B] RK356x 开发板双麦矩阵/降噪方案（https://pic-microcontroller.com/rk3568-development-board-features-voice-noise-reduction/）；[C] 平台侧多麦 + AEC 算法接入 HAL 路径可落地（https://www.elecfans.com/d/7401321.html）— Critical Claim 以「PDM/I2S 多麦通路 + 软件 AEC」口径，非硬 IP 清单 |

**Soft 判定**

| id | verdict | 说明 |
|----|---------|------|
| compute_band | met | 四核 A55，中端多任务够用 |
| camera_video | met | MIPI CSI 可用（偏好项，非必须） |
| hs_io | met | USB2 足够 |
| sw_stack | met | Linux Buildroot/Debian/Yocto 生态成熟 |
| delivery_form | met | 裸片 + 大量 SoM |
| cost_band | met | 入门桌面机器人主控主流价位带 |
| supply_life | met | 模组商与 SDK 路径多 |
| base_pan / probe:uart_count | met | GPIO PWM + 多 UART |
| probe:npu_tops | met | 有专用 NPU |

**Uncertainty**

- 精确代理商单价随容量/封装波动
- AEC 质量依赖算法与声学结构，非芯片单字段保证

**来源**

| URL | grade | dated |
|-----|-------|-------|
| https://rockchip.fr/RK3566%20datasheet%20V1.1.pdf | A | ~2021（现状引用按 freshness 规则作交叉） |
| https://www.geniatech.com/product/xpi-3566/ | B | 持续在售页 |
| https://download.t-firefly.com/Spec/Mainboards/ROC-RK3566-PC_Specification_EN.pdf | B | 厂商规格 |

对比说明：修订后无显示压力，仍是 **entry + 轻 NPU + 被动散热 + Linux** 的默认高匹配。

#### Rockchip RK3562

| 字段 | 值 |
|------|-----|
| part | RK3562 |
| vendor | Rockchip（瑞芯微） |
| silicon_class | ap_som |
| match_band | high |

**Hard 判定**

| id | verdict | 证据 |
|----|---------|------|
| sub_form | pass | [B] 工业/消费 SoM（Forlinx/Firefly/Boardcon） |
| on_device_ai | pass | [B] 内置约 1 TOPS NPU（https://www.forlinx.net/product/fet3562-up4-rockchip-rk3562-som-182.html；Firefly iCore-3562 规格 PDF） |
| power_thermal | pass | [B] 22nm 级低功耗定位、SoM 5V 供电常见；与 RK3566 同档被动友好（模组规格） |
| environment | pass | 消费/工业室内档均有 |
| audio_dialog | pass | [B] 模组引出 I2S 等音频口（Boardcon MINI3562）；AEC 同属「主控侧软件/方案可落地」口径 |

**Soft 判定**

| id | verdict | 说明 |
|----|---------|------|
| compute_band | partial | 四核 A53，偏轻中端；语音+轻任务通常够，重 UI 不如 A55/3566 |
| camera_video | met | 多路 MIPI CSI 常见 |
| cost_band | met | 入门/替代 3566 的成本向选项 |
| sw_stack / supply_life | met | Android14 / Linux 模组 SDK |
| probe:uart_count | met | 模组常见 ≥5 UART |
| probe:npu_tops | met | 有 NPU |

**Uncertainty**

- 与 RK3566 的渠道价差因批次而异
- 官方公开详细 datasheet 可得性弱于 3566，多依赖模组商 [B]

对比说明：无显示 Hard 后仍高匹配；算力 Soft 略弱于 3566，成本/供货接近。

### 中匹配

#### Allwinner T527

| 字段 | 值 |
|------|-----|
| part | T527 |
| vendor | Allwinner（全志） |
| silicon_class | ap_som |
| match_band | mid |

**Hard 判定**

| id | verdict | 证据 |
|----|---------|------|
| on_device_ai | pass | [A] 官方页 NPU 2 TOPS（https://www.allwinnertech.com/index.php?a=index&c=product&id=110&solveid=35） |
| audio_dialog | pass | [A] 集成 HiFi4 DSP + 多路 I2S/ADC（同上）；[B] MYIR SoM 音频外设表（https://en.myir.cn/datasheet/MYC-LT527.pdf） |
| power_thermal | pass | 八核 A55 工业定位；轻负载被动可行，重载需热设计验证（Uncertainty→不升 Hard 否决） |
| sub_form / environment | pass | 智慧终端/工业交互，室内桌面可用 |

**Soft 判定**

| id | verdict | 说明 |
|----|---------|------|
| compute_band | met | 八核 A55，中端以上 |
| cost_band | partial | 相对 RK 入门线通常更偏工业中端 |
| sw_stack | partial | Tina/厂商 Linux + MYIR Yocto；主线生态弱于 RK/NXP |
| supply_life | partial | 有 SoM，但消费桌面模组密度低于 RK356x |
| probe:npu_tops / uart_count | met | 2 TOPS；UART 丰富 |

对比说明：无显示后音频 DSP 优势更明显，但仍受成本与 Linux 生态 Soft 压在中匹配。

#### NXP i.MX 8M Plus

| 字段 | 值 |
|------|-----|
| part | i.MX 8M Plus |
| vendor | NXP |
| silicon_class | ap_som |
| match_band | mid |

**Hard 判定**

| id | verdict | 证据 |
|----|---------|------|
| on_device_ai | pass | [A] NPU 至 2.3 TOPS（https://www.nxp.com/products/i.MX8MPLUS） |
| audio_dialog | pass | [A] HiFi4 DSP；官方表述含 keyword / noise reduction / beamforming / AEC 类语音能力（产品页 / Fact Sheet） |
| power_thermal | pass | [A] 有功耗应用笔记；插电被动在语音助理负载下常见可做（需整机验证） |
| sub_form / environment | pass | 工业/消费多媒体 AP |

**Soft 判定**

| id | verdict | 说明 |
|----|---------|------|
| compute_band | met | 四核 A53 + M7，中端扎实 |
| cost_band | unmet | 显著高于入门 RK 线 |
| sw_stack / supply_life | met | Yocto/官方 BSP 长供货强 |
| camera_video | met | 双 CSI + ISP（超出 Soft 需求） |
| probe:npu_tops / uart_count | met | |

对比说明：**修订后升势最大**——显示能力闲置不再扣分；音频 Hard 证据最强。仍因 **entry Soft unmet** 留在中匹配。

### 低匹配

#### Amlogic A311D

| 字段 | 值 |
|------|-----|
| part | A311D |
| vendor | Amlogic |
| silicon_class | ap_som |
| match_band | low |

**Hard 判定**

| id | verdict | 证据 |
|----|---------|------|
| on_device_ai | pass | [A] NPU 至 5 TOPS（Khadas A311D datasheet / VIM3） |
| audio_dialog | pass | [A] 多路 I2S/TDM/PDM（含多路 DMIC）（https://dl.khadas.com/products/vim3/datasheet/a311d-datasheet.pdf） |
| power_thermal | pass* | 轻负载可被动；六核 A73/A53 峰值高于 3566，整机安静被动余量弱于入门 RK（*边缘通过，Match Band 降权） |
| sub_form / environment | pass | |

**Soft 判定**

| id | verdict | 说明 |
|----|---------|------|
| compute_band | met | 算力偏强 |
| cost_band | unmet | 相对 entry 偏高 |
| sw_stack / supply_life | partial | Linux 有社区/SBC 路径，消费机器人模组密度与长供货叙事弱于 NXP/RK 工业线 |
| probe:npu_tops | met | 有 NPU（算力过剩，不扣 Hard） |

对比说明：无显示后仍进 Shortlist；入门成本 + 被动安静偏好下保持 **低匹配**。

## 4. Near-Miss（非 Shortlist 成员）

| 型号 | 违反的 Hard Constraint | 建议回谈放宽？ | 证据 |
|------|------------------------|----------------|------|
| Raspberry Pi CM4 | `on_device_ai`（无专用 NPU） | 仅当改为「允许纯 CPU 轻模型 / 无 NPU」时回 Phase 1 | [A] CM4 datasheet 无 NPU 规格（https://pip-assets.raspberrypi.com/categories/634-raspberry-pi-compute-module-4/documents/RP-008168-DS-4-cm4-datasheet.pdf） |
| Rockchip RK3588 | `power_thermal`（持续负载常需主动风扇，与被动/极安静冲突） | 若接受小风扇 Soft 化散热 Hard，可回 Phase 1 后重跑 | [B] 满载约 12–18W、建议主动散热（多源 SBC 评测/选购指南）；[B] 产线推理常见需风扇或强风道（https://www.cognivis.co.uk/insights/edge-ai-rock-5b） |

## 5. 空清单处理

不适用（Shortlist 非空）。

## 6. 证据附录

- 分级：A > B > C；Critical Claim ≥2 独立来源
- Freshness：>48 月的 [A] 用于现状时降为 [B]
- 信息截止：见元信息表 `info_cutoff`
- Brief 修订要点：底座主控 **不要求** 任何显示输出；手表承担屏幕表情
