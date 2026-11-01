---
navigation:
  title: 共鸣网络
  icon: nautec:resonance_node
  position: 9
  parent: deep_engineering/deep_engineering-index.md
item_ids:
  - nautec:prismatic_emitter
  - nautec:tuning_fork
  - nautec:resonance_charm
---

# <Color id="light_purple">共鸣网络</Color>

<Column alignItems="center" fullWidth={true}>
  <Row>
    <ItemImage id="uplink_array" scale="2"/>
    <ItemImage id="resonance_node" scale="2"/>
  </Row>
  一种具名网络, 可在你的基地之间无线传输激光能量(AP)和 Forge 能量(FE).
</Column>

共鸣网络连接<ItemLink id="uplink_array"/>, [共鸣节点](resonance_node.md)和共鸣护符, 无论相距多远, 也无论处于哪个维度. 已发射卫星的上行链路阵列是网络的核心: 输入节点和线缆为其供能, 它再将 AP 和 FE 发送到输出节点和护符. 核心见[棱镜卫星](prism_satellite.md), 能量的输入与输出见[共鸣节点](resonance_node.md).

***

## <Color id="gold">设置</Color>

1. 放置一个<ItemLink id="resonance_node"/>或<ItemLink id="uplink_array"/>, 并用空手右键点击它.
2. 在框中输入名称并按**创建**. 该网络归你所有, 此方块会加入其中.
3. 打开下一个节点或阵列, 无论它在何处, 并使用箭头选择同一个网络.

节点和阵列只在其区块加载时工作. 在方块界面中开启**加载**, 它就会保持自身区块加载, 因此长距离链路会在你离开时继续运行, 除非服务器已关闭该功能(`resonanceChunkLoading`).

***

## <Color id="gold">谁可以使用</Color>

只有所有者及其信任的玩家才能将方块连接到网络, 或打开已接入网络的方块. 其他任何人都会收到一条消息, 指明该网络及其所有者.

所有者可从网络上的任意节点或阵列管理访问权限:

* **信任:** 输入在线玩家的名称并按信任. 他们现在可以将方块连接到该网络. 点击其名称旁的红色 x 可移除.
* **队伍:** 安装 FTB Teams 后, 开启此项可使所有者队伍中的所有成员使用该网络, 无需逐一信任他们.
* **删除:** 移除网络并断开其上的每个方块. 需点击两次.

每位玩家最多可拥有 16 个网络.

***

<Row>
  <ItemImage id="prismatic_emitter"/>
  ### <Color id="aqua">海晶发射器</Color>
</Row>

无需线缆即可为附近的机器供能. 从线缆或紧贴它放置的输出共鸣节点向其输入 FE, 然后连接它应供能的机器. 它会向每台机器发射水晶连接线, 并在它们之间共享最多 10,000 FE/t, 途中没有损耗.

1. 手持<ItemLink id="tuning_fork"/>右键点击发射器, 将音叉调谐到它.
2. 右键点击每台机器以连接. 再次右键点击已连接的机器可断开.

调谐后的音叉可用同样的方式连接另一个发射器, 因此能量可以从一个发射器跳到另一个, 以到达更远的机器. 链条不能回环到其起始发射器. 要将音叉调谐到另一个发射器, 请先潜行右键点击空气. 破坏已连接的机器或发射器会移除其连接线.

发射器可触及最远 64 格外的机器(`emitterRange`), 并可为其中 16 台供能. 只有放置它的玩家才能将音叉调谐到它. 手持音叉潜行右键点击发射器可断开所有连接, 或潜行右键点击空气以清除音叉.

***

<Row>
  <ItemImage id="resonance_charm"/>
  ### <Color id="aqua">共鸣护符</Color>
</Row>

无论你身在何处, 都能从网络为你携带的物品充能.

手持护符右键点击共鸣节点或上行链路阵列, 可将其绑定到该网络; 你需要拥有该网络的访问权限. 然后将其佩戴在护符槽中. 它每半秒从网络的[上行链路阵列](prism_satellite.md)中抽取 FE, 无论处于哪个维度, 并为你物品栏, 盔甲和饰品槽中的 FE 物品充能, 以及为依靠激光能量运行的 海蓝科技 物品充能, 例如<ItemLink id="atlantean_rifle"/>和<ItemLink id="prismatic_battery"/>. 它每 tick 最多传输 2,000 FE, 途中会损失 10%, 与输出节点相同.

其水晶还会起到<ItemLink id="prism_monocle"/>的作用: 装备它时, 无需佩戴单片镜即可看到激光方块上的功率和纯度读数, 以及更清晰的水下视野.

如果所有者不再信任你, 护符会停止工作, 直到你再次被信任. 手持它右键点击空气可打开其界面. 界面会显示它绑定的网络, 所有者, 网络中的上行链路和输出节点数量, 以及上行链路持有的 FE. 它还可设置护符的优先级: 优先级较高的护符会先于优先级较低的输出节点和护符充能. 手持它潜行右键点击空气可解除绑定.

### <Color id="aqua">共鸣强化体</Color>

要腾出护符槽, 可将护符作为强化体安装. 像其他部件一样将其装入[强化站](nautec:laser_augmentation/augmentation_station.md), 并装入你的头部槽位. 该强化体会保留护符的网络和优先级, 并像佩戴的护符一样为你的物品充能, 包括单片镜读数. 死亡时它会保留.

要将其调谐到其他网络, 请空手潜行右键点击共鸣节点或上行链路阵列. 要查看其网络或更改优先级, 请打开强化体界面(默认按 B), 然后点击头部一行. 如果你同时佩戴了已绑定的护符, 则优先使用护符, 强化体会等待.
