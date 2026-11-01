---
navigation:
  title: 深海材料
  icon: nautec:flawless_prismarine_crystal
  position: 4
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:resonant_shard
  - nautec:flawless_prismarine_crystal
  - nautec:deep_steel_plating
---

# <Color id="light_purple">深海材料</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="flawless_prismarine_crystal" scale="2"/>
  由共鸣室和深海压力锻炉制造的三种合成材料.
</Column>

它们各自只来自一个机器配方. JEI 会显示这些配方及其纯度和深度要求.

***

<Row>
  <ItemImage id="resonant_shard"/>
  ### <Color id="aqua">共鸣碎片</Color>
</Row>

在[共鸣室](resonance_chamber.md)中由<ItemLink id="prismarine_crystal_shard"/>在纯度 3.0 或更高的光束下制成. 一份碎片进, 一份共鸣碎片出.

用于[传送门](gateway.md), [深海压力锻炉](pressure_forge.md), [海王三叉戟](neptunes_trident.md), [聚变电站](fusion_plant.md)的激光注入器, 休眠晶种和[共鸣网络](resonance_network.md)方块, 并可压制成无瑕海棱水晶.

***

<Row>
  <ItemImage id="flawless_prismarine_crystal"/>
  ### <Color id="aqua">无瑕海棱水晶</Color>
</Row>

在[深海压力锻炉](pressure_forge.md)中由共鸣碎片制成. 需要纯度 2.0, 锻炉位于 Y -20 或更低, 每颗晶体耗时 10 秒.

用于[亚特兰蒂斯步枪](atlantean_rifle.md), [海王三叉戟](neptunes_trident.md), [传送门](gateway.md), 聚变控制器, 晶体培育座, 休眠晶种和压力合成器.

***

<Row>
  <ItemImage id="deep_steel_plating"/>
  ### <Color id="aqua">深海钢镀板</Color>
</Row>

在[深海压力锻炉](pressure_forge.md)中由海蓝钢锭制成. 需要纯度 2.5, 锻炉位于 Y -40 或更低, 每块镀板耗时 15 秒.

用于[亚特兰蒂斯步枪](atlantean_rifle.md), [海王三叉戟](neptunes_trident.md), [传送门](gateway.md), 大多数[聚变电站](fusion_plant.md)部件和晶体培育座.

它还能在铁砧上修复<ItemLink id="submarine"/>. 将捡起的海洋侦察艇放入左槽, 将镀板放入右槽. 每块镀板恢复 20% 的艇体, 消耗 2 级经验. 修复物品和每件恢复量分别是 `config/nautec-common.toml` 中的 `submarineRepairItem` 和 `submarineRepairPercent`.
