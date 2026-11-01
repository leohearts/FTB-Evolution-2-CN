---
navigation:
  title: 海蓝钢与铸铁
  icon: nautec:aquarine_steel_ingot
  position: 2
  parent: laser_chemistry/laser_chemistry-index.md
item_ids:
  - nautec:aquarine_steel_compound
  - nautec:aquarine_steel_ingot
  - nautec:aquarine_steel_block
  - nautec:cast_iron_compound
  - nautec:cast_iron_ingot
  - nautec:cast_iron_nugget
  - nautec:cast_iron_rod
  - nautec:cast_iron_block
  - nautec:laser_channeling_coil
  - nautec:whisk
  - nautec:broken_whisk
  - nautec:oil_barrel
---

# <Color id="light_purple">海蓝钢与铸铁</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="aquarine_steel_ingot" scale="2"/>
  大多数 海蓝科技 机器所用的金属和零件.
</Column>

## <Color id="gold">海蓝钢</Color>

<Row>
  <ItemImage id="aquarine_steel_compound"/>
  ### <Color id="aqua">海蓝钢混合物</Color>
</Row>

可以手动合成, 也可以在[搅拌机](mixer.md)中用盐水制作, 同样的粗铁能产出更多混合物. JEI 会显示搅拌机配方.

<Recipe id="nautec:aquarine_steel_compound"/>

<Row>
  <ItemImage id="aquarine_steel_ingot"/>
  ### <Color id="aqua">海蓝钢锭</Color>
</Row>

将混合物丢入任何已供能的激光束, 5 秒后它会变成锭. 任意纯度都可以, 因此一个海蓝催化器就足够. 纯度为 2.0 或更高的光束则会在 4 秒内使每份混合物产出 2 个锭. 搭建方法参见[物品转化](nautec:getting_started/item_transformation.md).

<Row>
  <ItemImage id="aquarine_steel_block"/>
  ### <Color id="aqua">海蓝钢块</Color>
</Row>

可储存九个锭.

<RecipeFor id="aquarine_steel_block"/>

***

## <Color id="gold">铸铁</Color>

<Row>
  <ItemImage id="cast_iron_compound"/>
  ### <Color id="aqua">铸铁混合物</Color>
</Row>

<Recipe id="nautec:cast_iron_compound"/>

<Row>
  <ItemImage id="cast_iron_ingot"/>
  ### <Color id="aqua">铸铁锭</Color>
</Row>

在熔炉中熔炼混合物, 或用高炉以获得两倍速度.

<Recipe id="nautec:cast_iron_ingot_blasting"/>

海床上的旧铁也可以高炉熔炼: 一个锚可产出 11 个锭, 一个油桶可产出 5 个.

<Recipe id="nautec:cast_iron_ingot_from_oil_barrel_blasting"/>

<Row>
  <ItemImage id="cast_iron_rod"/>
  ### <Color id="aqua">铸铁棒</Color>
</Row>

用于海蓝钢工具, 钓鱼站, 深海排水口壁, 油桶和搅拌器.

<Recipe id="nautec:cast_iron_rod"/>

<Row>
  <ItemImage id="cast_iron_nugget"/>
  ### <Color id="aqua">铸铁粒</Color>
</Row>

九个粒合成一个锭, 也可反向拆分. 粒可用于修复破损的搅拌器.

<Row>
  <ItemImage id="cast_iron_block"/>
  ### <Color id="aqua">铸铁块</Color>
</Row>

可储存九个锭.

<Recipe id="nautec:cast_iron_block_from_ingots"/>

<Row>
  <ItemImage id="oil_barrel"/>
  ### <Color id="aqua">油桶</Color>
</Row>

一个铸铁桶, 最多可储存 8,000 mB 原油, 可以是 海蓝科技 的或任何其他模组的(任何位于 `c:oil` 标签中的流体). 右键点击可打开或关闭盖子; 只有盖子打开时管道才能接触原油. 可高炉熔炼为铸铁锭. 用镐开采即可拾取.

<Recipe id="nautec:oil_barrel"/>

***

## <Color id="gold">机器零件</Color>

<Row>
  <ItemImage id="laser_channeling_coil"/>
  ### <Color id="aqua">激光引导线圈</Color>
</Row>

由<ItemLink id="burnt_coil"/>经物品转化制成: 在纯度为 1.5 或更高的光束中放置 10 秒. 海蓝催化器的上限为 1.2, 因此可将催化器射入<ItemLink id="prismarine_crystal"/>并使用其射出的光束, 或让海棱水晶碎片光束直接穿过<ItemLink id="focusing_lens"/>.

该线圈用于充能器, 海晶电池, 大多数海蓝钢工具以及许多后续机器.

<Row>
  <ItemImage id="broken_whisk"/>
  ### <Color id="aqua">破损的搅拌器</Color>
</Row>

溺尸有时会掉落一个, 幸运钓鱼区可能将其作为宝藏钓上来, 海底废墟和研究前哨站的箱子中也可能出现.

<Row>
  <ItemImage id="whisk"/>
  ### <Color id="aqua">搅拌器</Color>
</Row>

[搅拌机](mixer.md)的搅拌部件. 用四个铸铁粒修复破损的搅拌器, 或用铸铁棒, 海棱水晶碎片和海蓝钢锭合成新的.

<Recipe id="nautec:whisk"/>
<Recipe id="nautec:whisk_from_cast_iron"/>
