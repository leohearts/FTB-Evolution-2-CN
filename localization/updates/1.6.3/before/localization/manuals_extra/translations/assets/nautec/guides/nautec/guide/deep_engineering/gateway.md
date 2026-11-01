---
navigation:
  title: 传送门
  icon: nautec:gateway
  position: 2
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:gateway
  - nautec:gateway_ring
---

# <Color id="light_purple">传送门</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="gateway" scale="2"/>
  直径 13 格的立式环. 任何穿过其视界的东西都会从另一个具有相同地址的环中出来.
</Column>

开口宽 9 格, 因此<ItemLink id="submarine"/>通过时每侧还能剩下约三格余量.

环的底部有两格厚, 因此开口从环所在的地面上方两格处开始. 在水下你可以直接游入或驶入. 在陆地上, 请建造台阶或坡道通到开口.

***

## <Color id="gold">野生传送门</Color>

传送门矗立在海床上的小型海晶石平台上. 每一座都是成对传送门的一半, 拥有自己的地址, 且不需要能量.

当任何东西第一次穿过野生传送门时, 其配对的另一半会在大约 1,500 格外的另一片海洋中建成, 而你会在那里出现. 从那时起, 两个环就成为一条固定路线. 事先不需要探索或加载任何区域.

在此改动之前生成的野生传送门初始均为青色, 它们会在环建成时采用自己的配对地址.

你可以像调整其他传送门一样重新调谐野生传送门. 给它一个你建造的环的地址, 它就会连接到那里, 而不是其配对的另一半. 给它一个没有其他环使用的地址, 它下一次旅行时就会为该地址建造一个新的另一半.

***

## <Color id="gold">制作与移动传送门</Color>

制作出的传送门是打包状态, 整个环都包含在其中. 放置后完整环会立即建成, 横跨你面朝的方向, 正面朝向你.

潜行并用扳手(<ItemLink id="aquarine_steel_wrench"/>或任何其他模组的扳手)右键点击已成型环的任意部分, 可将其重新打包. 你会取回一个打包的传送门, 并保留其地址, 因此你可以把野生传送门搬回家并保留其路线.

环矗立在传送门方块上, 需要宽 13 格, 高 13 格的空间. 它会建入空气, 水, 海带, 海草, 珊瑚以及其他可以覆盖放置的方块. 如果有固体方块阻挡, 它会作为裸传送门等待并告诉你位置. 佩戴<ItemLink id="prism_monocle"/>并看向传送门, 可看到所有阻挡方块以红色高亮. 清除它们后, 环会在几秒内自行完成, 或用扳手右键点击传送门立即重试.

已成型的环无法挖取任何东西. 破坏一部分的耗时与徒手破坏黑曜石相同, 不会掉落任何东西, 并使环的其余部分变回普通<ItemLink id="gateway_ring"/>. 请改用扳手.

要修复破损的环, 请将环节段放回下方的圆环中, 并用扳手右键点击传送门.

