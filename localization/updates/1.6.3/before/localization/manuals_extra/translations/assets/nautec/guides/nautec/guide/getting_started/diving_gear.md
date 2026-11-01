---
navigation:
  title: 潜水服与氧气
  icon: nautec:diving_helmet
  position: 10
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:brown_polymer
  - nautec:diving_chestplate
  - nautec:diving_helmet
  - nautec:diving_leggings
  - nautec:diving_boots
  - nautec:air_bottle
---

# <Color id="light_purple">潜水服与氧气</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="diving_helmet" scale="2"/>
  一套四件式潜水服, 最多可携带十分钟的空气.
</Column>

穿戴全部四件后, 胸甲中的空气罐会在水下让你的呼吸保持满值. 你每在水下停留一秒, 它就会消耗一秒的空气并把你的氧气条补满. 空气罐耗尽后, 你的氧气会照常消耗.

穿齐四件后, 你在水下挖掘的速度与在陆地上一样快, 即使在游泳或漂浮时也是如此: 潜水服会抵消水下减速和未站在地面上的减速.

这套潜水服的护甲值接近一整套铁甲, 可在铁砧上用铜锭修复.

***

## <Color id="gold">各部件</Color>

<Row>
  <ItemImage id="diving_helmet"/>
  ### <Color id="aqua">潜水头盔</Color>
</Row>

清除水下迷雾, 让你能看得更远. 此效果单独生效, 无需穿戴整套潜水服.

<Recipe id="nautec:diving_helmet"/>

<Row>
  <ItemImage id="diving_chestplate"/>
  ### <Color id="aqua">潜水胸甲</Color>
</Row>

内置空气罐, 最多可储存 10 分钟的空气. 新的胸甲自带满罐空气. 其提示框会显示剩余量, 在水下时空气罐会以快捷栏上方的一排气泡显示. 空气罐耗尽时, 这排气泡会全部变成空泡, 提醒你补充空气.

<Recipe id="nautec:diving_chestplate"/>

<Row>
  <ItemImage id="diving_leggings"/>
  ### <Color id="aqua">潜水护腿与靴子</Color>
</Row>

用于凑齐整套潜水服. 只有穿齐四件时空气罐才会生效.

<Recipe id="nautec:diving_leggings"/>

<Recipe id="nautec:diving_boots"/>

***

## <Color id="gold">为空气罐充气</Color>

<Row>
  <ItemImage id="air_bottle"/>
  ### <Color id="aqua">压缩空气瓶</Color>
</Row>

手持空玻璃瓶右键点击气泡柱, 即可装入压缩空气. 任何气泡柱都可以, 无论是由灵魂沙还是岩浆块形成. 晶洞中的桶里也会有几个.

要为空气罐充气, 可用八个压缩空气瓶围绕胸甲进行合成. 这会得到装满十分钟空气的空气罐, 并返还空瓶. 合成产出的胸甲是一件新物品, 因此旧胸甲上的附魔会丢失. 若想保留附魔胸甲, 请改为饮用空气瓶.

<Recipe id="nautec:diving_chestplate_oxygen"/>

你也可以在穿戴胸甲时饮用空气瓶. 只要空气罐未满, 每瓶可增加 2 分钟的空气, 最多到 10 分钟, 因此五瓶可充满空罐. 饮用还会让你向上漂浮 10 秒.

### <Color id="aqua">氧气流体</Color>

胸甲也接受其他模组的氧气流体, 例如 群星 的氧气. 将其放入任何可为物品填充流体的机器或储罐槽位. 每 mB 氧气可增加一秒空气, 因此 600 mB 可充满空罐.

***

<Row>
  <ItemImage id="brown_polymer"/>
  ### <Color id="aqua">棕色聚合物</Color>
</Row>

制作潜水服的材料. 可用干海带和棕色染料合成, 也可以在板条箱和晶洞的桶中找到. 多余的聚合物还可以合成书, 床, 旗帜和物品展示框.

<Recipe id="nautec:brown_polymer"/>

***

## <Color id="gold">安装 群星 时</Color>

如果安装了 群星, 完整的潜水服还能让你在没有空气的星球上存活. 你在不可呼吸区域每停留一秒, 空气罐就会消耗一秒空气, 气泡行也会显示在快捷栏上方. 在氧气分配器的范围内, 空气罐不会被消耗.

当你戴着装有氧气模块的 群星 航天服头盔时, 饮用压缩空气瓶会为头盔增加 120 mB 氧气, 与它为潜水空气罐提供的 2 分钟空气相同.

***

## <Color id="gold">其他呼吸方式</Color>

* 只要有能量, [海洋侦察艇](nautec:submarine/submarine.md)就能让里面所有人呼吸.
* 按住[水流喷射器](nautec:submarine/wave_jet.md)的推进键可阻止氧气条消耗.
* 完整的 群星 航天服在头盔有氧气时能让你在水下呼吸.
* 溺尸之肺强化能让你在水下时氧气始终保持满值: 参见[生物强化](nautec:laser_augmentation/mob_augments.md).
