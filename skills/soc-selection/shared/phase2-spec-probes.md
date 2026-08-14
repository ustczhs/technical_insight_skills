# Phase 2 Spec Detail Probes（按需 · 形态门控）

供 `soc-shortlist` 在搜索后扫描。**不是**每轮必问清单；仅当该项会改变 Hard 去留、Critical Claim 口径或 Match Band，且 Brief 未给出可执行规格时才追问。

每一探针的问询为 **Probe Turn**：与 Phase 1 Dimension Turn 同形——同一回复给出**取值 + `hard`/`soft`/`unconstrained`**（例：`A / Hard`）。

**与检索覆盖的关系**：候选可来自相邻营销品类（眼镜视觉 SoC、IPC 主控等）；本文件只门控**问哪些规格细节**，不门控**能否搜该类芯片**。搜全、问准：第一性原理看 Spec，不看品类标签。

## 0. 形态门控（先做再问）

探针必须跟 **Silicon Class**（主类；可用 `sub_form` / Extension 细化）对齐，**不要**按 Product Family 选包：

1. 从 Brief 读出 `primary_silicon_class`、`adjacent_silicon_classes`、相关 Hard，以及可选的 `sub_form`
2. **只加载**下方与主 Class（及确有分叉时的相邻 Class）对应的探针包；禁止用 `audio_sip` 包去问 `display_mcu` 方案
3. 在包内再按「通用触发」决定追问哪些；一次一问
4. 问法用**技术规格选项**（通道数、接口类型、UART 数量档），不要改成 Phase 1 体验 Framing
5. 对跨 Class 候选，仍用**本产品主 Class**探针口径对照其手册

| primary_silicon_class | 形态包入口 |
|----------------------|------------|
| `audio_sip` / `wifi_bt_combo` | §2：按 OWS / 入耳 / 眼镜 / 腕戴（可参考 Domain / sub_form） |
| `ap_som` / `lightweight_ap` | §3：按桌面 / 室内移动 / 车载 sub_form |
| `vision_soc` | §3.1 视觉相关探针 + §2.1 若有 ISP 分叉 |
| `vehicle_soc` | §3.4 车载 + 按需 §5 |
| `display_mcu` | §5 |
| `industrial_mcu` | §5（偏 UART/ADC/温宽） |
| 未登记 / `needs_seed_extension` | 声明扩展；仅挑与 Hard 明显相关的少量探针 |

记录格式：`probe_pack = <primary_silicon_class>[/<sub_form>]`，例如 `display_mcu` 或 `ap_som/vehicle-mounted`。


## 1. 通用触发

| 条件 | 动作 |
|------|------|
| Brief 已有明确 Dimension Answer / Framing–Spec Mapping | 不重复追问 |
| 候选在该属性上无差异、且不阻塞判定 | 跳过 |
| 缺公开数据导致 Hard 无法判定 | 先走 Uncertainty 类 Clarification；必要时再 Spec Detail |
| 属性实质是新产品能力（非硅片细节） | 建议回 Phase 1 改 Brief，勿用 Probe 伪装 Dimension Turn |
| 探针与当前形态包无关 | **禁止提问** |

## 2. Wearable AI（音频 SoC / SiP）

### 2.1 全形态共用（有视觉 Hard 时优先扫）

| probe_id | 何时值得问 | Spec 口径示例 | 默认推荐倾向 |
|----------|------------|---------------|--------------|
| `isp_topology` | 有视觉 Hard，候选片上无 ISP / 行业多为外挂 | on_die / external_ok | 量产常见 → `external_ok` |
| `sram_psram` | 拍照缓冲/轻模型与候选内存差大 | min_sram_band / psram_required | 轻量拍传 → 较低档 |
| `cam_iface` | 静帧路径依赖 DVP/SPI/MIPI 等 | required_iface_set / any_working_path | 有可工作路径即可 |
| `bt_integration` | Brief 未钉死单芯 vs 双芯连接 | on_soc_bt / dual_ok | 跟 Brief `bt_integration` |

### 2.2 开放式 OWS / 入耳耳机

