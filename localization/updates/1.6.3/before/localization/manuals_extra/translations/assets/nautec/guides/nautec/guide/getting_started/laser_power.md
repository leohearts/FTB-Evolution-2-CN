---
navigation:
  title: 激光能量
  icon: nautec:aquatic_catalyst
  position: 1
  parent: getting_started/getting_started-index.md
item_ids:
  - nautec:aquatic_catalyst
  - nautec:advanced_aquatic_catalyst
  - nautec:prismarine_crystal
---

# <Color id="light_purple">激光能量</Color>

<Column alignItems="center" fullWidth={true}>
  <ItemImage id="aquatic_catalyst" scale="2"/>
  海蓝催化器燃烧海晶石, 并将其作为激光束射出.
</Column>

海蓝科技 机器依靠激光能量运行, 以每 tick 的 AP(AP/t)计量. 光束携带两个值: 功率和纯度. 机器使用功率来运行, 配方在开始前会检查纯度.

光束只在两个激光方块之间形成. 发射方块需要在其那一侧有能接受光束的东西(机器, 中继器, 转接器, 透镜), 距离不超过 16 格(`config/nautec-common.toml` 中的 `laserDistance`), 距中继器则为 64 格, 且中间没有实心方块. 光束可以穿过水和玻璃, 因此可以用玻璃把光束围起来.

***

<Row>
  <ItemImage id="aquatic_catalyst"/>
  ### <Color id="aqua">海蓝催化器</Color>
</Row>

你的第一个能量来源. 它一次燃烧一个海晶石物品, 并从一个面射出一道光束.

<Recipe id="nautec:aquatic_catalyst"/>

手持一组燃料右键点击催化器可装入燃料, 或用漏斗供料. 用空手右键点击可取回尚未开始燃烧的燃料.

| 燃料 | 纯度 | 功率 | 燃烧时间 |
|---|---|---|---|
| 海晶碎片 | 0.4 | 12 AP/t | 30 秒 |
| 海晶水晶 | 0.8 | 6 AP/t | 30 秒 |
| <ItemLink id="prismarine_crystal_shard"/> | 1.2 | 20 AP/t | 75 秒 |

放置时你正看着的面是浅色的进料面, 上面有八个插槽, 装入燃料时会填充. 光束从相对的面射出, 即带有青色透镜的深色面. 放置时向下看可向下发射, 向上看可向上发射. <ItemLink id="aquarine_steel_wrench"/>可旋转已放置的催化器.

只有当发射面一侧存在接收方时, 催化器才会燃烧. 那里没有东西时, 它会保留燃料并等待, 因此没有目标的催化器不会浪费任何东西. 它会直接从一个燃料物品切换到下一个, 因此只要整组燃料还在, 光束就会持续. 一组 64 个碎片可运行 32 分钟.

红石信号会暂停它. 暂停的催化器不发射光束, 并保留其燃料以及正在燃烧物品的进度, 信号停止后会从暂停处继续.

与催化器除透镜面以外任意一面接触的<ItemLink id="budding_prismarine"/>会强化它. 每个方块为其功率增加 25%, 纯度增加 0.1, 最高纯度 2.0(`catalystBuddingOutputBonus`, `catalystBuddingPurityBonus` 和 `catalystBuddingMaxPurity`). 提供强化的海晶母岩不会生长任何东西: 催化器每秒会破坏其上任何海晶簇, 且没有掉落物.

每侧靠近透镜端的两盏小灯显示它是否找到接收方. 绿色表示范围内有激光方块接受该光束. 红色表示没有: 透镜前方没有任何东西, 有实心方块挡路, 或前方的方块不接受来自该侧的光束(中继器朝向错误是常见原因). 用空手潜行右键点击催化器, 可在聊天栏查看其燃料, 发射方向, 光束命中的对象以及如何修复.

<Color id="gold">提示</Color>: 光束会灼烧其中的任何东西, 包括你自己, 更强的光束灼烧得更厉害(参见[传输激光能量](nautec:laser_chemistry/laser_manipulation.md)). 请绕开正在运行的光束, 或让光束穿过玻璃.

***

<Row>
  <ItemImage id="advanced_aquatic_catalyst"/>
  ### <Color id="aqua">高级海蓝催化器</Color>
</Row>

