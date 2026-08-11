# Selection Brief: 视觉蓝牙耳机（OWS）

## 0. 元信息

| 字段 | 值 |
|------|-----|
| schema_version | 1 |
| brief_status | brief_ready |
| product_name | 视觉蓝牙耳机（OWS） |
| product_slug | vision-ows-earbuds |
| product_family | wearable_ai |
| target_silicon_class | 音频 SoC / SiP / 低功耗主控 |
| created | 2026-08-11 |
| updated | 2026-08-11 |

## 1. 产品概念（选型所需最小描述）

面向消费者的开放式（OWS）视觉蓝牙耳机。核心用途是日常听音乐，并能拍照后做识别（识别主要在手机/云端完成）。形态为消费类智能硬件，非专业影像或强端侧 AI 设备。选型深度以音频主控 + 轻量相机接口与上传链路为限。

## 2. Product Family

| 项 | 内容 |
|------|------|
| 选定 | wearable_ai |
| 推断理由 | 视觉蓝牙耳机属 Wearable AI；Target Silicon Class 为音频 SoC/SiP/低功耗主控，与听歌 + 轻量拍照识别匹配 |
| 产品确认 | 是 |

## 3. Target Silicon Class

本族默认：**音频 SoC / SiP / 低功耗主控**（非经典 AP，除非产品明确要应用处理器）。本 Brief 确认固件/厂商 SDK 与单芯片内置 BT，不覆盖应用处理器路线。

## 4. Dimensions

### 4.1 维度总表

| id | phase | Product Framing（摘要） | Dimension Answer | Spec Field（摘要） | Framing–Spec Mapping | grade | 推荐等级 | 已确认 |
|----|-------|-------------------------|------------------|--------------------|----------------------|-------|----------|--------|
| sub_form | core | 开放式 OWS 视觉蓝牙耳机 | option:`ows_vision` 开放式 OWS 视觉蓝牙耳机 | 形态标签：ows_vision_earbuds；触发视觉/开放式 Extension | 「OWS 视觉耳机」↔ form=ows_vision_earbuds | hard | soft | 是 |
| power_battery | core | 短续航可接受，重依赖充电盒 | option:`short` 单耳约 2–3h 听歌 | 功耗/续航带：short；always-on 预算偏低 | 「2–3h + 重依赖盒」↔ battery_band=short | soft | hard | 是 |
| package_size | core | 中等腔体，可略鼓换算力/接口 | option:`mid` 中等体积/重量 | 封装/SiP 尺寸档：mid | 「可略鼓」↔ package_band=mid | soft | hard | 是 |
| audio_chain | core | 双麦通话降噪 + 完整听歌编解码 | option:`mainstream` 主流双麦+编解码 | 音频前端≥2 mic；通话 ENC；标准 BT 音频编解码/DSP | 「主流双麦听歌通话」↔ audio_tier=mainstream | hard | hard | 是 |
| wireless | core | 较新 BT 音频、低延迟、双设备友好 | option:`mainstream_bt` 主流较新 BT 体验 | BT 音频协议档：mainstream（低延迟听感、多点/双设备友好）；功耗敏感 | 「主流较新 BT」↔ bt_tier=mainstream | hard | hard | 是 |
| on_device_ai | core | 几乎无端侧 AI，识别在手机/云 | option:`none_light` 几乎无端侧 AI | 无强制 NPU；不要求本地视觉推理加速器 | 「云/手机识别」↔ on_device_ai=none | soft | soft | 是 |
| sense_vision | core | 单摄像头拍照档，拍清日常即可 | option:`single_cam_photo` 单摄拍照 | 至少 1× camera 接口；支持静帧采集 | 「单摄拍照」↔ vision=single_camera_still | hard | hard | 是 |
| fw_stack | core | 纯固件 / 厂商 SDK | option:`bare_sdk` 纯固件/厂商 SDK | 固件栈：vendor SDK / bare-metal 或等价；非 Linux AP | 「厂商 SDK」↔ fw_stack=vendor_sdk | hard | hard | 是 |
| cost_band | core | 中端消费主控价位 | option:`mid` 中端消费 | 主控成本带：mid | 「中端消费」↔ cost_band=mid | soft | soft | 是 |
| supply_life | core | 稳定供货 + 完整耳机 SDK | option:`mainstream_supply` 主流稳定供货与 SDK | 可获得性：有量产耳机 SDK 的主流供货路径 | 「稳定供货+SDK」↔ supply=mainstream_sdk | soft | soft | 是 |
| camera_isp | extension | 约 2–5MP、基础 ISP 静帧 | option:`basic_still` 2–5MP 基础 ISP | 相机约 2–5MP；基础 ISP 或可出可识别 JPEG/YUV 静帧 | 「够用静帧」↔ camera=2to5mp_basic_isp | hard | hard | 是 |
| storage_bw | extension | 轻量拍一张即传，少量缓冲 | option:`light_buffer` 轻量缓冲上传 | 少量本地缓冲即可；无需大容量本地相册带宽 | 「拍一张即传」↔ storage_bw=light | soft | soft | 是 |
| thermal_wear | extension | 连拍/上传允许短暂温升 | option:`brief_warmup` 可接受短暂温升 | 热设计偏好：允许短时峰值温升；非极致冷贴耳 | 「短暂温升可接受」↔ thermal=brief_warmup_ok | soft | soft | 是 |
| ows_amp | extension | 漏音/驱动不写入 SoC 规格 | unconstrained | — | 产品明确无 SoC 侧要求 | unconstrained | soft | 是 |
| bt_integration | extension | 音频主控内置 BT 单芯片 | option:`bt_in_soc` 主控内置 BT | 单芯片音频 SoC/SiP 含 BT；排除强制双芯架构 | 「单芯片内置 BT」↔ bt_integration=on_soc | hard | hard | 是 |

