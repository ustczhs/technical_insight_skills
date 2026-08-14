# Dimension Profile: Wearable AI

**Product Family**: Wearable AI（**仅问卷**）  
**推荐 primary Silicon Class**: `audio_sip`（可改；权威见 Brief 元信息与 [silicon-classes.md](../silicon-classes.md)）  
**相邻类**: 由 Hard 触发 + 产品确认；常见 `vision_soc` / `lightweight_ap`。

**厂商矩阵**：Phase 2 按 Brief 的 **Silicon Class 段 ∪ Application Domain 加扫**（见 [vendor-seeds.md](../vendor-seeds.md)），**不**再按本 Family 名选表。

## Core Dimensions

| id | Product Framing（问法要点） | Spec Field（落盘要点） | 默认推荐等级 |
|----|------------------------------|------------------------|--------------|
| `sub_form` | 耳机 / 眼镜 / 腕戴 / 其他可穿戴 | 形态标签；触发 Extension | Soft |
| `power_battery` | 续航体感档、充电盒/本机电池约束 | 功耗带、always-on 预算 | 常 Hard |
| `package_size` | 可接受体积/重量/耳塞腔体限制 | 封装尺寸/SiP 约束档 | 常 Hard |
| `audio_chain` | 麦阵路数、通话/降噪/骨传导等 | 音频前端、编解码、DSP 需求 | Hard（音频产品） |
| `wireless` | BT 版本体感、多联、功耗敏感 | BT/无线协议与功耗档 | Hard |
| `on_device_ai` | 无 / 端侧唤醒与轻推理 / 更重本地 AI | 低功耗 NPU/加速器带或无 | Soft 或 Hard |
| `sense_vision` | 无传感 / IMU / 相机视觉档 | 传感器与摄像头接口需求 | Hard（有视觉时） |
| `fw_stack` | 纯固件 / RTOS / 轻量 Linux 等 | 软件/固件栈期望 | Hard |
| `cost_band` | BOM 敏感区间 | 主控成本带 | Soft |
| `supply_life` | 寿命、品牌/供货约束 | 生命周期与可获得性 | Soft 或 Hard |

## Extension packs

| 触发 | Extension 示例 |
|------|----------------|
| 视觉蓝牙耳机 / 眼镜 | 相机分辨率与 ISP、存储带宽、散热与佩戴舒适折中 |
| 骨传导 / 开放式 | 驱动与功放是否集成、漏音相关不必写入 SoC 规格则标 Unconstrained |
| 强本地小模型 | 内存带宽、SRAM/PSRAM 需求档 |
| 需手机 App 深度协同 | 连接芯片与主控分工（主控是否含 BT） |
