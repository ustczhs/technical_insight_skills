# soc-selection（选型簇）

主控 / SoC 选型能力簇：产品端 Brief 与技术端 Shortlist 在**本簇内**硬衔接。  
本簇**不是**单一 Cursor skill——安装时分别链接两个叶子目录。

| Skill | 角色 | 目录 |
|-------|------|------|
| `hardware-selection-brief` | Phase 1：产品概念 → Selection Brief | [hardware-selection-brief/](./hardware-selection-brief/) |
| `soc-shortlist` | Phase 2：Brief Ready → SoC Shortlist | [soc-shortlist/](./soc-shortlist/) |

## 簇内资源

| 路径 | 用途 |
|------|------|
| [CONTEXT.md](./CONTEXT.md) | 本簇领域术语权威 |
| [shared/](./shared/) | Brief/Shortlist 模板、Dimension Profile、证据规则、Spec Detail Probe |

本地可自建 `examples/` 对照格式（已 gitignore，**勿提交**具体产品 Brief/Shortlist）。叶子 skill 经相对路径读取本簇 `shared/` 与 `CONTEXT.md`；若 symlink 后读不到，见根 [README.md](../../README.md) 的 realpath 提示。

## 运行时产出

```
selection/<slug>/SELECTION_BRIEF.md
selection/<slug>/SOC_SHORTLIST.md
```

## 簇内衔接

1. `/hardware-selection-brief` → `brief_status` = `brief_ready`
2. `/soc-shortlist` 加载同一 Brief → 导出 Shortlist（+ 必要时 Near-Miss）

术语：[CONTEXT.md](./CONTEXT.md)  
包公约：[../../CONTEXT.md](../../CONTEXT.md)  
包总览：[../../README.md](../../README.md)
