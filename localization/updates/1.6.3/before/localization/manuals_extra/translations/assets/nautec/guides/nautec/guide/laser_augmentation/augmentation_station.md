---
navigation:
  title: 强化站
  icon: nautec:augmentation_station
  position: 1
  parent: laser_augmentation/laser_augmentation-index.md
item_ids:
  - nautec:augmentation_station
  - nautec:augmentation_station_extension
  - nautec:claw_robot_arm
---

# <Color id="light_purple">强化站</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="augmentation_station" scale="2"/>
  强化站是将强化安装到你身体中的多方块结构.
</Column>

你站在中间方块上, 周围的四个扩展单元放置部件, 它们的机械臂会完成安装.

***

## <Color id="gold">建造</Color>

该结构只有一层, 大小为 5 x 5, 四角留空:

* 中间是强化站.
* 它的正北, 正南, 正东和正西方向是磨制海晶石.
* 四条对角线方向是海蓝钢块.
* 每侧向外两格处各有一个强化站扩展单元.

<GameScene zoom="4" background="#333333" interactive={true}>
  <Block id="nautec:augmentation_station_extension" x="2" y="0" z="0"/>
  <Block id="nautec:aquarine_steel_block" x="1" y="0" z="1"/>
  <Block id="nautec:polished_prismarine" x="2" y="0" z="1"/>
  <Block id="nautec:aquarine_steel_block" x="3" y="0" z="1"/>
  <Block id="nautec:augmentation_station_extension" x="0" y="0" z="2"/>
  <Block id="nautec:polished_prismarine" x="1" y="0" z="2"/>
  <Block id="nautec:augmentation_station" x="2" y="0" z="2"/>
  <Block id="nautec:polished_prismarine" x="3" y="0" z="2"/>
  <Block id="nautec:augmentation_station_extension" x="4" y="0" z="2"/>
  <Block id="nautec:aquarine_steel_block" x="1" y="0" z="3"/>
  <Block id="nautec:polished_prismarine" x="2" y="0" z="3"/>
  <Block id="nautec:aquarine_steel_block" x="3" y="0" z="3"/>
  <Block id="nautec:augmentation_station_extension" x="2" y="0" z="4"/>
  <IsometricCamera yaw="225" pitch="30"/>
</GameScene>

手持 <ItemLink id="aquarine_steel_wrench"/> 右击中间的强化站方块(不要潜行)即可成型. 四个扩展单元必须全部就位, 即使你只使用其中一个. 破坏已成型强化站的任意方块都会使整体解除成型; 重新放回方块并再次使用扳手即可.

***

## <Color id="gold">装载扩展单元</Color>

右击已成型的扩展单元可将其打开. 它有两个槽位, 每个槽位放一件物品:

* 上方槽位放入 <ItemLink id="claw_robot_arm"/>. 没有它, 该扩展单元会被忽略.
* 下方槽位放入你想要安装的部件.

按强化所需部件数量装载相应数量的扩展单元. 几乎所有强化都只使用一个部件, 因此只装载一个扩展单元, 其余留空. 热泉甲壳是例外: 它需要在四个扩展单元中各放一个甲壳板. 只有当装载的扩展单元与该配方完全一致时强化站才会识别, 因此多装载一个扩展单元就不会提供任何可选项.

***

## <Color id="gold">供能</Color>

每个放有部件的扩展单元都需要至少 25 AP 的激光束从下方方块向上射入. 能量只被检测, 不会被消耗, 但在整个安装过程中必须保持 25 AP 或更高. 空扩展单元不需要光束.

由于光束必须从下方射入, 请将你的催化器或中继器放在地板下方并垂直向上发射. 关于如何产生光束, 见[激光能量](nautec:getting_started/laser_power.md).

25 AP 的阈值可以配置(`augmentationPowerRequirement`).

***

## <Color id="gold">使用</Color>

站在中间方块上. 半秒后强化站界面会打开. 你站在上面时它会实时更新, 因此你可以让它开着来装载部件或调整光束:

* 顶部状态栏显示强化站是否就绪, 若未就绪则显示原因. 将鼠标悬停其上可查看完整说明.
* 强化框会显示已装载部件所构成的强化及其作用.
* 四个扩展单元列会显示各自的部件, 若部件没有爪式机械臂则显示红色边框, 同时显示其获得的光束. 达到 25 AP 或更高时数字变绿, 低于该值时为红色. 将鼠标悬停在某一列上可查看详情.
* 将鼠标悬停在左侧的自己身上, 可查看你已经拥有的强化.

在底部选择身体槽位, 然后按下应用. 如果该槽位已经装有强化, 应用按钮会变红, 其提示会说明将被替换的内容. 如果你关闭了界面, 走下强化站再走回来即可重新打开. 站在未成型的强化站上时, 快捷栏上方会显示提示.

在接下来的四秒内你会被固定在原地, 由机械臂进行操作, 同时有进度条显示进度. 走下强化站, 光束低于 25 AP, 或部件被取出都会取消安装, 且不会消耗任何东西. 安装完成后, 部件会被消耗, 爪式机械臂保留, 强化则进入你选择的槽位.

[玩家强化](augmentation.md)列出了每个槽位可接受的强化以及替换强化的方式.

***

## <Color id="gold">配方</Color>

<Recipe id="nautec:augmentation_station"/>

<Recipe id="nautec:augmentation_station_extension"/>

<Recipe id="nautec:claw_robot_arm"/>

***

## <Color id="gold">更强的光束</Color>

每个使用中的扩展单元需要 25 AP. 更强的光束安装更快: 速度为 (光束 ÷ 25) 的平方根, 而安装按使用中最弱扩展单元的速度进行, 因此请均匀供能.

| 光束 | 速度 |
|---|---|
| 25 AP | ×1 (正常) |
| 100 AP | ×2 |
| 225 AP | ×3 |
| 400 AP | ×4 |

每次安装的四秒是每个扩展单元都为 25 AP 时的用时.

关于该规则及其适用的每台机器, 见[更强的光束](nautec:getting_started/stronger_beams.md).