带金色边框的海蓝催化器, 可同时燃烧八个燃料物品. 每次燃烧的持续时间与海蓝催化器中一个物品相同, 而光束携带八倍的功率, 因此一组碎片提供每 tick 160 AP 而不是 20, 耗尽速度也快八倍. 每个物品的能量相同; 只是更快地全部获得.

<Recipe id="nautec:advanced_aquatic_catalyst"/>

| 燃料 | 纯度 | 功率 | 燃烧时间 |
|---|---|---|---|
| 海晶碎片 | 0.44 | 96 AP/t | 30 秒 |
| 海晶水晶 | 0.88 | 48 AP/t | 30 秒 |
| <ItemLink id="prismarine_crystal_shard"/> | 1.32 | 160 AP/t | 75 秒 |

在没有任何海晶母岩强化之前, 其光束比海蓝催化器中使用相同燃料的光束纯 10%. 装入少于八个物品时, 它会燃烧现有的物品, 功率为相应倍数. 其他一切与海蓝催化器相同: 放置, 指示灯, 红石暂停, 海晶母岩和潜行右键点击读数. `advancedCatalystFuelMultiplier` 和 `advancedCatalystPurityMultiplier` 分别设定八倍和 10%.

***

## <Color id="gold">纯度</Color>

纯度在光束起始处确定. 催化器光束携带其燃料的纯度, 从 0.4 到 1.2, 再加上任何海晶母岩强化. 当两束或更多光束供给同一个方块时, 它们的功率相加, 纯度则保持在最纯光束附近. 结果是最高纯度减去它与所有光束平均值之间差距的四分之一(`beamMergePurityDrop`), 因此 3.0 的光束与 0 的光束合并后约为 2.6.

更高纯度来自<ItemLink id="prismarine_crystal"/>(3.0), <ItemLink id="bacterial_fuel_cell"/>(最高 2.5), 或添加到现有光束中的<ItemLink id="focusing_lens"/>. [光束光学](nautec:deep_engineering/beam_optics.md)介绍光束的转向, 分流和聚焦.

***

<Row>
  <ItemImage id="prismarine_crystal"/>
  ### <Color id="aqua">海棱水晶</Color>
</Row>

一种六格高的水晶, 立于海底下的水晶晶洞中(参见[结构](structures.md)). 它会把任何光束变成纯度 3.0 的光束. 野生水晶固定原地, 但你可以培育一株可移动的: 参见[水晶培育](nautec:deep_engineering/crystal_cultivation.md).

从侧面将光束射入水晶. 它的六个方块中的任何一个都能在四个侧面中的任意一面接受光束, 来自多个源头的光束会相加. 然后顶部方块向上直射, 底部方块向下直射, 两者纯度均为 3.0. 如果只有其中一束到达接收方, 该光束携带全部输入功率. 如果两束都到达, 功率在它们之间平均分配, 因此水晶输出的 AP 绝不会多于输入. 这两道光束会一直运行, 直到到达接收方或实心方块, 因此射向空地面或空天花板也有效.

水晶会留在生成的位置, 因此请围绕它建造. 开启能力的海蓝钢镐可以从它上面敲下[海棱水晶碎片](nautec:laser_chemistry/crystal_shards.md), 但每次命中都有概率击碎整株水晶.

***

## <Color id="gold">传输能量</Color>

* [传输激光能量](nautec:laser_chemistry/laser_manipulation.md): 海晶石激光中继器传递光束, 激光转接器合并和分流光束.
* [光束光学](nautec:deep_engineering/beam_optics.md): 聚焦透镜, 用于提高纯度.
* [充能器](nautec:laser_chemistry/charger.md)和[海晶电池](nautec:laser_chemistry/prismatic_battery.md): 将能量储存在物品中.

戴上<ItemLink id="prism_monocle"/>可读取任何激光方块处到达的功率和纯度.

***

## <Color id="gold">更强的光束</Color>

机器的 AP 数值是运行所需的最低值, 而不是消耗. 比这更强的光束绝不会浪费: 大多数机器会因此运行得更快, 倍率为(光束 ÷ 所需值)的平方根, 因此四倍的功率会让机器以两倍速度运行. [更强的光束](nautec:getting_started/stronger_beams.md)给出了完整规则和机器列表.
