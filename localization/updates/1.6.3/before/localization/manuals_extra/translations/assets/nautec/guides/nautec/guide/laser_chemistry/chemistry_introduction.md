---
navigation:
  title: 化学流体
  icon: nautec:eas_bucket
  position: 3
  parent: laser_chemistry/laser_chemistry-index.md
item_ids:
  - nautec:eas_bucket
  - nautec:saltwater_bucket
  - nautec:oil_bucket
  - nautec:glass_vial
  - nautec:eas_vial
  - nautec:salt
---

# <Color id="light_purple">化学流体</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="eas_bucket" scale="2"/>
  海蓝科技 机器使用和生产的流体.
</Column>

盐水是几乎所有[搅拌机](mixer.md)配方的基础. 搅拌机将盐水转化为电解藻类浆液(EAS)和蚀刻酸.

***

<Row>
  <ItemImage id="saltwater_bucket"/>
  ### <Color id="aqua">盐水</Color>
</Row>

盐水来自[深海排水口](drain.md), 它每秒向内部储罐泵入 500 mB. 用桶或管道抽取.

也可以在[搅拌机](mixer.md)中制作: 1,000 mB 普通水和一份盐可在 5 秒内产出 1,000 mB 盐水.

默认情况下, 用桶装取海水仍会得到普通水. 整合包作者可在 `config/nautec-common.toml` 中把 `collectSaltWater` 设为 true, 这样在海洋生物群系中从任意水源装桶都会得到盐水桶.

***

<Row>
  <ItemImage id="eas_bucket"/>
  ### <Color id="aqua">电解藻类浆液(EAS)</Color>
</Row>

在[搅拌机](mixer.md)中由盐水制成. EAS 可解锁[海蓝钢工具](tools.md)的能力.

要灌注工具, 请将 EAS 倒出为源方块, 并把工具丢入其中. 约 7.5 秒后工具会永久完成灌注, EAS 源方块会被消耗, 因此一桶只能灌注一件工具.

***

<Row>
  <ItemImage id="etching_acid_bucket"/>
  ### <Color id="aqua">蚀刻酸</Color>
</Row>

清除板条箱和旧零件上的锈迹. 可在[搅拌机](mixer.md)中制作, 也可通过合成获得. 参见[板条箱与物品蚀刻](nautec:getting_started/etching.md).

***

<Row>
  <ItemImage id="oil_bucket"/>
  ### <Color id="aqua">原油</Color>
</Row>

一种黏稠流体, 可在<ItemLink id="oil_barrel"/>中找到.

***

## <Color id="gold">试管与盐</Color>

<Row>
  <ItemImage id="glass_vial"/>
  ### <Color id="aqua">玻璃试管</Color>
</Row>

<Recipe id="nautec:glass_vial"/>

<Row>
  <ItemImage id="eas_vial"/>
  ### <Color id="aqua">电解藻类浆液(EAS)试管</Color>
</Row>

一个 EAS 桶和三支玻璃试管可合成三支 EAS 试管, 并返还空桶. 玻璃试管和 EAS 试管会放入<ItemLink id="syringe_robot_arm"/>.

<Recipe id="nautec:eas_vial"/>

<Row>
  <ItemImage id="salt"/>
  ### <Color id="aqua">盐</Color>
</Row>

在幸运钓鱼区可作为渔获获得. 参见[钓鱼](nautec:getting_started/fishing.md). [热泉汲取器](nautec:getting_started/ocean_generators.md)每煮沸 1,000 mB 盐水也会留下一个盐. 盐和水可在[搅拌机](mixer.md)中制成盐水.
