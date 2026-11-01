---
navigation:
  title: 更强的光束
  icon: nautec:focusing_lens
  position: 2
  parent: getting_started/getting_started-index.md
---

# <Color id="light_purple">更强的光束</Color>

每台需要激光束的 海蓝科技 机器都有一个最低值: 它在开始运行前必须接收的每 tick AP. 比该最低值更强的光束绝不会浪费. 大多数机器会因此运行得更快, 深海排水口则会泵送更多.

***

## <Color id="gold">规则</Color>

**速度 = (光束 ÷ 机器所需值)的平方根.**

四倍的功率会让机器以两倍速度运行. 九倍则快三倍. 没有上限, 但每一步额外提升所消耗的功率都比上一步更多.

| 光束, 以机器所需值的倍数表示 | 速度 |
|---|---|
| 低于 1× | 不运行 |
| 1× | ×1(正常) |
| 2× | ×1.41 |
| 4× | ×2 |
| 9× | ×3 |
| 16× | ×4 |
| 25× | ×5 |
| 100× | ×10 |

一台需要 10 AP 的机器接收 40 AP 的光束时以 ×2 运行. 同一台机器接收 90 AP 时以 ×3 运行.

纯度不会加快任何东西. 需要最低纯度的机器(高级细菌分析机, 菌落复制机和移植站)在低于该纯度时仍会停止, 无论到达多少功率.

***

## <Color id="gold">哪些机器</Color>

| 机器 | 需要(默认) | 更强的光束加快什么 |
|---|---|---|
| [搅拌机](nautec:laser_chemistry/mixer.md) | 10 AP | 增加每周期加工次数, 每 10 AP 加工一次, 最多 64 次; 超过 640 AP 后缩短周期 |
| [诱变机](nautec:aquatic_biology/mutator.md) | 10 AP | 变异尝试, 因此每分钟尝试次数更多 |
| [培养机](nautec:aquatic_biology/incubator.md) | 20 AP | 生长周期, 以及每个周期消耗的营养 |
| [细菌分析机](nautec:aquatic_biology/bacterial_analyzer.md) | 5 AP | 分析 |
| [高级细菌分析机](nautec:aquatic_biology/bacterial_analyzer.md) | 40 AP, 纯度 2.1 | 全部九个培养皿的分析 |
| [深海压力锻炉](nautec:deep_engineering/pressure_forge.md) | 40 AP | 锻造 |
| [菌落复制机](nautec:aquatic_biology/colony_replicator.md) | 80 AP, 纯度 2.0 | 每次复制 |
| [移植站](nautec:aquatic_biology/bacteria_grafting.md) | 100 AP, 纯度 2.8, 使用高级移植锚时 500 AP | 每次移植 |
| [生物反应机](nautec:aquatic_biology/bio_reactor.md) | 5 AP, 每个菌落再加 15, 再乘以其升级 | 产量 |
| [工业生物反应机](nautec:aquatic_biology/industrial_bio_reactor.md) | 100 AP, 每个菌落再加 50, 再乘以其升级 | 产量 |
| [强化站](nautec:laser_augmentation/augmentation_station.md) | 每个使用中的扩展单元 25 AP | 安装强化, 速度取决于最弱的扩展单元 |
| [海洋侦察艇船坞](nautec:submarine/submarine_dock.md) | 20 AP | 为停靠的潜艇充能的速度 |
| [深海排水口](nautec:laser_chemistry/drain.md) | 多于 20 AP | 每秒泵出的盐水量, 与光束成正比 |
| [渗透过滤器](nautec:laser_chemistry/osmosis_filter.md) | 无 | 每 40 AP 使产水量翻倍 |

**叠加.** 生物反应机先根据其菌落和升级算出所需值, 更强的光束随后在它们的速度升级之上加速. 升级使其以 ×1.5 运行的反应机, 若获得所需功率的四倍, 则以 ×3 运行. 更强的光束不会让菌落更快消耗营养, 因此这是纯粹的额外产量. 高级移植锚同理: 它把移植站的需求提高到 500 AP 并加快移植, 高于 500 AP 的光束会再次加速.

**不加速.** [激光提纯熔炉](nautec:deep_engineering/laser_purification_smelter.md)的运行速度取决于其导管升级, 与光束强度无关. 更纯的光束反而会降低其所需的 AP.

**已有比例关系.** [共鸣室](nautec:deep_engineering/resonance_chamber.md)按其接收的功率充能, [晶体培育座](nautec:deep_engineering/crystal_cultivation.md)按其累计接收的总功率生长, 因此两者在更强的光束下本就更快, 且成正比.

***

## <Color id="gold">查看效果</Color>

Jade 会显示这些机器中任何一台的速度, 以及它获得的光束和所需值, 例如 "速度 x2.00, 光束 40 AP(需要 10)". 过弱的光束会显示为红色. <ItemLink id="prism_monocle"/>会显示任何激光方块处到达的功率和纯度.

要获得更强的光束, 可用[激光转接器](nautec:laser_chemistry/laser_manipulation.md)合并多个源头, 或从更强的发电机为机器供能, 例如[能量转换器](nautec:laser_chemistry/energy_converter.md).

***

## <Color id="gold">供整合包作者</Color>

`config/nautec-common.toml` 中的 `beamOverclock` 可关闭加速, 这样每台机器在高于最低值时都以正常速度运行. `beamOverclockMaxSpeed` 会限制速度倍率; 0 表示不限制. 深海排水口的泵送有自己的设置, 在其页面上说明.
