---
navigation:
  title: 深海生命
  icon: nautec:luminous_membrane
  position: 12
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:deep_kelp
  - nautec:luminescent_algae
  - nautec:glow_polyp
  - nautec:prismarine_frond
  - nautec:vent_tubeworm
  - nautec:abyssal_coral
  - nautec:silt_skipper
  - nautec:silt_skipper_bucket
  - nautec:silt_skipper_spawn_egg
  - nautec:lantern_jelly_spawn_egg
  - nautec:vent_crawler_spawn_egg
  - nautec:abyssal_maw_spawn_egg
---

# <Color id="light_purple">深海生命</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="luminous_membrane" scale="2"/>
  海蓝科技 海洋中的六种植物和四种生物.
</Column>

## <Color id="gold">植物</Color>

用剪刀采集全部六种植物; 使用任何其他工具破坏它们都不会掉落任何东西. 它们中的每一种都可以用<ItemLink id="grafting_tool"/>移植获得细菌; [细菌移植](nautec:aquatic_biology/bacteria_grafting.md)列出了具体对应关系.

| 植物 | 生物群系 | 光照 |
|---|---|---|
| <ItemLink id="deep_kelp"/> | 荧光海林 | 无 |
| <ItemLink id="luminescent_algae"/> | 荧光海林 | 9 |
| <ItemLink id="glow_polyp"/> | 荧光海林 | 7 |
| <ItemLink id="prismarine_frond"/> | 海晶礁 | 无 |
| <ItemLink id="vent_tubeworm"/> | 海底热泉 | 3 |
| <ItemLink id="abyssal_coral"/> | 深渊海沟 | 无 |

深海海带会像海带一样在水中向上生长, 最高可达 40 格(`config/nautec-common.toml` 中的 `kelpHeight`). 一整株只有最顶端的方块会掉落, 因此要剪取尖端. 荧光珊瑚虫会像发光地衣一样附着在方块的任意一面, 骨粉可以使其蔓延. 其余四种是单株的水下植物.

每个生物群系中的幸运钓鱼区也会钓出该生物群系的植物. 参见[钓鱼](fishing.md).

***

## <Color id="gold">淤泥跳鱼</Color>

<GameScene zoom="3.2" background="#333333" interactive={true}>
  <Entity id="nautec:silt_skipper"/>
</GameScene>

一种小型被动鱼类, 会以最多八条为一群, 在深渊海沟, 荧光海林和海晶礁中游动.

* 杀死它会掉落一个<ItemLink id="silt_skipper"/>物品, 可以食用.
* 手持水桶右键点击它, 可将其舀入<ItemLink id="silt_skipper_bucket"/>, 倒空桶即可将其放回.

***

## <Color id="gold">灯笼水母</Color>

<GameScene zoom="2.4" background="#333333" interactive={true}>
  <Entity id="nautec:lantern_jelly"/>
</GameScene>

一种缓慢发光的水母, 漂浮在荧光海林中. 它是被动生物, 生命值很低.

掉落 1 到 2 个<ItemLink id="luminous_membrane"/>(抢夺附魔可增加), 用于制作发光皮肤强化.

***

## <Color id="gold">热泉爬行者</Color>

<GameScene zoom="2.4" background="#333333" interactive={true}>
  <Entity id="nautec:vent_crawler"/>
</GameScene>

一种在海底热泉底部行走的带甲生物. 受伤时它会逃跑而不会反击, 能抵消一半的击退, 并且不受火焰伤害.

掉落 1 到 3 个<ItemLink id="chitin_plate"/>(抢夺附魔可增加). 四个甲壳板可制作热泉甲壳强化.

***

## <Color id="gold">深渊巨口</Color>

<GameScene zoom="1.8" background="#333333" interactive={true}>
  <Entity id="nautec:abyssal_maw"/>
</GameScene>

深渊海沟中的敌对掠食者. 它只会在 Y 40 以下的黑暗水域中生成, 最远能从 24 格外发现玩家并发动攻击, 还会在水中追赶你. 它有 24 点生命值, 每次撕咬造成 6 点伤害.

掉落一个<ItemLink id="abyssal_organ"/>(抢夺附魔可增加), 用于制作深渊之眼强化.

***

## <Color id="gold">强化</Color>

这三种生物掉落物各自可以制作一种强化: 参见[深海生物强化](nautec:laser_augmentation/deep_fauna_augments.md). 全部四种生物的刷怪蛋都可以在创造模式菜单中找到.