### 4.2 维度备注

#### sub_form

- 提供过的选项：入耳/半入耳 / OWS 视觉 / AI 眼镜 / 其他
- 等级：产品升为 Hard（量产形态锁定 OWS 视觉耳机）

#### power_battery

- 提供过的选项：short 2–3h / mid 4–6h / long ≥8h
- 等级：产品定为 Soft（短续航可接受，作偏好而非硬门槛）

#### package_size

- 提供过的选项：极致轻薄 / 中等 / 宽松
- 等级：Soft（可用体积换接口）

#### on_device_ai

- 识别链路：耳机拍照 → 手机/云识别；不强制 NPU

#### ows_amp

- 开放式漏音与声学结构不进入主控 Hard/Soft 筛选

#### bt_integration

- 与 `wireless`、`fw_stack` 一致：厂商 SDK 单芯片路线

## 5. Hard Constraints（汇总）

- `sub_form`：形态 = 开放式 OWS 视觉蓝牙耳机（ows_vision_earbuds）
- `audio_chain`：音频档 = mainstream（≥2 mic 通话降噪 + 标准听歌编解码/DSP）
- `wireless`：BT 档 = mainstream（较新 BT 音频体验、低延迟、双设备友好）
- `sense_vision`：至少单路相机静帧采集能力
- `fw_stack`：vendor SDK / 纯固件（非 Linux AP 路线）
- `camera_isp`：约 2–5MP 级 + 基础 ISP/可识别静帧输出
- `bt_integration`：主控内置 BT 的单芯片 SoC/SiP

## 6. Soft Preferences（汇总）

- `power_battery`：续航带 short（约 2–3h 听歌、重依赖充电盒）
- `package_size`：封装尺寸档 mid
- `on_device_ai`：无强制端侧 AI / NPU
- `cost_band`：主控成本 mid
- `supply_life`：主流稳定供货 + 完整耳机 SDK
- `storage_bw`：轻量缓冲、拍传即可
- `thermal_wear`：允许短时温升（brief_warmup_ok）

## 7. Unconstrained

- `ows_amp`

## 8. Brief Ready 检查

- [x] Product Family 已确认（或 Out-of-Family 已明示）
- [x] Profile 内全部 Core 均有 Dimension Answer
- [x] 已纳入的 Extension 均有 Dimension Answer
- [x] 每项等级已在 Dimension Turn 中确认
- [x] Framing–Spec Mapping 均已写明

`brief_status` = **brief_ready**
