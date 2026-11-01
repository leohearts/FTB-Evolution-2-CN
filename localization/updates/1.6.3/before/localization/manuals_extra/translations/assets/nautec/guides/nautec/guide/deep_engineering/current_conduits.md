---
navigation:
  title: 水流导管
  icon: nautec:current_conduit
  position: 12
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:current_conduit
  - nautec:aquarine_copper_ingot
  - nautec:aquarine_copper_compound
  - nautec:clay_gasket
  - nautec:eddy_upgrade
  - nautec:surge_upgrade
  - nautec:riptide_upgrade
  - nautec:maelstrom_upgrade
  - nautec:filter
  - nautec:intricate_filter
---

# <Color id="aqua">水流导管</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="current_conduit" scale="2"/>
  一种用于物品, 流体和 FE 的管道. 普通导管自身没有任何作用; 移动由导管接口完成.
</Column>

一排<ItemLink id="current_conduit"/>会将它连接到的每个导管接口并入同一个网络. 接口之间直接移动资源, 因此没有任何东西在管道内传输, 接口之间的导管也永远不需要加载其区块. 如果线路的一部分位于未加载的区块中, 网络就会在该处停止, 直到该区块再次加载.

导管可在水下工作, 并且可以含水.

***

## <Color id="gold">制作导管接口</Color>

1. 将导管铺在你想要连接的方块旁边.
2. 潜行使用<ItemLink id="aquarine_steel_wrench"/>点击接触这些方块的导管. 它会变成导管接口.
3. 一个接口会同时连接它接触到的每个方块, 最多五台机器外加导管线路.

潜行使用扳手点击接口, 可将其变回普通导管. 你会取回升级和过滤器. 破坏接口会掉落导管及其内部的所有东西.

不潜行使用扳手会关闭或重新开启某一侧. 在导管上, 这会阻止它与旁边的方块连接, 这样两条线路就可以并排铺设而不合并. 在接口上, 这会关闭该面.

***

## <Color id="gold">面</Color>

空手右键点击接口可打开它. 在左侧选择一个面, 然后在设置页面中设置每种资源:

* **插入:** 网络将此资源放入方块.
* **抽取:** 网络从方块中取出此资源. 发电机和漏斗也可以推入抽取面.
* **抽取与插入:** 取出也存入, 但绝不会将某物送回其来源方块.
* **关闭:** 此面忽略该资源.

新接口的每个面初始都设为插入, 因此请将来源面设为抽取.

接口接触的每个方块上的连接器会显示该面的设置: 仅插入时为橙色, 仅抽取时为蓝色, 两者都做时为紫色, 两者都不做时为普通铜色. 只有方块能容纳的资源才算数, 因此箱子的连接器会忽略能量设置.

**优先级**范围为 -99 到 99. 优先级更高的目标会先被填充. **分配**决定同优先级目标之间的行为: 轮询会依次轮流, 最近优先会填充最近的目标, 随机会在每次移动时选择不同的起点. **红石**可使某个面仅在接口通电时运行, 或仅在未通电时运行.

<ItemLink id="configuration_card"/>会将一个接口的每个面连同其升级和过滤器复制到另一个接口. 粘贴时会从你的物品栏中取走升级和过滤器, 并返还目标接口原本持有的那些.

***

## <Color id="gold">速度</Color>

每个面独立移动. 在接口中放入一个升级可提高其所有面的速度:

| 升级 | 物品 | 流体 | FE |
| --- | --- | --- | --- |
| 无 | 每 20 tick 8 个 | 1,000 mB/t | 5,000/t |
| <ItemLink id="eddy_upgrade"/> | 每 10 tick 16 个 | 5,000 mB/t | 25,000/t |
| <ItemLink id="surge_upgrade"/> | 每 5 tick 32 个 | 30,000 mB/t | 150,000/t |
| <ItemLink id="riptide_upgrade"/> | 每 2 tick 64 个 | 200,000 mB/t | 1,000,000/t |
| <ItemLink id="maelstrom_upgrade"/> | 每 tick 256 个 | 1,000,000 mB/t | 5,000,000/t |

***

## <Color id="gold">过滤器</Color>

在接口中放入<ItemLink id="filter"/>, 即可为每个面开放过滤: 过滤页面中有 9 个物品槽和 9 个流体槽. <ItemLink id="intricate_filter"/>可开放全部 27 个物品槽.

* 手持物品, 桶或储罐点击某个槽位, 或从 JEI 拖入. 右键点击可清除.
* Shift+点击某个物品槽, 可使其精确匹配组件, 例如附魔书或装有菌落的培养皿. 这些槽位会用金色角标标记.
* 装有菌落的培养皿初始会匹配其菌株, 不限菌落规模. Shift+点击它可改为匹配任意培养皿. 设为精确匹配的空培养皿只接受空培养皿.
* **白名单**只允许列出的事物通过该面, **黑名单**则会阻挡它们. 未设置过滤的面允许所有事物通过.

过滤双向生效: 它们既限制抽取面送出什么, 也限制插入面接受什么.

***

## <Color id="gold">材料</Color>

用纯度 2.1 或更高的激光束照射掉落的<ItemLink id="aquarine_copper_compound"/>, 可将每份转化为 4 个<ItemLink id="aquarine_copper_ingot"/>. 该混合物由铜, 海晶水晶和干海带合成, 或在<ItemLink id="mixer"/>中用 3 个铜锭, 1 份<ItemLink id="kelp_slurry"/>和 500 mB 盐水批量制作, 可产出 6 份.

<RecipeFor id="aquarine_copper_compound"/>
<RecipeFor id="clay_gasket"/>
<RecipeFor id="current_conduit"/>
<RecipeFor id="eddy_upgrade"/>
<RecipeFor id="filter"/>