| probe_id | 何时值得问 | Spec 口径示例 | 默认推荐倾向 |
|----------|------------|---------------|--------------|
| `audio_iface` | 麦路、DMIC/I2S、功放集成与候选外设表分叉 | mic_paths / amp_on_soc | 跟 `audio_chain` |
| `package_pin` | 腔体紧，WLCSP vs 大 BGA | prefer_wlcsp / mid_ok | OWS 偏 `prefer_wlcsp` 或 mid_ok |
| `storage_iface` | 本地暂存差异大 | spi_nor_ok / eMMC_required | 轻量 → SPI NOR |
| `wireless_extra` | Wi‑Fi 是否必要（耳塞通常否） | bt_only / wifi_optional | 默认 `bt_only` |
| `pmic_integration` | 续航 Soft + 集成度差大 | integrated_pmu_preferred | Soft |

### 2.3 AI 眼镜

| probe_id | 何时值得问 | Spec 口径示例 | 默认推荐倾向 |
|----------|------------|---------------|--------------|
| `display_out` | 有屏/光波导时：MIPI DSI lane、分辨率带 | dsi_lanes / no_display | 无屏拍照镜 → `no_display` |
| `wifi_throughput` | 传图/录像常走 Wi‑Fi | bt_only / wifi6_preferred | 有录像 Soft→可问 |
| `multi_mic_bone` | 骨传导麦 / 风噪方案 | bone_mic_ok / std_mems | Soft |
| `isp_topology` | 同 §2.1，眼镜量产多外挂 ISP | external_ok | `external_ok` |

### 2.4 腕戴

| probe_id | 何时值得问 | Spec 口径示例 | 默认推荐倾向 |
|----------|------------|---------------|--------------|
| `display_out` | 表盘 MIPI/SPI 屏 | mipi_dsi / spi_panel | 跟显示档 |
| `sensor_hub_if` | I2C/SPI 传感器数量档 | i2c_multi / unconstrained | Soft |
| `gnss_coex` | 是否要 GNSS/外挂共存 | gnss_optional | 常 unconstrained |

## 3. Companion Robot（AP / SoM）

机器人选型重点在 **外设与通道数量**，不要照搬耳机的 SRAM/ISP 小包；按 `sub_form` 加载。

### 3.1 全形态共用

| probe_id | 何时值得问 | Spec 口径示例 | 默认推荐倾向 |
|----------|------------|---------------|--------------|
| `uart_count` | 多外设/调试/模组：UART/USART 数量不够会否决候选 | ≥2 / ≥4 / ≥6 / unconstrained | 移动多外设 → 至少 ≥4 |
| `iface_types` | 需要哪些总线：I2C / SPI / CAN / RS485 / USB Host | required_set | 按底盘与传感器列出必选集合 |
| `display_channels` | 有屏 Hard：独立显示通道/接口数量与类型 | 1×MIPI-DSI / 2×DSI / LVDS / HDMI | 单屏消费 → `1×MIPI-DSI` |
| `csi_lanes_cams` | 有摄像 Hard：CSI 口数量、lane、是否同时开多路 | 1cam_2lane / 2cam / 4cam | 跟 `camera_video` |
| `isp_vpu` | 多摄/录像编码与候选 ISP·VPU 分叉 | isp_count / encode_codecs | 跟摄像档 |
| `dram_bandwidth` | 多路相机+显示同时开 | lpddr4_band 等 | 跟算力/视觉档 |
| `hi_speed_io` | 外扩存储/网口/加速卡 | USB3 / PCIe / GbE | 跟 `hs_io` |
| `npu_tops` | 端侧 AI 边界模糊 | tops_band / unconstrained | 跟 `on_device_ai` |
| `som_vs_chip` | 交付未落到可筛字段 | chip_ok / som_preferred | 跟 `delivery_form` |
| `storage_iface` | eMMC/UFS/SD 启动与容量档 | eMMC_ Mandatory / sd_ok | 消费机器人常 eMMC |

### 3.2 桌面固定

| probe_id | 何时值得问 | Spec 口径示例 | 默认推荐倾向 |
|----------|------------|---------------|--------------|
| `display_channels` | 桌面屏/双屏交互 | 1–2×DSI 或 HDMI | 单屏为主 |
| `usb_host_count` | 外设扩展（摄像扩展坞等） | ≥2 USB Host | Soft/Hard 视 Brief |
| `eth_required` | 是否必须有线网 | rj45_required / wifi_ok | 家用常 wifi_ok |
| `uart_count` | 调试 + 少量模组 | ≥2 | Soft |

