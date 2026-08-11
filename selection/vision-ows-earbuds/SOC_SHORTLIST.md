# SoC Shortlist: 视觉蓝牙耳机（OWS）

## 0. 元信息

| 字段 | 值 |
|------|-----|
| schema_version | 1 |
| product_slug | vision-ows-earbuds |
| product_family | wearable_ai |
| target_silicon_class | 音频 SoC / SiP / 低功耗主控 |
| brief_path | ./SELECTION_BRIEF.md |
| info_cutoff | 2026-08-11 |
| probe_pack | wearable_ai/ows_vision |

**Phase 2 Clarification 记录**

| 类型 | 结论 |
|------|------|
| Spec Detail Probe | 见 §1b（5 条） |
| Uncertainty | `sram_psram`：WQ7036AX 公开无具体 Mb 值；运营方选 **B**（datasheet/FAE 确认 >2 Mb）本轮放行 |
| 归属确认 | 维持下方 Shortlist / Near-Miss |

## 1. 筛选摘要

- Hard Constraint 条数：7（Brief）+ 3（`grade=hard` 探针）
- Shortlist 数量：**2**
- Near-Miss 数量：**4**
- 主要不确定点：WQ7036AX SRAM 精确值依赖 FAE/手册（非双源公开）；OWS 耳塞同时容纳 SoC+外挂 ISP+相机的量产拆解仍少；渠道价≠ BOM
- Phase 2 Clarification：Spec Detail×5；SRAM Uncertainty（B）；归属确认

## 1b. Spec Detail Probe 记录

| 字段 | 值 |
|------|-----|
| probe_pack | `wearable_ai/ows_vision` |

| probe_id | answer | grade | 影响 |
|----------|--------|-------|------|
| isp_topology | external_ok | hard | 外挂 ISP 可满足 `sense_vision` / `camera_isp` |
| package_pin | mid_ok | soft | 常见可穿戴 BGA 可留；过大封装降 Match Band |
| sram_psram | >2 Mb（megabit） | hard | 公开无法证实 >2 Mb → Near-Miss；WQ7036 本轮 FAE 确认例外 |
| wireless_extra | bt_only | soft | 不强制 Wi‑Fi；带 Wi‑Fi 选项不加分 |
| cam_iface | any_working_path | hard | 主控+外挂 ISP 可工作路径即可，不锁死 MIPI/DVP/SPI |

跳过（Brief 已覆盖或不分叉）：`bt_integration`（Brief Hard）、`audio_iface`（暂无外设表冲突）。

## 2. Hard Constraints 应用表

| id | Spec 摘要 | 结果策略 |
|----|-----------|----------|
| sub_form | ows_vision_earbuds | 耳侧/开放式音频主控品类 |
| audio_chain | mainstream ≥2 mic + 编解码/DSP | 官方/量产能力 |
| wireless | mainstream BT | BT 5.3+ 双模等 |
| sense_vision | 单路静帧路径 | + `isp_topology`/`cam_iface` |
| fw_stack | vendor SDK | 厂商固件平台 |
| camera_isp | ~2–5MP 基础 ISP 静帧 | 外挂 ISP 可（probe） |
| bt_integration | 主控内置 BT 单芯片 | 排除 BT 分芯强制双芯 |
| probe:isp_topology | external_ok | hard |
| probe:sram_psram | >2 Mb | hard |
| probe:cam_iface | any_working_path | hard |

## 3. SoC Shortlist

### 高匹配

#### 物奇 WUQI WQ7036AX

| 字段 | 值 |
|------|-----|
| part | WQ7036AX |
| vendor | WUQI Microelectronics（物奇） |
| silicon_class | audio_soc |
| match_band | high |

**Hard / grade=hard 探针判定**

| id | verdict | 证据 |
|----|---------|------|
| sub_form | pass | [A] 高级 TWS/低功耗音频（信息时效：2023-08，https://www.wuqi-micro.com/Public/Uploads/uploadfile2/files/20230830/WQ7036EN.pdf）；[A] 华为 FreeClip OWS 采用（信息时效：2024，https://www.52audio.com/archives/189999.html） |
| audio_chain | pass | [A] HiFi5 DSP/NPU、多麦降噪、Hybrid ANC（PDF 2023-08）；[A] 量产通话/音效方案（52audio） |
| wireless | pass | [A] BT/BLE 5.3、LE Audio/LC3（PDF）；[B] 终端 BT 5.4 宣传 |
| sense_vision | pass | [A] Looktech：WQ7036AX+SSC309QL+相机（https://www.52audio.com/archives/258897.html）；[A] 官方「音频 SoC+独立 ISP」（https://www.wuqi-micro.com/about-wuqi/news-and-events/newss/85，2026-07） |
| camera_isp | pass | 同上 + probe `isp_topology=external_ok` |
| fw_stack | pass | [A] software platform / Open DSP；[B] 多品牌量产 |
| bt_integration | pass | [A] 单芯片蓝牙音频 SoC；影像外挂符合探针 |
| probe:isp_topology | pass | Clarification / Probe：external_ok |
| probe:cam_iface | pass | any_working_path + 拆解可工作路径 |
| probe:sram_psram | pass\* | 公开仅「更大 SRAM」；\*本轮运营方 **FAE/datasheet 确认 >2 Mb**（非双源公开数值） |

**Soft / grade=soft 探针判定**

