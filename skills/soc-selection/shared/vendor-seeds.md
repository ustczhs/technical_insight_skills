# Vendor Seeds（Phase 2 检索种子）

**厂商覆盖矩阵**按 **Silicon Class** 分段，再叠加 **Application Domain** 加扫表。  
**不是** Shortlist 白名单；也**不再**按 Product Family 选表。

用法（`soc-shortlist` Step 2）：

1. 打开 Brief 的 `primary_silicon_class` + `adjacent_silicon_classes` → 合并对应 Class 表（国内+国外必扫行）
2. 打开每个 `application_domains` → 合并 Domain 加扫行
3. 中英双语定向 query；扫描表落盘后方可 `complete`
4. `needs_seed_extension=true` 时：尽力检索 + 文首降级声明，不得假装未登记域已覆盖

---

## Class · `audio_sip`（音频 SoC / SiP / 低功耗蓝牙音频）

### 国内（CN）— 必扫

| 厂商（中/英） | 检索锚（品牌 + 料号前缀/产品线） | 备注 |
|---------------|--------------------------------|------|
| 恒玄 / Bestechnic | BES2600、BES2700、BES2800 | OWS/TWS |
| 络达 / Airoha | AB15xx、AB16xx | SiP / Hybrid ANC |
| 物奇 / WuQi Micro | WQ70xx、WQ71xx | **须中文**官网/PDF |
| 炬芯 / Actions | ATS28xx、ATS30xx | |
| 中科蓝讯 / Bluetrum | AB56xx、BT89xx | |
| 杰理 / Jieli | JL70xx、AC79xx | |
| 瑞昱 / Realtek | RTL87xx（蓝牙音频线） | |

### 国外 / 跨国（Global）— 必扫

| 厂商 | 检索锚 | 备注 |
|------|--------|------|
| Qualcomm | QCC51xx、QCC30xx、S5 音频线 | |
| Nordic | nRF53、nRF54 | 偏低功耗 BLE 时 |
| Dialog / Renesas | DA14xxx | |
| Apple / 封闭生态 | 仅 Brief 接受非公开 SDK 时 | 常 Near-Miss |

---

## Class · `ap_som`（边缘 AP / SoM）

### 国内（CN）— 必扫

| 厂商 | 检索锚 | 备注 |
|------|--------|------|
| 瑞芯微 / Rockchip | RK35xx、RK3576、RK3588 | |
| 全志 / Allwinner | A/T/V 系列边缘 AP | |
| 晶晨 / Amlogic | A311D、S 系列 | |
| 华为海思 / HiSilicon | 公开可采买线 | 供货单独判 |
| 紫光展锐 / UNISOC | IoT/边缘线 | |
| 地平线 / Horizon | 征程（强视觉 NPU 时） | |

### 国外 / 跨国（Global）— 必扫

| 厂商 | 检索锚 | 备注 |
|------|--------|------|
| Qualcomm | RB5、QCS/QRB、Snapdragon 边缘 | |
| NXP | i.MX8、i.MX9、i.MX93 | |
| NVIDIA | Jetson Orin Nano/NX 等 | |
| Texas Instruments | AM62、TDA4 入门 | |
| Raspberry Pi / 工业 SoM | CM4/CM5 等 | |

---

## Class · `vision_soc`（视觉 / IPC / 运动相机）

### 国内 + 国外 — 必扫

| 厂商 | 检索锚 | 备注 |
|------|--------|------|
| 君正 / Ingenic | T 系列等 | |
| 安凯 / Anyka | 公开 IPC 线 | |
| 国科微 / Goke | 公开视觉线 | |
| 全志 / Rockchip | V/RV 视觉向 | |
| Ambarella | CV2/CV5 入门线 | |
| 海思 / HiSilicon | Hi35xx 公开线 | 供货约束 |

---

## Class · `display_mcu`（显示控制 / 表情屏 MCU）

### 国内 + 国外 — 必扫

| 厂商 | 检索锚 | 备注 |
|------|--------|------|
| 匠芯创 / ArtInChip | D13x、D21x | LVDS/RGB + PSRAM 常见 |
| 兆易创新 / GigaDevice | GD32 带显示/LTDC 线 | |
| 国民技术 / Nations | N32 显示向 | |
| 乐鑫 / Espressif | ESP32-P4 / 带屏方案（若 Hard 允许） | |
| ST | STM32H7/U5 + LTDC/DSI | |
| NXP | i.MX RT 跨界 MCU | |
| 全志 | 低端显示/车机 MCU 线（公开料） | |