<GameScene zoom="2" background="#333333" interactive={true}>
  <Block id="nautec:gateway_ring" x="4" y="0" z="0"/>
  <Block id="nautec:gateway_ring" x="5" y="0" z="0"/>
  <Block id="nautec:gateway" x="6" y="0" z="0"/>
  <Block id="nautec:gateway_ring" x="7" y="0" z="0"/>
  <Block id="nautec:gateway_ring" x="8" y="0" z="0"/>
  <Block id="nautec:gateway_ring" x="2" y="1" z="0"/>
  <Block id="nautec:gateway_ring" x="3" y="1" z="0"/>
  <Block id="nautec:gateway_ring" x="4" y="1" z="0"/>
  <Block id="nautec:gateway_ring" x="5" y="1" z="0"/>
  <Block id="nautec:gateway_ring" x="6" y="1" z="0"/>
  <Block id="nautec:gateway_ring" x="7" y="1" z="0"/>
  <Block id="nautec:gateway_ring" x="8" y="1" z="0"/>
  <Block id="nautec:gateway_ring" x="9" y="1" z="0"/>
  <Block id="nautec:gateway_ring" x="10" y="1" z="0"/>
  <Block id="nautec:gateway_ring" x="1" y="2" z="0"/>
  <Block id="nautec:gateway_ring" x="2" y="2" z="0"/>
  <Block id="nautec:gateway_ring" x="3" y="2" z="0"/>
  <Block id="nautec:gateway_ring" x="9" y="2" z="0"/>
  <Block id="nautec:gateway_ring" x="10" y="2" z="0"/>
  <Block id="nautec:gateway_ring" x="11" y="2" z="0"/>
  <Block id="nautec:gateway_ring" x="1" y="3" z="0"/>
  <Block id="nautec:gateway_ring" x="2" y="3" z="0"/>
  <Block id="nautec:gateway_ring" x="10" y="3" z="0"/>
  <Block id="nautec:gateway_ring" x="11" y="3" z="0"/>
  <Block id="nautec:gateway_ring" x="0" y="4" z="0"/>
  <Block id="nautec:gateway_ring" x="1" y="4" z="0"/>
  <Block id="nautec:gateway_ring" x="11" y="4" z="0"/>
  <Block id="nautec:gateway_ring" x="12" y="4" z="0"/>
  <Block id="nautec:gateway_ring" x="0" y="5" z="0"/>
  <Block id="nautec:gateway_ring" x="1" y="5" z="0"/>
  <Block id="nautec:gateway_ring" x="11" y="5" z="0"/>
  <Block id="nautec:gateway_ring" x="12" y="5" z="0"/>
  <Block id="nautec:gateway_ring" x="0" y="6" z="0"/>
  <Block id="nautec:gateway_ring" x="1" y="6" z="0"/>
  <Block id="nautec:gateway_ring" x="11" y="6" z="0"/>
  <Block id="nautec:gateway_ring" x="12" y="6" z="0"/>
  <Block id="nautec:gateway_ring" x="0" y="7" z="0"/>
  <Block id="nautec:gateway_ring" x="1" y="7" z="0"/>
  <Block id="nautec:gateway_ring" x="11" y="7" z="0"/>
  <Block id="nautec:gateway_ring" x="12" y="7" z="0"/>
  <Block id="nautec:gateway_ring" x="0" y="8" z="0"/>
  <Block id="nautec:gateway_ring" x="1" y="8" z="0"/>
  <Block id="nautec:gateway_ring" x="11" y="8" z="0"/>
  <Block id="nautec:gateway_ring" x="12" y="8" z="0"/>
  <Block id="nautec:gateway_ring" x="1" y="9" z="0"/>
  <Block id="nautec:gateway_ring" x="2" y="9" z="0"/>
  <Block id="nautec:gateway_ring" x="10" y="9" z="0"/>
  <Block id="nautec:gateway_ring" x="11" y="9" z="0"/>
  <Block id="nautec:gateway_ring" x="1" y="10" z="0"/>
  <Block id="nautec:gateway_ring" x="2" y="10" z="0"/>
  <Block id="nautec:gateway_ring" x="3" y="10" z="0"/>
  <Block id="nautec:gateway_ring" x="9" y="10" z="0"/>
  <Block id="nautec:gateway_ring" x="10" y="10" z="0"/>
  <Block id="nautec:gateway_ring" x="11" y="10" z="0"/>
  <Block id="nautec:gateway_ring" x="2" y="11" z="0"/>
  <Block id="nautec:gateway_ring" x="3" y="11" z="0"/>
  <Block id="nautec:gateway_ring" x="4" y="11" z="0"/>
  <Block id="nautec:gateway_ring" x="5" y="11" z="0"/>
  <Block id="nautec:gateway_ring" x="6" y="11" z="0"/>
  <Block id="nautec:gateway_ring" x="7" y="11" z="0"/>
  <Block id="nautec:gateway_ring" x="8" y="11" z="0"/>
  <Block id="nautec:gateway_ring" x="9" y="11" z="0"/>
  <Block id="nautec:gateway_ring" x="10" y="11" z="0"/>
  <Block id="nautec:gateway_ring" x="4" y="12" z="0"/>
  <Block id="nautec:gateway_ring" x="5" y="12" z="0"/>
  <Block id="nautec:gateway_ring" x="6" y="12" z="0"/>
  <Block id="nautec:gateway_ring" x="7" y="12" z="0"/>
  <Block id="nautec:gateway_ring" x="8" y="12" z="0"/>
</GameScene>

***

## <Color id="gold">能量</Color>

从未被移动过的野生传送门不需要能量. 任何制作或移动过的传送门都需要 AP: 将激光对准环底部的传送门方块(见[激光能量](nautec:getting_started/laser_power.md)). 它可储存 5,000 AP, 开启时每 tick 消耗 100 AP. 储存达到 2,000 AP 后它会开启, 并保持开启直到缓冲耗尽, 因此至少供应 100 AP/t 的激光可让它在有人靠近时一直开启. 激光较弱时, 它会一次开启几秒, 然后关闭并重新充能到 2,000.

***

## <Color id="gold">开启</Color>

有配对目标的环会在玩家或潜艇进入约 12 格范围内时开启, 因此你可以直接驶入. 它会先拨号: 符号轨道旋转, 地址符号以其颜色亮起, 视界随之猛然张开. 所有人离开几秒后它会再次关闭.

向传送门方块输入红石信号会使环保持关闭.

***

## <Color id="gold">地址</Color>

九个地址符号中有四个承载地址: 从正面看分别为左上, 右上, 左下和右下. 每个可以是八种颜色之一, 共 4,096 个地址:

白色, 淡蓝色, 青色, 蓝色, 紫色, 品红色, 黄绿色和黑色.

更改地址不消耗任何东西. 有两种方法:

* 手持其中一种染料, 右键点击地址符号附近的环. 最近的符号会采用该颜色, 且染料不会被消耗.
* 空手右键点击环可打开地址界面. 第 1 到 4 行分别是左上, 右上, 左下和右下符号. 为每个选择一种颜色, 然后按设置.

透过<ItemLink id="prism_monocle"/>看向环的任意部分, 可读取其地址, 是否开启以及储存的能量.

***

## <Color id="gold">旅行</Color>

从任一侧穿过视界, 你就会从配对环的正面出来, 仍保持相同的速度, 并位于开口上相同的相对位置, 面朝远离环的方向. 你乘坐的任何东西都会随你同行, 骑乘它的其他人也一样, 因此潜艇会载着船员抵达. 生物和掉落物也可以通行.

* 如果远端环的正面被阻挡, 你会改从其背面出来. 如果两侧都被阻挡, 什么也不会发生, 你会像环关闭时一样直接穿过.
* 一次旅行后, 5 秒内任何东西都不能再次穿过传送门(`config/nautec-common.toml` 中的 `gatewayCooldown`, 100 tick), 因此你不会立刻被弹回.
* 远端环可以位于未加载的区块中. 传送门会在你旅行时加载它.
* 你总是抵达最近的配对环. 如果多个环共用一个地址, 请为每一对分配各自的地址, 以便抵达你想要的地点.

没有配对目标的环会保持黯淡, 并让所有东西直接穿过.

***

### <Color id="aqua">配方</Color>

<Recipe id="nautec:gateway"/>

<Recipe id="nautec:gateway_ring"/>
