---
navigation:
    title: 工具
    icon: epsilon_drill
    position: 30
---

# ε-系列工具

ε 系列是我们的标准工具产品线. 所有工具都无法损坏, 由<Color id="energy">能量</Color>驱动,
并且[可以升级](fundamentals/upgrade_system.md).

## 模块化挖掘工具

<ItemGrid>
<ItemIcon id="epsilon_drill" />
<ItemIcon id="epsilon_shovel" />
<ItemIcon id="epsilon_axe" />
<ItemIcon id="epsilon_hoe" />
</ItemGrid>

### 默认升级

<Row>
<UpgradeEntry id="default/epsilon_shovel" />
<UpgradeEntry id="tree_vein_mine" />
</Row>

钻头, 锹, 斧和锄属于 *模块化挖掘工具*. 切换装备模式可循环选择 5 种
基础挖掘速度:

- **关闭**: 禁止破坏方块, 包括创造模式.
- **慢速**: 3.0
- **正常**: 9.0
- **快速**: 20.0
- **超速**: 75.0

升级系统可以提高挖掘等级(上限), 并扩展工具适用的方块范围. 锹,
斧和锄适用于各自对应的材料. 钻头可开采 *镐* 和 *锹*
适用的材料, 以方便采矿.

> ε-系列锹的默认升级模块提供精准采集效果.

## 其他挖掘工具

<ItemGrid>
<ItemIcon id="epsilon_shears" />
<ItemIcon id="epsilon_wrench" />
</ItemGrid>

### 默认升级

<UpgradeEntry id="default/epsilon_wrench" />

扳手和剪刀无法调节速度, 也不能通过升级系统改变适用方块.
它们仍然支持附魔升级模块.

## 近战武器

<ItemGrid>
<ItemIcon id="epsilon_sword" />
<ItemIcon id="epsilon_axe" />
</ItemGrid>

### 默认升级

<UpgradeEntry id="default/epsilon_melee" />

剑和斧属于 *近战武器*, 与[特制系列武器](weapons/index.md)共享部分升级模块,
包括附魔模块(剃刀和抢夺)及目标过滤器.

> [装备伤害修正](fundamentals/damage_modifiers.md)系统适用于所有 ε-系列近战武器.

## 杂项工具

<ItemGrid>
<ItemIcon id="epsilon_fishing_rod" />
<ItemIcon id="epsilon_brush" />
<ItemIcon id="epsilon_lighter" />
</ItemGrid>

这些工具目前只有基础功能, 没有额外能力. 不过由于制造成本较低,
仍然建议制作.

## 兼容升级

### 所有 ε-系列工具

- **共振调谐电机**: 最高 1 级. 抑制手持工具发出的振动.
- **强化装备电池**: 最高 4 级. 1 级时能量容量乘以 4, 此后每级翻倍,
  4 级时最高 32x. 也适用于 [AL/1C 盔甲](armor.md).

### 挖掘工具

钻头, 锹, 斧, 锄, 剪刀和扳手.

- **超频采收矩阵**: 最高 5 级. 按等级提供 1, 2, 3, 5 或 7 级时运.
- **稳定采收矩阵**: 最高 1 级. 提供精准采集.
- **亚空间采掘链接**: 最高 1 级. 将破坏方块的掉落物直接送入你的物品栏.

> 两种采收矩阵互斥. 工具只能具有时运或精准采集之一, 无法同时拥有两者.

### 模块化挖掘工具

钻头, 锹, 斧和锄.

- **ε 切割器 Rev.000**: 最高 1 级. 在工具原有材料范围之外, 使其对所有
  方块都有效.

### 单种工具模块

- **纳米探矿机器**: 最高 1 级. 用于 ε 钻头. 一次最多连锁开采 64 个矿石, 每多开采一个方块
  都会额外耗能.
- **树木倾倒单元**: 最高 1 级. 用于 ε 斧. 一次最多砍伐 256 个原木及其
  周围树叶, 不额外消耗能量.
- **ε-垂钓者套装**: 最高 5 级. 用于 ε 钓鱼竿. 按安装等级提供饵钓和海之眷顾
  附魔.

### 近战武器

ε 剑和 ε 斧也属于`#ltxi:weapons`, 因此可安装武器侧模块:
战利品协议, 高效切割算法, 亚空间战斗链接, 生物识别混淆, 以及
三种开火协议. 各自用途见[武器](weapons/index.md).
