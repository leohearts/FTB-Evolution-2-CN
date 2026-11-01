---
navigation:
  title: 板条箱与蚀刻
  icon: nautec:rusty_crate
  position: 6
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:etching_acid_bucket
  - nautec:crate
  - nautec:rusty_crate
---

# <Color id="light_purple">板条箱与蚀刻</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="rusty_crate" scale="2"/>
  像打开箱子一样打开板条箱, 生锈的板条箱需要先在蚀刻酸中清洗.
</Column>

***

<Row>
  <ItemImage id="crate"/>
  ### <Color id="aqua">板条箱</Color>
</Row>

一种有 27 个槽位的容器, 可在晶洞以及原版沉船和废墟的战利品中找到. 右键点击即可像箱子一样打开. 漏斗也可以从中取出或放入物品.

破坏板条箱会掉落板条箱本身, 内容物仍留在其中, 无论是否打开过, 因此你可以先把找到的箱子带回家再打开.

***

<Row>
  <ItemImage id="rusty_crate"/>
  ### <Color id="aqua">生锈的板条箱</Color>
</Row>

一种锈死无法打开的板条箱, 可在废墟中找到. 在你蚀刻它之前, 它无法打开, 漏斗也无法取出其中的内容物: 把它丢入蚀刻酸, 它就会变成普通板条箱, 战利品保持不变. 其提示框和你尝试打开时收到的消息都说明了这一点, JEI 会在物品蚀刻分类下显示该转换.

生锈的板条箱装有比普通板条箱更好的打捞物. 破坏它即可搬运; 它会像板条箱一样保留战利品.

***

## <Color id="gold">蚀刻</Color>

将物品丢入蚀刻酸, 它会在配方时间(8 到 10 秒)后被清洗完成. 整组丢入的物品会一次性全部转换.

| 输入 | 输出 | 时间 |
|---|---|---|
| 生锈的板条箱 | 板条箱, 保留战利品 | 10 s |
| <ItemLink id="rusty_gear"/> | <ItemLink id="gear"/> | 8 s |
| <ItemLink id="ancient_valve"/> | <ItemLink id="valve"/> | 10 s |

JEI 会在物品蚀刻分类下列出这些配方.

每三次蚀刻会有一次消耗掉物品所在的蚀刻酸源方块. 流动的酸永远不会被消耗, 酸池下方的方块也不会. 一个一格深的坑中放一个酸源就足够了, 只要留一桶备用以便重新填充.

***

<Row>
  <ItemImage id="etching_acid_bucket"/>
  ### <Color id="aqua">蚀刻酸</Color>
</Row>

<RecipeFor id="etching_acid_bucket"/>

拥有[搅拌机](nautec:laser_chemistry/mixer.md)后, 就可以用它从盐水中制取. 蚀刻酸很黏稠: 你会陷进去并缓慢涉水, 生物会绕开它. [深海压力锻炉](nautec:deep_engineering/pressure_forge.md)也以它为燃料运行.