| id | verdict | 说明 |
|----|---------|------|
| power_battery | met | 低功耗叙事 ↔ short Soft |
| package_size / package_pin | met | OWS/镜腿量产；mid_ok |
| on_device_ai | met | 无强制 NPU |
| cost_band | partial | 渠道价样本≠ BOM |
| supply_life | met | 多品牌、官方出货叙事 |
| storage_bw | met | 轻量拍传 |
| thermal_wear | partial | 双芯片峰值热取决于结构 |
| wireless_extra | met | BT-only 路径清晰，不依赖 Wi‑Fi |

**Uncertainty**

- SRAM 精确 Mb 未公开双源；依赖本轮 FAE 确认
- OWS 耳塞级「SoC+ISP+相机」同腔拆解样本少

**来源**

| URL | grade | dated |
|-----|-------|-------|
| https://www.wuqi-micro.com/Public/Uploads/uploadfile2/files/20230830/WQ7036EN.pdf | A | 2023-08 |
| https://www.wuqi-micro.com/about-wuqi/news-and-events/newss/85 | A | 2026-07 |
| https://www.52audio.com/archives/258897.html | A | 2024-12 |
| https://www.52audio.com/archives/189999.html | A | 2024 |
| 运营方 FAE/datasheet（SRAM >2 Mb） | 运营确认 | 2026-08-11 |

对比说明：最贴 OWS + 听歌 + 外挂 ISP 拍传；SRAM Hard 依赖确认条款。

### 中匹配

#### 恒玄 Bestechnic BES2800HP

| 字段 | 值 |
|------|-----|
| part | BES2800HP |
| vendor | Bestechnic（恒玄） |
| silicon_class | audio_soc |
| match_band | mid |

**Hard / grade=hard 探针判定**

| id | verdict | 证据 |
|----|---------|------|
| sub_form | pass | [A] TWS / **open-type** headphones / smart glasses（https://www.bestechnic.com/Uploads/keditor/file/20241011/20241011104844_98351.pdf，2024-10） |
| audio_chain | pass | [A] 2×DAC / 4×ADC、ANC；[B] 高端可穿戴导入 |
| wireless | pass | [A] Dual-mode BT 5.4 + LE Audio；Wi‑Fi 6 optional |
| sense_vision / camera_isp | pass | [B] 行业「BES2800+外挂 ISP」（如 https://m.elecfans.com/article/6900196.html）；+ probes |
| fw_stack | pass | [A] 厂商可穿戴/音频平台 |
| bt_integration | pass | [A] 片上双模 BT |
| probe:isp_topology | pass | external_ok |
| probe:cam_iface | pass | 外挂 ISP 路径（媒体双源级 [B]+[B]） |
| probe:sram_psram | pass | [A] Shared **8.3 MB** SRAM（官方 Brief）≫ 2 Mb |

**Soft / grade=soft 探针判定**

| id | verdict | 说明 |
|----|---------|------|
| power_battery | partial | 能力更强、可选 Wi‑Fi，短续航余量更紧 |
| package_size / package_pin | partial | [A] 220-pin BGA；mid_ok 下可留但不如紧凑方案 |
| on_device_ai | met | Soft 不强制 NPU |
| cost_band | partial | 旗舰档位，中端 BOM 未证实 |
| supply_life | met | 6nm 平台广泛导入 |
| storage_bw | met | 轻量拍传足够 |
| thermal_wear | partial | Soft 允许短暂温升；Wi‑Fi+ISP 更敏感 |
| wireless_extra | partial | 满足 BT；可选 Wi‑Fi 对 bt_only Soft 无加成 |

**Uncertainty**

- 部分媒体将 Looktech 误写为 BES2800；拆解实为 WQ7036AX，不以该条为 BES 视觉证据
- OWS 耳塞结构验证不足

**来源**

| URL | grade | dated |
|-----|-------|-------|
| https://www.bestechnic.com/Uploads/keditor/file/20241011/20241011104844_98351.pdf | A | 2024-10 |
| https://m.elecfans.com/article/6900196.html | B | 2025 |
| https://daguoai.com/2516.html | B | 2025–2026 |

对比说明：内存与开放式定位过 Hard 很干净；封装与功耗 Soft 弱于 WQ7036AX → 中匹配。

## 4. Near-Miss（非 Shortlist 成员）

| 型号 | 违反的 Hard Constraint | 建议回谈放宽？ | 证据 |
|------|------------------------|----------------|------|
| Qualcomm Snapdragon AR1 | Target Silicon Class / 常双芯 `bt_integration` | 仅当改 Family/允许 AP | [A] AR1 Brief；[B] AR1+BES 方案报道 |
| Qualcomm QCC5181 / S5·S7 | `sense_vision` / `camera_isp` / `cam_iface` | 与拍照冲突则否 | [A] Sound Platform 音频 Brief，无相机 ISP 路径双源 |
| Bestechnic BES6100 | 量产/可交付 Critical Claim 不足 | 跟踪量产后重跑 | [B] 送样/2027 量产口径 |
| Nordic nRF52840 | `audio_chain` | 否（研究原型） | [A/B] VueBuds：BLE+低分辨率传感，非主流听歌双麦 SoC |

## 5. 空清单处理

不适用。

## 6. 证据附录

- 分级：A > B > C；Critical Claim 尽量双源
- `sram_psram`：BES2800 有 [A] 数值；WQ7036 本轮为**运营方 FAE/datasheet 确认**，已在 Uncertainty 中明示
- Freshness：>48 月 [A] 降 [B]；WQ7036 PDF 2023-08 仍 <48 月
- 信息截止：2026-08-11
- 本文件相对旧版：纳入形态门控 Spec Detail Probe，并重筛归属
