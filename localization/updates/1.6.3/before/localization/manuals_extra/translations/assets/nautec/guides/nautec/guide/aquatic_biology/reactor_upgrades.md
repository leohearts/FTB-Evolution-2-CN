---
navigation:
  title: 反应机升级
  icon: nautec:reactor_speed_upgrade
  position: 11
  parent: aquatic_biology/aquatic_biology-index.md
item_ids:
  - nautec:reactor_speed_upgrade
  - nautec:reactor_yield_upgrade
  - nautec:reactor_efficiency_upgrade
  - nautec:reactor_fusion_upgrade
---

# <Color id="light_purple">反应机升级</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="reactor_speed_upgrade" scale="2"/>
  升级让反应机产出更多或消耗更少, 代价是更高的能量需求.
</Column>

[生物反应机](bio_reactor.md)有 2 个升级槽, [工业生物反应机](industrial_bio_reactor.md)有 4 个. 每个槽放一个升级, 可以自由混搭类型, 两个同类型会计算两次. 升级影响反应机中的每个菌落. 漏斗和管道也可以输入它们; 它们只会进入升级槽.

每个升级的悬停提示会按当前配置值显示其效果和能量倍率.

***

## <Color id="gold">升级</Color>

<Row>
  <ItemImage id="reactor_speed_upgrade"/>
  ### <Color id="aqua">反应机速度升级</Color>
</Row>

每个升级增加 50% 生产速度: 一个为 1.5 倍速度, 两个为 2 倍, 四个为 3 倍. 能量消耗乘以 1.6.

<Row>
  <ItemImage id="reactor_yield_upgrade"/>
  ### <Color id="aqua">反应机产量升级</Color>
</Row>

每个完成的循环额外产出一个物品: 一个升级每循环 2 个, 两个 3 个, 四个 5 个. 能量消耗乘以 1.8. 菌落的输出槽必须能容纳整批物品, 循环才能完成.

<Row>
  <ItemImage id="reactor_efficiency_upgrade"/>
  ### <Color id="aqua">反应机效率升级</Color>
</Row>

每个升级让每个菌落每 tick 少消耗 25% 的[营养物缓冲](colony_feeding.md), 且减免会相乘: 一个剩下 75%, 两个 56%, 三个 42%, 四个 32%. 一个价值 1,200 tick 的营养物, 在一个升级下能维持 80 秒工作, 两个 107 秒, 四个 190 秒. 它永远不会低于 25% 的下限(可配置), 而在默认值下四个升级也达不到该下限. 能量消耗乘以 1.2. 它不会改变物品产出的速度.

速度升级和产量升级都会降低每件物品消耗的营养物, 因为营养物是按工作 tick 消耗, 而不是按物品. 就每 AP 的产出来说, 产量升级(1.8 倍能量换两倍物品)胜过速度升级(1.6 倍能量换 1.5 倍物品).

<Row>
  <ItemImage id="reactor_fusion_upgrade"/>
  ### <Color id="aqua">反应机融合升级</Color>
</Row>

由另外三种升级各一个制成. 它相当于一个速度升级, 一个产量升级和一个效率升级, 全部占用一个槽, 并且可以与它们以及其他融合升级叠加. 能量消耗乘以 2.5, 低于三个独立升级合在一起所需的 3.46.

它适用于升级槽已经装满的反应机. 工业生物反应机中的四个融合升级提供 3 倍速度, 每循环 5 个物品和 32% 的营养物消耗, 能量约为基础值的 39 倍.

***

## <Color id="gold">能量计算</Color>

所需 AP = (基础值 + 每菌落值 x 已占用菌落槽数) x 每个速度升级 1.6 x 每个产量升级 1.8 x 每个效率升级 1.2 x 每个融合升级 2.5, 向上取整

每个升级都会再次乘以整个总量, 因此消耗增长得很快. 基础值和每菌落值见[生产速率](production_rates.md)页面.

有 3 个菌落的生物反应机:

| 升级 | 所需 AP |
|---|---|
| 无 | 50 |
| 1 速度 | 80 |
| 2 速度 | 128 |
| 1 产量 | 90 |
| 2 产量 | 162 |
| 1 速度, 1 产量 | 144 |
| 1 产量, 1 效率 | 108 |
| 2 效率 | 72 |
| 1 融合 | 125 |
| 1 融合, 1 产量 | 225 |
| 2 融合 | 313 |

有 9 个菌落的工业生物反应机:

| 升级 | 所需 AP |
|---|---|
| 无 | 550 |
| 4 效率 | 1,141 |
| 2 产量, 2 效率 | 2,567 |
| 4 速度 | 3,605 |
| 2 速度, 2 产量 | 4,562 |
| 4 产量 | 5,774 |
| 1 融合 | 1,375 |
| 2 融合 | 3,438 |
| 2 融合, 2 产量 | 11,138 |
| 4 融合 | 21,485 |

本页的每个加成和倍率均可配置.

***

## <Color id="gold">配方</Color>

材料见[深海材料](nautec:deep_engineering/materials.md)页面.

***

## <Color id="gold">更强的光束</Color>

比反应机需求更强的光束会在速度升级之外进一步加快它, 两者相乘. 每个提高能量消耗的升级也会提高反应机开始加速所需的光束, 因此光束速度始终是相对于升级后的反应机来衡量的.

规则及其适用的每台机器参见[更强的光束](nautec:getting_started/stronger_beams.md).

<RecipeFor id="reactor_speed_upgrade"/>

<RecipeFor id="reactor_yield_upgrade"/>

<RecipeFor id="reactor_efficiency_upgrade"/>

<RecipeFor id="reactor_fusion_upgrade"/>
