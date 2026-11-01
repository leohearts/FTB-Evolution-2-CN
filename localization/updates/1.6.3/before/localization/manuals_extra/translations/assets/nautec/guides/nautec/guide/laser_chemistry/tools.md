---
navigation:
  title: 海蓝钢工具
  icon: nautec:aquarine_steel_axe
  position: 8
  parent: laser_chemistry/laser_chemistry-index.md
item_ids:
  - nautec:aquarine_steel_sword
  - nautec:aquarine_steel_pickaxe
  - nautec:aquarine_steel_axe
  - nautec:aquarine_steel_shovel
  - nautec:aquarine_steel_hoe
---

# <Color id="light_purple">海蓝钢工具</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="aquarine_steel_axe" scale="2"/>
  以 AP 代替耐久度的工具, 每件都有可用 EAS 解锁的能力.
</Column>

## <Color id="gold">能量</Color>

这些工具永远不会损坏. 它们改为消耗 AP: 开采大多数方块或击中生物消耗 1 AP. 图标下方的进度条显示电量, 提示框会给出精确数值.

AP 耗尽后, 工具将无法开采, 攻击或对方块使用, 因此请在[充能器](charger.md)上或用[海晶电池](prismatic_battery.md)为其补充能量. 锄可储存 700 AP; 其他工具储存 1,200 AP.

***

## <Color id="gold">解锁能力</Color>

新工具的能力处于锁定状态. 倒出一格[电解藻类浆液](chemistry_introduction.md)源方块, 并将工具丢入其中. 约 7.5 秒后工具会永久完成灌注, EAS 会被消耗.

完成灌注后, 手持工具并潜行右键点击可开启或关闭其能力. 能力开启时工具会闪烁.

***

<Row>
  <ItemImage id="aquarine_steel_pickaxe"/>
  ### <Color id="aqua">镐</Color>
</Row>

在你破坏的面上开采 3x3 范围的石头和其他可被镐开采的方块, 每块消耗 2 AP. 它会跳过带有方块实体的方块, 例如箱子和机器.

由能力破坏的方块会像用普通工具开采一样掉落, 因此若想让时运或精准采集生效, 请关闭能力. 斧和锹也是如此.

开启能力后, 它也是采集<ItemLink id="prismarine_crystal"/>的方式: 参见[海棱水晶碎片](crystal_shards.md).

<RecipeFor id="aquarine_steel_pickaxe"/>

***

<Row>
  <ItemImage id="aquarine_steel_axe"/>
  ### <Color id="aqua">斧</Color>
</Row>

破坏一个原木会砍倒与它相连的所有原木, 每个原木消耗 2 AP, 直到整棵树倒下或斧的能量耗尽.

<RecipeFor id="aquarine_steel_axe"/>

***

<Row>
  <ItemImage id="aquarine_steel_shovel"/>
  ### <Color id="aqua">锹</Color>
</Row>

它开采的每个方块消耗 1 AP. 开启能力后, 它会在你破坏的面上挖掘 3x3 范围的泥土, 沙子, 沙砾以及其他可被锹挖掘的方块, 每个额外方块消耗 2 AP. 它会跳过带有方块实体的方块.

<RecipeFor id="aquarine_steel_shovel"/>

***

<Row>
  <ItemImage id="aquarine_steel_hoe"/>
  ### <Color id="aqua">锄</Color>
</Row>

一次使用可将 3x3 范围的泥土或草方块耕成耕地, 每块消耗 2 AP.

<RecipeFor id="aquarine_steel_hoe"/>

***

<Row>
  <ItemImage id="aquarine_steel_sword"/>
  ### <Color id="aqua">剑</Color>
</Row>

开启能力后, 只要它还有 AP, 就会造成 70% 额外伤害, 并召唤闪电击中其命中的目标. 此时每次命中消耗 10 AP.

<Color id="gold">注意</Color>: 闪电也会击中目标附近几格内的任何东西, 包括你自己, 并可能引发火灾.

<RecipeFor id="aquarine_steel_sword"/>