### 3.3 室内移动（底盘）

| probe_id | 何时值得问 | Spec 口径示例 | 默认推荐倾向 |
|----------|------------|---------------|--------------|
| `uart_count` | 电机驱动/激光雷达/IMU 模组常占多路 UART | ≥4 / ≥6 | **优先追问** |
| `iface_types` | CAN / RS485 / 多路 I2C·SPI 是否必选 | can_required + … | 有轮毂/总线底盘 → 含 CAN |
| `realtime_io` | 是否要硬件 PWM / 正交编码接口 / 实时核 | pwm_abz / rpmsg_mcu | Soft 或 Hard |
| `csi_lanes_cams` | 导航相机 + 交互相机 | ≥2 cam | 常 Hard |
| `wireless_robot` | Wi‑Fi 6 / BT / 可选 4G 模组口（USB/PCIe/UART） | wifi_bt / modem_uart | Soft |

### 3.4 车载

| probe_id | 何时值得问 | Spec 口径示例 | 默认推荐倾向 |
|----------|------------|---------------|--------------|
| `iface_types` | 车载 CAN(-FD) / 车载以太网 | can_fd_required | 常 Hard |
| `display_channels` | 中控/副屏/仪表通道数 | multi_display | 跟显示档 |
| `serdes_link` | 是否要 FPD-Link / GMSL 类 | serdes_required / unconstrained | 远距屏/摄时问 |
| `automotive_grade` | 温宽/车规与候选分叉 | aecq_preferred | 跟 `environment` |
| `uart_count` | 车身模组与诊断口 | ≥4 | Soft/Hard |

## 4. 记录格式（写入 Shortlist）

须注明本轮加载的形态包，例如：`probe_pack = display_mcu` 或 `ap_som/indoor_mobile`。  
落盘位置：`SOC_SHORTLIST.md` 的**过程附录**（探针全表）；§1 结论区只保留一行摘要。详见 [shortlist-template.md](./shortlist-template.md)。

| probe_id | answer | grade | 影响 |
|----------|--------|-------|------|
| uart_count | >=4 | hard | UART&lt;4 的 SoC 进 Near-Miss |
| display_channels | 1x_mipi_dsi | hard | 无 DSI 的候选淘汰 |
| package_pin | mid_ok | soft | 仅影响 Match Band |

`grade`：`hard` \| `soft` \| `unconstrained`（与 Phase 1 / CONTEXT 同义；**不要**再写 apply_as / run_hard / run_soft / note_only）

### Probe Turn 回复示例

- `A / Hard`
- `B / Soft`
- `自定义：SRAM>2Mb / Hard`
- `U / Unconstrained`

## 5. Display / Industrial MCU（`display_mcu` / `industrial_mcu`）

小屏 HMI、表情屏、宽温控制主控：重点在 **显示接口、外设数量、片上内存、温宽与 RTOS**，不要默认套 `ap_som` 的 CSI/NPU 包。

| probe_id | 何时值得问 | Spec 口径示例 | 默认推荐倾向 |
|----------|------------|---------------|--------------|
| `display_channels` | LVDS/RGB/MIPI 与候选分叉 | 1×LVDS / RGB565 / MIPI-DSI | 跟 Brief 显示维 |
| `uart_count` | 舵机/模组/调试占口 | ≥2 / ≥4 | 跟控制 IO |
| `adc_count` | 模拟采样需求 | ≥2 / unconstrained | 跟 Brief |
| `sram_psram` | 帧缓冲/资源是否够 | sram_band / psram_required | 表情屏常要 PSRAM |
| `storage_iface` | NAND/NOR/eMMC 启动 | spi_nand_ok / eMMC | 跟 hs_io |
| `usb_host_device` | USB 角色 | host / device / otg | 跟 Brief |
| `rtos_sdk` | 仅 Linux 证据 vs RTOS | rtos_required / linux_ok | 跟 sw_stack |
| `temp_grade` | 工业/车载温区 OPN | minus30_85 / aecq | 跟 environment |