---

## Class · `industrial_mcu`（工业宽温 / 多外设 MCU）

### 国内 + 国外 — 必扫

| 厂商 | 检索锚 | 备注 |
|------|--------|------|
| 兆易创新 / GigaDevice | GD32 工业温区 | |
| 士兰 / Silan 等国产 MCU | 公开工业线 | 按 Hard 相关性 |
| ST | STM32 工业 / 宽温 OPN | |
| NXP | MCX / i.MX RT 工业 | |
| Texas Instruments | Sitara AM62 旁路对照；MSP/实时线按接口 | |
| 匠芯创 / ArtInChip | D13x 工业温区 SKU | 与 display_mcu 可重叠评估 |

---

## Class · `vehicle_soc`（车载 / 座舱 / 仪表）

### 国内 + 国外 — 必扫

| 厂商 | 检索锚 | 备注 |
|------|--------|------|
| 全志 | T5xx 车载 / 仪表线 | |
| 瑞芯微 | 车载/仪表公开线 | |
| 芯驰 / SemiDrive | 座舱/仪表 | |
| 杰发 / AutoChips | 车机/仪表 | |
| 紫光展锐 | 车载公开线 | |
| NXP | i.MX 车载 / S32 入门对照 | |
| TI | Jacinto / AM 车载入门 | |
| Renesas | R-Car 入门 | |

---

## Class · `lightweight_ap` / `wifi_bt_combo`

- `lightweight_ap`：在 `ap_som` 表中优先扫低功耗/带屏 IoT AP（全志入门、Rockchip 入门、ESP32-P4 等），并补君正等轻量线。
- `wifi_bt_combo`：在 `audio_sip` 表中优先扫带 Wi‑Fi 变体（BES Wi‑Fi、部分 Realtek），外加乐鑫等复合连接料。

---

## Domain Overlay（行业加扫 · 每域固定必扫行）

以下行与 Class 表 **并入**扫描义务；未扫完不得 `complete`。入选仍只看 Hard；Domain 命中可抬 Match Band。

### `motorcycle` / `light_ev`（两轮 · 可合并执行）

| 加扫锚 | 检索提示 |
|--------|----------|
| 摩托车 / 电摩 **仪表盘** SoC·MCU 方案 | 中文：「摩托车仪表芯片」「电摩仪表 MCU LVDS」 |
| 两轮 **车机 / 中控** 国产方案 | 芯驰/杰发/全志车载公开料 + 方案商 |
| 车载 **表情 / 助手** 小屏主控 | 显示 MCU + 宽温；对照 NOMI 类交互硬件拆解仅作线索 |
| 电动车 **仪表芯片** 供应商名录 | 须至少 1 次中文定向 + 1 次英文/原厂 |

### `automotive_cabin`

| 加扫锚 | 检索提示 |
|--------|----------|
| 座舱 SoC 公开可采买线 | 芯驰、半驱、高通座舱入门对照 |
| 车载仪表 / 副驾娱乐主控 | 与 `vehicle_soc` 重叠时合并 assessed，勿重复凑数 |

### `desktop_companion` / `indoor_mobile_robot`

| 加扫锚 | 检索提示 |
|--------|----------|
| 桌面机器人 / 室内机器人参考主控 | 常见 RK/全志/晶晨方案；有视觉 Hard 时叠加 `vision_soc` |

### `ows_earbuds` / `ai_glasses` / `wrist_wearable`

| 加扫锚 | 检索提示 |
|--------|----------|
| 对应形态公开 SiP/主控方案 | 与 `audio_sip` / 眼镜视觉线合并扫描 |

### `industrial_hmi`

| 加扫锚 | 检索提示 |
|--------|----------|
| 工业串口屏 / 宽温 HMI MCU | 与 `display_mcu`、`industrial_mcu` 合并 |

### `generic_iot`

无额外行业行；仅 Class 矩阵。

---

## 检索质量底线

1. **矩阵行覆盖**：本轮涉及的每个 Class 必扫行 + 每个 Domain 加扫行，均须有扫描表状态。
2. **双语**：默认 Class 至少一半厂商用**中文** query；物奇/蓝讯/杰理/炬芯等禁止只跑英文判无。
3. **原厂优先**：产品中心、datasheet、SDK；二手转载仅 [B]/[C]。
4. **禁止**：只用一条泛搜结束；禁止按 Product Family 打开旧「族表」替代 Class∪Domain；禁止把矩阵当唯一候选池。
