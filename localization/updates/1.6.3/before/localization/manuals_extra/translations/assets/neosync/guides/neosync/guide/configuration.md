---
navigation:
  title: 配置
  icon: minecraft:writable_book
  parent: index.md
  position: 8
---

# <Color id="light_purple">配置</Color>

配置文件为 `config/neosync-common.toml`.玩家最常问的选项如下:

| 键 | 默认值 | 效果 |
| --- | --- | --- |
| `enableInstantShellConstruction` | `false` | 创造模式玩家的躯壳会瞬间完成 |
| `warnPlayerInsteadOfKilling` | `false` | 拒绝采样, 而不是杀死生命值不足的玩家 |
| `fingerstickDamage` | `20` | 每次采样消耗的生命值 |
| `hardcoreFingerstickDamage` | `40` | 极限模式下每次采样消耗的生命值 |
| `shellConstructorCapacity` | `256000` | 培育一个完整躯壳所需的 FE |
| `shellConstructionSpeed` | `2.5` | 培育速度倍率 |
| `shellStorageCapacity` | `320` | 存放仓的 FE 缓冲 |
| `shellStorageConsumption` | `16` | 每刻维持躯壳存活所消耗的 FE |
| `acceptsRedstone` | `true` | 存放仓接受红石信号作为能量 |
| `maxUnpoweredLifespan` | `20` | 断电后存放仓维持躯壳存活的刻数 |
| `energyMap` | 见下文 | 跑步机上每种实体每刻产生的 FE |
| `syncPriority` | `NATURAL` | 死亡时选择躯壳的顺序 |
| `autoSyncOnDeath` | `true` | 躯壳死亡时同步到另一个躯壳 |
| `wrench` | `minecraft:stick` | 用于切换容器比较器输出的物品 |

默认的 `energyMap` 为: 鸡 2, 猪 16, 玩家 20, 狼 22, 村民 25, 苦力怕 80, 末影人 160.条目的格式为 `entity_id:energy_per_tick`, 因此 `minecraft:horse:30` 会以每刻 30 FE 添加马.

`syncPriority` 接受 `NATURAL`, `NEAREST` 或以大写书写的任意染料颜色名, 例如 `RED` 或 `LIGHT_BLUE`.关于该顺序如何使用, 参见[同步](syncing.md).
